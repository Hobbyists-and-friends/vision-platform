from PyQt5.QtWidgets import QWidget
from abc import ABCMeta


class PyQtMetaClass(type(QWidget), ABCMeta):
    pass
