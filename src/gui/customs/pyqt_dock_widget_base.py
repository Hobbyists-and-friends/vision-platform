from typing import (
    Callable,
    Any,
)
from abc import (
    abstractmethod,
)
from PyQt5.QtWidgets import (
    QDockWidget,
)
from PyQt5.QtCore import Qt
from src.cores import (
    System,
)
from src.utils.MultiObserverBase import MultiObserverBase
from src.interfaces.ui import (
    PyQtMetaClass,
    IUIComponent,
)
from src.operations.system_call import *


class PyQtDockWidgetBase(MultiObserverBase,
                         QDockWidget,
                         IUIComponent,
                         metaclass=PyQtMetaClass):
    def __init__(self, component_id: str, horizontal: bool = False) -> None:
        MultiObserverBase.__init__(
            self,
            observer_id=component_id,
            observer_class=AddVariableObserverOperation,
            change_value_class=ChangeVariableValueOperation,
            raise_error_class=RaiseErrorOperation,
        )
        QDockWidget.__init__(self, System.system.application.app)
        self.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)

    @ abstractmethod
    def init(self) -> None:
        raise NotImplementedError
