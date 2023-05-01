from src.interfaces.ui import (
    IVariableRelatedComponent,
    PyQtMetaClass,
)

from .pyqt_component_base import PyQtComponentBase


class PyQtComponentRelatedVariable(PyQtComponentBase, IVariableRelatedComponent):
    def __init__(self, horizontal=False) -> None:
        super().__init__(horizontal)

        self._src_params = {}
        self._res_params = {}
