from abc import abstractmethod, abstractproperty


from src.interfaces import (
    IPublisher,
    IOperation,
    IVariable,
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
