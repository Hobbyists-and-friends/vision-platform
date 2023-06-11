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
from src.interfaces import IPublisher
from src.operations.system_call import *
from src.utils.MultiObserverBase import MultiObserverBase


class PyQtComponentBase(
    MultiObserverBase, IUIComponent, QWidget, metaclass=PyQtMetaClass
):
    def __init__(self, component_id: str, horizontal=False) -> None:
        MultiObserverBase.__init__(
            self,
            observer_id=component_id,
            observer_class=AddVariableObserverOperation,
            change_value_class=ChangeVariableValueOperation,
            raise_error_class=RaiseErrorOperation,
        )
        QWidget.__init__(self)

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
