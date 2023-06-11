from random import random
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QDockWidget,
    QLabel,
)
from src.interfaces.ui import (
    PyQtMetaClass,
    IVariableRelatedComponent,
)
from src.interfaces import IPublisher

from src.cores import *
from src.constants import *
from src.utils.Logging import Logging

from .pyqt_component_base import PyQtComponentBase
from .pyqt_dock_widget_base import PyQtDockWidgetBase


class PyQtComponentList(
    PyQtDockWidgetBase, QDockWidget, IVariableRelatedComponent, metaclass=PyQtMetaClass
):
    def __init__(
        self, component_id: str, horizontal=False, add_component_class=None, **kwargs
    ) -> None:
        super().__init__(component_id, horizontal)
        self.__kwargs = kwargs
        self.__add_component_class = add_component_class
        self.__layout_name = f"{component_id}_layout"

        self._widget = QWidget()

        self.__main_layout = QVBoxLayout()
        self.__main_layout.setObjectName(self.__layout_name)
        self._widget.setLayout(self.__main_layout)
        self.setWidget(self._widget)
        self.__components = None

    def init(self) -> None:
        pass

    def update(self, publisher: "IPublisher", data: dict) -> None:
        component_names = self._get_params_value(SRC_VARIABLE)

        if component_names is not None:
            self._clear_layout()

            if self.__add_component_class is not None:
                for component_name in component_names:
                    # self.__add_component_class(
                    #     component_id=component_name,
                    #     layout=self.__layout_name,
                    # ).run()
                    component = System.system.ui_components[component_name]
                    self.__main_layout.addWidget(component)
                    component.init()
                    component.show()

            self.__components = component_names

    def _clear_layout(self):
        if self.__components is not None:
            Logging.debug(msg="Remove all widget")
            for component_name in self.__components:
                component = System.system.ui_components[component_name]
                self.__main_layout.removeWidget(component)
                component.hide()

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> dict:
        return {}

    def on_update(self) -> None:
        pass
