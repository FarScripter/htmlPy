from PyQt4 import QtCore

Bridge = QtCore.QObject
attach = QtCore.pyqtSlot

from .web_app_window import WebAppWindow
from .app_window import AppWindow
