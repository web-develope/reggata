'''
Created on 23.12.2012
@author: vlkv
'''
from reggata.logic.handler_signals import HandlerSignals
import reggata.consts as consts
from reggata.data.commands import *
from reggata.logic.action_handlers import AbstractActionHandler
from reggata.gui.item_dialog import ItemDialog
from reggata.logic.worker_threads import UpdateGroupOfItemsThread, BackgrThread, CreateGroupOfItemsThread
from reggata.gui.items_dialog import ItemsDialog


class AddItemAlgorithms(object):
    
    @staticmethod
    def addSingleItem(tool, dialogs, file=None):
        '''
            Creates and saves in repo an Item linked with a given file (or without file). 
        Returns id of saved Item, or raises an exception.
        '''
        savedItemId = None

        item = Item(user_login=tool.user.login)
        if not helpers.is_none_or_empty(file):
            file = os.path.normpath(file)
            item.title, _ = os.path.splitext(os.path.basename(file))
            item.data_ref = DataRef(type=DataRef.FILE, url=file)

        if not dialogs.execItemDialog(
            item=item, gui=tool.gui, repo=tool.repo, dialogMode=ItemDialog.CREATE_MODE):
            raise CancelOperationError("User cancelled operation.")
        
        uow = tool.repo.createUnitOfWork()
        try:
            srcAbsPath = None
            dstRelPath = None
            if item.data_ref is not None:
                srcAbsPath = item.data_ref.srcAbsPath
                dstRelPath = item.data_ref.dstRelPath

            cmd = SaveNewItemCommand(item, srcAbsPath, dstRelPath)
            thread = BackgrThread(tool.gui, uow.executeCommand, cmd)
            
            dialogs.startThreadWithWaitDialog(
                thread, tool.gui, indeterminate=True)
            
            savedItemId = thread.result
            
        finally:
            uow.close()
            
        return savedItemId
    
    @staticmethod
    def addManyItems(tool, dialogs, files):
        '''
            Creates items linked with given list of files (filenames). 
        Returns a tuple (itemsCreatedCount, filesSkippedCount, listOfSavedItemIds)
        '''
        if len(files) <= 1:
            raise ValueError("You should give more than one file.")
        
        items = []
        for file in files:
            file = os.path.normpath(file)
            item = Item(user_login=tool.user.login)
            item.title, _ = os.path.splitext(os.path.basename(file))
            item.data_ref = DataRef(type=DataRef.FILE, url=file) #DataRef.url can be changed in ItemsDialog
            item.data_ref.srcAbsPath = file
            items.append(item)
        
        if not dialogs.execItemsDialog(
            items, tool.gui, tool.repo, ItemsDialog.CREATE_MODE, sameDstPath=True):
            raise CancelOperationError("User cancelled operation.")
        
        thread = CreateGroupOfItemsThread(tool.gui, tool.repo, items)
        
        dialogs.startThreadWithWaitDialog(
                thread, tool.gui, indeterminate=False)
            
        return (thread.createdCount, thread.skippedCount, thread.lastSavedItemIds)


class EditItemActionHandler(AbstractActionHandler):
    def __init__(self, tool, dialogs):
        super(EditItemActionHandler, self).__init__(tool)
        self._dialogs = dialogs
        
    def handle(self):
        try:
            self._tool.checkActiveRepoIsNotNone()
            self._tool.checkActiveUserIsNotNone()            
            
            itemIds = self._tool.gui.selectedItemIds()
            if len(itemIds) == 0:
                raise MsgException(self.tr("There are no selected items."))
            
            if len(itemIds) > 1:
                self.__editManyItems(itemIds)
            else:
                self.__editSingleItem(itemIds.pop())
                            
        except Exception as ex:
            show_exc_info(self._tool.gui, ex)
            
        else:
            self._emitHandlerSignal(HandlerSignals.STATUS_BAR_MESSAGE, 
                                    self.tr("Editing done."), consts.STATUSBAR_TIMEOUT)
            self._emitHandlerSignal(HandlerSignals.ITEM_CHANGED)
            
    
    def __editSingleItem(self, itemId):
        uow = self._tool.repo.createUnitOfWork()
        try:
            item = uow.executeCommand(GetExpungedItemCommand(itemId))
            
            if not self._dialogs.execItemDialog(
                item=item, gui=self._tool.gui, repo=self._tool.repo, dialogMode=ItemDialog.EDIT_MODE):
                return
            
            cmd = UpdateExistingItemCommand(item, self._tool.user.login)
            uow.executeCommand(cmd)
        finally:
            uow.close()
    
    def __editManyItems(self, itemIds):
        uow = self._tool.repo.createUnitOfWork()
        try:
            items = []
            for itemId in itemIds:
                items.append(uow.executeCommand(GetExpungedItemCommand(itemId)))
            
            if not self._dialogs.execItemsDialog(
                items, self._tool.gui, self._tool.repo, ItemsDialog.EDIT_MODE, sameDstPath=True):
                return
            
            thread = UpdateGroupOfItemsThread(self._tool.gui, self._tool.repo, items)
            self._dialogs.startThreadWithWaitDialog(thread, self._tool.gui, indeterminate=False)
                
        finally:
            uow.close()
