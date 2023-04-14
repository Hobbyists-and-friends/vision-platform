from abc import abstractmethod, abstractproperty
from typing import (
    Dict,
)


from src.interfaces import (
    IPublisher,
    IOperation,
    IVariable,
    IApplicationGUI,
    IGUIComponent,
    IObserver,
)


class ISystem(IPublisher):
    """
    The ISystem class is the interface for the system in this platform which will
    manage all variables, applications, operations and UI components. 

    Attributes:
        variables: dict
            The variables which are managed by this system.

        error: IVariable
            The error variable which is managed by this system.

        applications: list
            The applications which are managed by this system.

        operations: list
            The operations which are managed by this system.

        ui_components: list
            The UI components which are managed by this system.
    """
    @abstractproperty
    def variables(self) -> Dict[str, 'IVariable']:
        raise NotImplementedError

    @abstractproperty
    def error(self) -> 'IVariable':
        raise NotImplementedError

    @abstractproperty
    def ui_components(self) -> Dict[str, 'IGUIComponent']:
        raise NotImplementedError

    @abstractproperty
    def operations(self) -> Dict[str, 'IOperation']:
        raise NotImplementedError

    @abstractproperty
    def observerable_components(self) -> Dict[str, 'IObserver']:
        raise NotImplementedError
