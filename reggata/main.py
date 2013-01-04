# -*- coding: utf-8 -*-
'''
Copyright 2010 Vitaly Volkov

This file is part of Reggata.

Reggata is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Reggata is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Reggata.  If not, see <http://www.gnu.org/licenses/>.

Created on 21.01.2012

@author: vlkv
'''
import os.path
import sys
import codecs
import logging.config
import PyQt4.QtCore as QtCore
from PyQt4.QtGui import QApplication
import reggata.consts as consts
from reggata.user_config import UserConfig
import reggata.logging_default_conf as logging_default_conf
from reggata.gui.main_window import MainWindow

logger = logging.getLogger(consts.ROOT_LOGGER + "." + __name__)


def configureLogging():
    if not os.path.exists(consts.USER_CONFIG_DIR):
        os.makedirs(consts.USER_CONFIG_DIR)

    if not os.path.exists(consts.LOGGING_CONFIG_FILE):
        f = codecs.open(consts.LOGGING_CONFIG_FILE, "w", "utf-8")
        try:
            f.write(logging_default_conf.loggingDefaultConf)
        finally:
            f.close()

    logging.config.fileConfig(os.path.join(consts.LOGGING_CONFIG_FILE))


def configureTmpDir():
    if not os.path.exists(consts.DEFAULT_TMP_DIR):
        os.makedirs(consts.DEFAULT_TMP_DIR)


def configureTranslations(app):
    qtr = QtCore.QTranslator(app)
    language = UserConfig().get("language")
    if language:
        qm_filename = "reggata_{}.qm".format(language)

        reggataDir = os.path.dirname(__file__)
        isQmLoaded = qtr.load(qm_filename, os.path.join(reggataDir, "locale"))
        if not isQmLoaded:
            isQmLoaded = qtr.load(qm_filename, os.path.join(reggataDir, "..", "locale"))

        if isQmLoaded:
            QtCore.QCoreApplication.installTranslator(qtr)
        else:
            logger.warning("Cannot find translation file {}.".format(qm_filename))



def main():
    configureLogging()

    logger.info("========= Reggata started =========")
    logger.debug("pyqt_version = {}".format(QtCore.PYQT_VERSION_STR))
    logger.debug("qt_version = {}".format(QtCore.QT_VERSION_STR))
    logger.debug("current dir is " + os.path.abspath("."))
    logger.debug("__file__ is " + __file__)
    logger.debug("os.path.abspath(__file__) is " + os.path.abspath(__file__))

    configureTmpDir()

    app = QApplication(sys.argv)

    configureTranslations(app)

    form = MainWindow()
    form.show()
    app.exec_()
    logger.info("========= Reggata finished =========")


if __name__ == '__main__':
    main()