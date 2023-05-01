from src.interfaces import (
    ISystem,
    IOperation,
    IPublisher,
    IObserver,
    IGUIComponent,
)
from src.interfaces.ui import (
    PyQtMetaClass,
)
from src.utils import (
    PublisherBase,
)
from src.operations.system_call import *
from src.utils.MultiObserverBase import MultiObserverBase


class ComponentBase(PublisherBase,
                    MultiObserverBase,
                    IGUIComponent,
                    metaclass=PyQtMetaClass):
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
        MultiObserverBase.__init__(self, observer_id=component_id,
                                   observer_class=AddVariableObserverOperation,
                                   change_value_class=ChangeVariableValueOperation,
                                   raise_error_class=RaiseErrorOperation)
        self.system = system
        self.__component_id = component_id

    @ property
    def component_id(self) -> str:
        return self.__component_id

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> dict:
        return {}
