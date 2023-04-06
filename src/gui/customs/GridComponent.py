from abc import ABCMeta
from PyQt5.QtWidgets import (
    QWidget,
)

from src.interfaces import (
    IGUIComponent,
)
from src.constants import (
    DEFAULT_COLUMN,
    DEFAULT_ROW,
)
from src.interfaces import (
    PyQtMetaClass,
    IGUIComponent,
    IPublisher,
)




# Not implement
class GridComponent(QWidget, IGUIComponent, metaclass=PyQtMetaClass):
    def __init__(self, *args,
                 columns=DEFAULT_COLUMN,
                 rows=DEFAULT_ROW,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.__columns = columns
        self.__rows = rows

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
