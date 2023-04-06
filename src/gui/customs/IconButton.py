from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
)
from copy import copy

from src.interfaces import (
    IGUIComponent,
    PyQtMetaClass,
    IPublisher,
    ISystem,
)
from src.utils import (
    PublisherBase,
)
from src.constants import (
    ICON_BUTTON_DEFAULT_OPERATION,
)


class IconButton(QPushButton, PublisherBase, IGUIComponent, metaclass=PyQtMetaClass):
    def __init__(self, name: str, system: 'ISystem'):
        super().__init__()
        PublisherBase.__init__(self)
        self.__name = name
        self.system = system
        self.__operation = copy(ICON_BUTTON_DEFAULT_OPERATION)
        self.clicked.connect(self._click)
        self.setText(name)

    @property
    def component_id(self) -> str:
        return self.__name

    def __repr__(self):
        return f'<IconButton name={self.__name} />'

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def assign_operation(self, operation: str):
        self.__operation = operation

    def _click(self):
        self.notify()
