from PyQt5.QtWidgets import (
    QLabel,
    QSizePolicy,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPixmap,
    QImage,
)

from src.cores import System
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


class PyQtImageDisplay(PyQtComponentBase, QLabel,
                       IVariableRelatedComponent, metaclass=PyQtMetaClass):
    """
    The image display component from a variable. 
    """

    def __init__(self,
                 component_id: str):
        QLabel.__init__(self)
        self.__component_id = component_id

    def init(self) -> None:
        self.setScaledContents(True)
        self.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

    def __repr__(self) -> str:
        return f'<ImageDisplay name={self.__component_id}/>'

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        if data[VALUE_KEY] is not None:
            img_data = data[VALUE_KEY]

            if len(img_data.shape) == 2:
                format = QImage.Format_Grayscale8
            else:
                format = QImage.Format_RGB888

            image = QImage(
                img_data, img_data.shape[1], img_data.shape[0], format)
            pixmap = QPixmap.fromImage(image)
            self.setPixmap(pixmap.scaled(
                self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def set_variable(self, variable_id: str) -> None:
        AddVariableObserverOperation(
            variable_id=variable_id,
            observer_id=self.__component_id,
        ).run()

    def on_update(self) -> None:
        pass
