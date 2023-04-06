from src.interfaces import (
    ISystem,
    IOperation,
    IPublisher,
    PyQtMetaClass,
    IObserver,
    IGUIComponent,
)
from src.utils import (
    PublisherBase,
)


class ComponentBase(PublisherBase, IGUIComponent, metaclass=PyQtMetaClass):
    def __init__(self,
                 system: 'ISystem',
                 component_id: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.system = system
        self.__component_id = component_id

    @property
    def component_id(self) -> str:
        return self.__component_id
