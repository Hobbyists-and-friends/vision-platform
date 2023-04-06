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
    """
    The main window of this application which will be manipulated by all operations. 

    Attributes:
        system: ISystem
            The system object which is passed to all objects in this platform.

        layouts: dict
            The dictionary which stores all layouts in this application.
    """

    def __init__(self, system: 'ISystem', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.system = system
        self.setWindowTitle(APP_NAME)
        self.resize(*APP_SIZE)
        self.__layouts = {}

    @property
    def layouts(self) -> dict:
        return self.__layouts

    def load_layout(self, path: str) -> None:
        """
        Load the layout from the given path.

        Args:
            path: str
                The path to the layout file.
        """
        loadUi(path, self)

    def add_component(self, component: 'IGUIComponent', layout: str) -> None:
        """
        Add the given component to the given layout.

        Args:
            component: IGUIComponent
                The component which will be added to the layout.
        """
        self.findChild(QLayout, layout).layout().addWidget(component)
