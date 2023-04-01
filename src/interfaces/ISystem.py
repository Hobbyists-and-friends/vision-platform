from abc import abstractmethod, ABC


from src.interfaces import (
    IPublisher, 
    IOperation,
)


class ISystem(IPublisher):
    @abstractmethod
    def run_operation(self, operation: 'IOperation'):
        raise NotImplementedError
