from copy import deepcopy

from src.constants import (
    VariableType,
    TYPE_KEY,
    NAME_KEY,
    VALUE_KEY,
    EMPTY_STRING,
)
from src.utils import PublisherBase
from src.interfaces import (
    IVariable,
    ISystem,
)


class Variable(PublisherBase, IVariable):
    """
    The Variable class is a data structure that stores a variable in this platform. 
    It is an concrete class of the combination IPublisher and IVariable.
    All operations is used for operating on this data.
    Each time the value of this variable is changed, it will notify all its subscribers.
    It's also can be assign to an UI component which will be updated when 
        the value of this variable is changed, vice versa.

    Attributes:
        system: ISystem
            The system that this variable belongs to.
        type: VariableType
            The type of this variable.
            E.x: VariableType.INTEGER, VariableType.STRING, VariableType.NULL
        data: dict
            The dicionary which stores all data (properties) of this variable.
            E.x: {'name': 'var1', 'value': 1, 'type': VariableType.INTEGER}
        variable_id: str
            The id which is used to identify this variable. Cannot have the same id with other variables.
    """

    def __init__(self, system: 'ISystem', **kwargs):
        super().__init__(**kwargs)
        self.system = system
        self.__handle_missing()
        self.__add_type()

    def __handle_missing(self) -> None:
        if NAME_KEY not in self._dict:
            self._dict[NAME_KEY] = EMPTY_STRING

        if VALUE_KEY not in self._dict:
            self._dict[VALUE_KEY] = None

    def __add_type(self) -> None:
        self._dict[TYPE_KEY] = VariableType.get_type_from_value(
            self._dict[VALUE_KEY])

    @property
    def type(self) -> VariableType:
        return self._dict[TYPE_KEY]

    @property
    def data(self) -> dict:
        return self._dict

    @property
    def variable_id(self) -> str:
        return self._dict[NAME_KEY]

    def change_value(self, **kwargs) -> None:
        """
        Change the value of this variable with the type checking.
        """
        if VALUE_KEY in kwargs.keys():
            if self.type == VariableType.NULL:
                self._dict.update(kwargs)
                self._dict[TYPE_KEY] = VariableType.get_type_from_value(
                    self._dict[VALUE_KEY])
                self.notify()

            if VariableType.get_type_from_value(kwargs[VALUE_KEY]) == self.type:
                self._dict.update(kwargs)
                self.notify()

    def __repr__(self) -> str:
        return f"<Variable {self.variable_id} value={self.data[VALUE_KEY]}>"
