from PyQt5.QtWidgets import QWidget
from abc import ABCMeta


# this part is used for synchronize the meta class of PyQt5.QtWidgets.QWidget and abc.ABCMeta
class PyQtMetaClass(type(QWidget), ABCMeta):
    pass
