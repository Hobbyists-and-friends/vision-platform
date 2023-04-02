from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
)
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

        self.show()

    def add_component(self, component: 'IGUIComponent', layout_name: str):
        pass

    def load_layout(self, path: str):
        pass
