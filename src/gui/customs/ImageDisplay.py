from PyQt5.QtWidgets import (
    QLabel,
)
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
                 system: 'ISystem',
                 component_id: str,
                 variable_id: str):
        QLabel.__init__(self)
        ComponentBase.__init__(self, system, component_id)
        self.__variable_id = variable_id

    def __repr__(self) -> str:
        return f'<ImageDisplay name={self.component_id} variable={self.__variable_id}/>'

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        img_data = data[VALUE_KEY]

        image = QImage(
            img_data, img_data.shape[1], img_data.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.setPixmap(pixmap.scaled(self.size(), aspectRatioMode=True))
