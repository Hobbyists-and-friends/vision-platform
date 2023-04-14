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
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

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
        self.__clearCentralWidget()
        loadUi(path, self.central_widget)

    def add_component(self, component: 'IGUIComponent', layout: str) -> None:
        """
        Add the given component to the given layout.

        Args:
            component: IGUIComponent
                The component which will be added to the layout.
        """
        self.central_widget.findChild(
            QLayout, layout).layout().addWidget(component)

    def __clearCentralWidget(self):
        """
        Clear the central widget.
        """
        child_widgets = self.central_widget.findChildren(QWidget)

        for child_widget in child_widgets:
            child_widget.deleteLater()
