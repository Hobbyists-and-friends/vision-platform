from abc import abstractmethod, abstractproperty

from src.interfaces import (
    IPublisher,
)
from src.constants import (
    VariableType,
)


class IVariable(IPublisher):
    """
    The IVariable class is the interface for all variables in this platform which will
    be used to store data and notify all observers when the variables update their data.

    Attributes:
        type: VariableType
            The type of this variable.

        data: dict
            The data of this variable.

        variable_id: str
            The ID of this variable. 
    """

    @abstractproperty
    def type(self) -> VariableType:
        raise NotImplementedError

    @abstractproperty
    def data(self) -> dict:
        raise NotImplementedError

    @abstractproperty
    def variable_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def change_value(self, **kwargs) -> None:
        """
        Change the value of this variable with the type checking.
        """
        raise NotImplementedError
