from abc import abstractmethod, abstractproperty

from src.interfaces import IPublisher


class IVariable(IPublisher):
    @abstractproperty
    def type(self):
        pass

    @abstractproperty
    def data(self):
        pass

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def change_value(self, **kwargs):
        pass
