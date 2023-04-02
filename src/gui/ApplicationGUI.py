from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QLayout,
)
from PyQt5.uic import loadUi
from PyQt5.Qt import Qt

from src.constants import (
    APP_SIZE,
    APP_NAME,
)
from src.interfaces import (
    IGUIComponent,
    ISystem,
)


class ApplicationGUI(QMainWindow):
    def __init__(self, system: 'ISystem', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.system = system
        self.setWindowTitle(APP_NAME)
        self.resize(*APP_SIZE)
        self.__layouts = {}

    @property
    def layouts(self) -> dict:
        return self.__layouts

    def load_layout(self, path: str):
        loadUi(path, self)

    def add_component(self, component: 'IGUIComponent', layout: str):
        self.findChild(QLayout, layout).layout().addWidget(component)
