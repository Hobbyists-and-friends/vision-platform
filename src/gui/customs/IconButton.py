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
from .ComponentBase import ComponentBase


class IconButton(ComponentBase, QPushButton):
    def __init__(self, system: 'ISystem',
                 component_id: str,
                 text: str):
        QPushButton.__init__(self)
        ComponentBase.__init__(self, system, component_id)
        self.clicked.connect(self._click)
        self.setText(text)

    def __repr__(self):
        return f'<IconButton name={self.component_id} />'

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def _click(self):
        self.notify()
