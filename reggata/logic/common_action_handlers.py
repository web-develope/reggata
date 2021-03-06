'''
Created on 23.12.2012
@author: vlkv
'''
import logging
import os
import reggata.data.db_schema as db
import reggata.helpers as hlp
import reggata.errors as err
import reggata.data.commands as cmds
from reggata.logic.handler_signals import HandlerSignals
from reggata.logic.action_handlers import AbstractActionHandler
from reggata.gui.item_dialog import ItemDialog
from reggata.logic.worker_threads import UpdateGroupOfItemsThread
from reggata.logic.worker_threads import BackgrThread
from reggata.logic.worker_threads import CreateGroupOfItemsThread
from reggata.gui.items_dialog import ItemsDialog


logger = logging.getLogger(__name__)



class AddItemAlgorithms(object):

    @staticmethod
    def addItems(tool, dialogs, listOfPaths):
        '''
            Creates and saves in repository a number of items linked with files defined by given listOfPaths.
        listOfPaths is a list of paths to files and directories. Depending on the elements of
        listOfPaths one or another add algorithm is chosen.
            Returns a tuple (itemsCreatedCount, filesSkippedCount, listOfSavedItemIds) or raises
        an exception.
        '''
        itemsCreatedCount = 0
        filesSkippedCount = 0
        lastSavedItemIds = []

        if len(listOfPaths) == 0:
            # User wants to add a single Item without any file
            savedItemId = AddItemAlgorithms.addSingleItem(tool, dialogs)
            itemsCreatedCount += 1
            lastSavedItemIds.append(savedItemId)

        elif len(listOfPaths) == 1:
            file = listOfPaths[0]
            if os.path.isdir(file):
                # User wants to create Items for all files in selected directory
                created, skipped, savedItemIds = \
                    AddItemAlgorithms.addManyItemsRecursively(tool, dialogs, [file])
                itemsCreatedCount += created
                filesSkippedCount += skipped
                lastSavedItemIds.extend(savedItemIds)
            else:
                # User wants to add single Item with file
                savedItemId = AddItemAlgorithms.addSingleItem(tool, dialogs, file)
                itemsCreatedCount += 1
                lastSavedItemIds.append(savedItemId)
        else:
            # User wants to create Items for a whole list of files and dirs
            created, skipped, savedItemIds = \
                AddItemAlgorithms.addManyItemsRecursively(tool, dialogs, listOfPaths)
            itemsCreatedCount += created
            filesSkippedCount += skipped
            lastSavedItemIds.extend(savedItemIds)
        return (itemsCreatedCount, filesSkippedCount, lastSavedItemIds)


    @staticmethod
    def addSingleItem(tool, dialogs, file=None):
        '''
            Creates and saves in repo an Item linked with a given file (or without file).
        Returns id of saved Item, or raises an exception.
        '''
        savedItemId = None

        item = db.Item(user_login=tool.user.login)
        if not hlp.is_none_or_empty(file):
            file = os.path.normpath(file)
            item.title, _ = os.path.splitext(os.path.basename(file))
            item.data_ref = db.DataRef(objType=db.DataRef.FILE, url=file)

        if not dialogs.execItemDialog(
            item=item, gui=tool.gui, repo=tool.repo, dialogMode=ItemDialog.CREATE_MODE):
            raise err.CancelOperationError("User cancelled operation.")

        uow = tool.repo.createUnitOfWork()
        try:
            srcAbsPath = None
            dstRelPath = None
            if item.data_ref is not None:
                srcAbsPath = item.data_ref.srcAbsPath
                dstRelPath = item.data_ref.dstRelPath

            cmd = cmds.SaveNewItemCommand(item, srcAbsPath, dstRelPath)
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
            Creates and saves in repository items linked with given list of files (filenames).
        Returns a tuple (itemsCreatedCount, filesSkippedCount, listOfSavedItemIds) or raises an
        exception.
        '''
        if len(files) <= 1:
            raise ValueError("You should give more than one file.")

        items = []
        for file in files:
            file = os.path.normpath(file)
            item = db.Item(user_login=tool.user.login)
            item.title, _ = os.path.splitext(os.path.basename(file))
            item.data_ref = db.DataRef(objType=db.DataRef.FILE, url=file) #DataRef.url can be changed in ItemsDialog
            item.data_ref.srcAbsPath = file
            items.append(item)

        if not dialogs.execItemsDialog(
            items, tool.gui, tool.repo, ItemsDialog.CREATE_MODE, sameDstPath=True):
            raise err.CancelOperationError("User cancelled operation.")

        thread = CreateGroupOfItemsThread(tool.gui, tool.repo, items)

        dialogs.startThreadWithWaitDialog(
                thread, tool.gui, indeterminate=False)

        return (thread.createdCount, thread.skippedCount, thread.lastSavedItemIds)


    @staticmethod
    def addManyItemsRecursively(tool, dialogs, listOfPaths):
        '''
            Creates and saves in repository a number of items linked with files defined by given listOfPaths.
        listOfPaths is a list of paths to files and directories. For every file an Item is created.
        Every directory is scanned recursively and for every file found an Item is created.
        Returns a tuple (itemsCreatedCount, filesSkippedCount, listOfSavedItemIds) or raises
        an exception.
        '''
        items = []
        for path in listOfPaths:
            path = os.path.normpath(path)

            if os.path.isfile(path):
                file = path
                item = db.Item(user_login=tool.user.login)
                item.title, _ = os.path.splitext(os.path.basename(file))
                srcAbsPath = os.path.abspath(file)
                item.data_ref = db.DataRef(objType=db.DataRef.FILE, url=srcAbsPath) #DataRef.url can be changed in ItemsDialog
                item.data_ref.srcAbsPath = srcAbsPath
                item.data_ref.srcAbsPathToRoot = os.path.dirname(file)
                # item.data_ref.dstRelPath will be set by ItemsDialog
                items.append(item)
            elif os.path.isdir(path):
                dirPath = path
                for root, _dirs, files in os.walk(dirPath):
                    if os.path.relpath(root, dirPath) == ".reggata":
                        continue
                    for file in files:
                        item = db.Item(user_login=tool.user.login)
                        item.title, _ = os.path.splitext(os.path.basename(file))
                        srcAbsPath = os.path.join(root, file)
                        item.data_ref = db.DataRef(objType=db.DataRef.FILE, url=srcAbsPath) #DataRef.url can be changed in ItemsDialog
                        item.data_ref.srcAbsPath = srcAbsPath
                        item.data_ref.srcAbsPathToRoot = os.path.join(dirPath, "..")
                        # item.data_ref.dstRelPath will be set by ItemsDialog
                        items.append(item)
            else:
                logger.info("Skipping path '{}'".format(path))

        if not dialogs.execItemsDialog(
            items, tool.gui, tool.repo, ItemsDialog.CREATE_MODE, sameDstPath=False):
            raise err.CancelOperationError("User cancelled operation.")

        thread = CreateGroupOfItemsThread(tool.gui, tool.repo, items)

        dialogs.startThreadWithWaitDialog(
                thread, tool.gui, indeterminate=False)

        return (thread.createdCount, thread.skippedCount, thread.lastSavedItemIds)



class EditItemsActionHandler(AbstractActionHandler):
    def __init__(self, tool, dialogs):
        super(EditItemsActionHandler, self).__init__(tool)
        self._dialogs = dialogs

    def handle(self):
        try:
            self._tool.checkActiveRepoIsNotNone()
            self._tool.checkActiveUserIsNotNone()

            itemIds = self._tool.gui.selectedItemIds()
            if len(itemIds) == 0:
                raise err.MsgException(self.tr("There are no selected items."))

            if len(itemIds) > 1:
                updated, skipped = self.__editManyItems(itemIds)
            else:
                updated, skipped = self.__editSingleItem(itemIds.pop())

            self._emitHandlerSignal(HandlerSignals.STATUS_BAR_MESSAGE,
                self.tr("Editing done. Updated={}, skipped={} items.".format(updated, skipped)))
            self._emitHandlerSignal(HandlerSignals.ITEM_CHANGED)

        except Exception as ex:
            hlp.show_exc_info(self._tool.gui, ex)



    def __editSingleItem(self, itemId):
        updated, skipped = 0, 0
        uow = self._tool.repo.createUnitOfWork()
        try:
            item = uow.executeCommand(cmds.GetExpungedItemCommand(itemId))

            if not self._dialogs.execItemDialog(
                item=item, gui=self._tool.gui, repo=self._tool.repo, dialogMode=ItemDialog.EDIT_MODE):
                return updated, skipped

            srcAbsPath = item.data_ref.srcAbsPath if item.data_ref is not None else None
            dstRelPath = item.data_ref.dstRelPath if item.data_ref is not None else None
            cmd = cmds.UpdateExistingItemCommand(item, srcAbsPath, dstRelPath, self._tool.user.login)
            uow.executeCommand(cmd)
            updated += 1
        except:
            skipped += 1
        finally:
            uow.close()
        return updated, skipped

    def __editManyItems(self, itemIds):
        updated, skipped = 0, 0
        uow = self._tool.repo.createUnitOfWork()
        try:
            items = []
            for itemId in itemIds:
                items.append(uow.executeCommand(cmds.GetExpungedItemCommand(itemId)))

            if not self._dialogs.execItemsDialog(
                items, self._tool.gui, self._tool.repo, ItemsDialog.EDIT_MODE, sameDstPath=False):
                return updated, skipped

            thread = UpdateGroupOfItemsThread(self._tool.gui, self._tool.repo, items)
            self._dialogs.startThreadWithWaitDialog(thread, self._tool.gui, indeterminate=False)
            updated = thread.updatedCount
            skipped = thread.skippedCount
        finally:
            uow.close()
        return updated, skipped
