from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
)
from abc import (
    abstractmethod,
)

from src.interfaces.ui import (
    IUIComponent,
    PyQtMetaClass,
)


class PyQtComponentBase(IUIComponent, QWidget, metaclass=PyQtMetaClass):
    def __init__(self, horizontal=False) -> None:
        super().__init__()

        self._layout = QVBoxLayout() if not horizontal else QHBoxLayout()
        self._label = QLabel()
        self._layout.addWidget(self._label)
        self.setLayout(self._layout)

    def _add_widget(self, widget: QWidget) -> None:
        self._layout.addWidget(widget)

    def _set_label_text(self, text: str) -> None:
        self._label.setText(text)

    @abstractmethod
    def init(self) -> None:
        """
        Initialize the component (only for PyQt Component). 
        """
        raise NotImplementedError
