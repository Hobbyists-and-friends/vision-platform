from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QLayout,
    QDesktopWidget,
)
from PyQt5.uic import loadUi

from src.constants import (
    APP_SIZE,
    APP_NAME,
)
from src.interfaces import (
    IGUIComponent,
    ISystem,
)
from src.utils import (
    find_all_layouts,
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
        app_size = self.__get_app_size()
        self.resize(*app_size)
        self.setMaximumSize(*app_size)
        self.setMinimumSize(*app_size)
        self.__layouts = {}
        self.__clearCentralWidget()

    def __get_app_size(self) -> tuple:
        """
        Get the size of the application.

        Returns:
            tuple: The size of the application.
        """
        screen_size = QDesktopWidget().availableGeometry()
        return (screen_size.width() * 0.95, screen_size.height() * 0.95)

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
        # self.layouts[layout].addWidget(component)
        self.central_widget.findChild(
            QLayout, layout).layout().addWidget(component)

    def __clearCentralWidget(self):
        """
        Clear the central widget.
        """
        # child_widgets = self.central_widget.findChildren(QWidget)

        # for child_widget in child_widgets:
        #     child_widget.deleteLater()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
