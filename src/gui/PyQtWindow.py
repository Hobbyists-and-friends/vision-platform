import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QLayout,
    QDesktopWidget,
    QApplication,
)
from PyQt5.uic import loadUi

from src.constants import (
    APP_SIZE,
    APP_NAME,
)
from src.interfaces.ui import (
    IWindow,
    PyQtMetaClass,
)
from src.cores import (
    System,
)


class PyQtWindow(QApplication, IWindow, metaclass=PyQtMetaClass):
    """
    The main window of this application which will be manipulated by all operations.

    Attributes:
        system: ISystem
            The system object which is passed to all objects in this platform.

        layouts: dict
            The dictionary which stores all layouts in this application.
    """

    def __init__(self, layout, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__layout = layout

    def init(self) -> None:
        """
        Initialize the application.
        """
        self.app = QMainWindow()
        self.app.setWindowTitle(APP_NAME)
        app_size = self.__get_app_size()
        self.app.resize(*app_size)
        self.app.setMaximumSize(*app_size)
        self.app.setMinimumSize(*app_size)
        self.central_widget = QWidget()
        self.load_layout(self.__layout)
        self.app.show()

    def update(self) -> None:
        pass

    def exit(self) -> None:
        """
        Exit the PyqtWindow.
        """
        sys.exit(self.exec_())

    def __get_app_size(self) -> tuple:
        """
        Get the size of the application.

        Returns:
            tuple: The size of the application.
        """
        screen_size = QDesktopWidget().availableGeometry()
        return (screen_size.width() * 0.95, screen_size.height() * 0.95)

    def load_layout(self, path: str) -> None:
        """
        Load the layout from the given path.

        Args:
            path: str
                The path to the layout file.
        """
        self.clear()
        loadUi(path, self.central_widget)

    def add_component(self, component_id: str, layout: str) -> None:
        """
        Add the given component to the given layout.

        Args:
            component_id: str
                The component id which will be added to the layout.
        """
        component = System.system.ui_components[component_id]
        self.central_widget.findChild(
            QLayout, layout).layout().addWidget(component)

        component.init()

    def clear(self):
        """
        Clear the central widget.
        """
        # child_widgets = self.central_widget.findChildren(QWidget)

        # for child_widget in child_widgets:
        #     child_widget.deleteLater()
        self.central_widget = QWidget()
        self.app.setCentralWidget(self.central_widget)
