from PyQt5.QtWidgets import (
    QLabel,
    QSizePolicy,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPixmap,
    QImage,
)

from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    NAME_KEY,
    VALUE_KEY,
)

from .ComponentBase import ComponentBase


class ImageDisplay(ComponentBase, QLabel):
    """
    The image display component from a variable. 
    """

    def __init__(self,
                 component_id: str):
        QLabel.__init__(self)
        ComponentBase.__init__(self, None, component_id)
        self.__variable_id = None
        self.setScaledContents(True)
        self.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

    def __repr__(self) -> str:
        return f'<ImageDisplay name={self.component_id} variable={self.__variable_id}/>'

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
