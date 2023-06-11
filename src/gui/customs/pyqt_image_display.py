from PyQt5.QtWidgets import (
    QLabel,
    QSizePolicy,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPixmap,
    QImage,
)

from src.cores import System
from src.constants import *
from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    NAME_KEY,
    VALUE_KEY,
)
from src.interfaces.ui import (
    IVariableRelatedComponent,
    PyQtMetaClass,
)
from src.operations.system_call import AddVariableObserverOperation

from .pyqt_component_base import PyQtComponentBase


class PyQtImageDisplay(
    PyQtComponentBase, IVariableRelatedComponent, metaclass=PyQtMetaClass
):
    """
    The image display component from a variable.
    """

    def __init__(self, component_id: str):
        PyQtComponentBase.__init__(self, component_id)

        self.__img_label = QLabel()
        self._add_widget(self.__img_label)

        self.__component_id = component_id

    def init(self) -> None:
        self.__img_label.setScaledContents(True)
        self.__img_label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

    def __repr__(self) -> str:
        return f"<ImageDisplay name={self.__component_id}/>"

    def update(self, publisher: "IPublisher", data: dict) -> None:
        img_data = self._get_params_value(SRC_VARIABLE)

        if img_data is not None:
            if len(img_data.shape) == 2:
                format = QImage.Format_Grayscale8
            else:
                format = QImage.Format_RGB888

            image = QImage(img_data, img_data.shape[1], img_data.shape[0], format)
            pixmap = QPixmap.fromImage(image)
            self.__img_label.setPixmap(
                pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )

    def on_update(self) -> None:
        pass

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> dict:
        return {}
