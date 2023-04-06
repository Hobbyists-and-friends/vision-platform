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
    """
    The ComponentBase class is the base class for all ui components in this platform.
    It's inherited from the PublisherBase class which is the base class for all publishers in this platform.

    Attributes:
        system: ISystem
            The system object which is passed to all objects in this platform.
        component_id: str
            The identifier of this component, there. 
    """

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
