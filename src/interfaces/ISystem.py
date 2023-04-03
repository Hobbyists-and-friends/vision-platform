from abc import abstractmethod, abstractproperty


from src.interfaces import (
    IPublisher,
    IOperation,
    IVariable,
    IApplicationGUI,
)


class ISystem(IPublisher):
    @abstractproperty
    def variables(self) -> dict:
        raise NotImplementedError

    @abstractproperty
    def error(self) -> 'IVariable':
        raise NotImplementedError

    @abstractmethod
    def run_operation(self, operation: 'IOperation'):
        raise NotImplementedError

    @abstractmethod
    def add_variable(self, variable: 'IVariable'):
        raise NotImplementedError

    @abstractmethod
    def add_application(self, application: 'IApplicationGUI'):
        raise NotImplementedError

    @abstractmethod
    def add_operation(self, operation: 'IOperation'):
        raise NotImplementedError
