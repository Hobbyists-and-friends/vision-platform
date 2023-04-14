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

    @abstractmethod
    def add_variable(self, variable: 'IVariable') -> None:
        """
        Add a variable to this system.

        Args:
            variable: IVariable
                The variable which will be added to this system.
        """
        raise NotImplementedError

    @abstractmethod
    def add_application(self, application: 'IApplicationGUI') -> None:
        """
        Add an application to this system.

        Args:
            application: IApplicationGUI
                The application which will be added to this system.
        """
        raise NotImplementedError

    @abstractmethod
    def add_operation(self, operation: 'IOperation') -> None:
        """
        Add an operation to this system.

        Args:
            operation: IOperation
                The operation which will be added to this system.
        """
        raise NotImplementedError

    @abstractmethod
    def add_ui_component(self, ui_component: 'IGUIComponent') -> None:
        """
        Add a UI component to this system.

        Args:
            ui_component: IGUIComponent
                The UI component which will be added to this system.
        """
        raise NotImplementedError
