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
)


class Variable(PublisherBase, IVariable):
    def __init__(self, system, **kwargs):
        super().__init__(**kwargs)
        self.system = system
        self.__handle_missing()
        self.__add_type()

    def __handle_missing(self):
        if NAME_KEY not in self._dict:
            self._dict[NAME_KEY] = EMPTY_STRING

        if VALUE_KEY not in self._dict:
            self._dict[VALUE_KEY] = None

    def __add_type(self):
        self._dict[TYPE_KEY] = VariableType.get_type_from_value(
            self._dict[VALUE_KEY])

    @property
    def type(self):
        return self._dict[TYPE_KEY]

    @property
    def data(self):
        return deepcopy(self._dict)

    @property
    def variable_id(self):
        return self._dict[NAME_KEY]

    def change_value(self, **kwargs):
        if VALUE_KEY in kwargs.keys():
            if self.type == VariableType.NULL:
                self._dict.update(kwargs)
                self._dict[TYPE_KEY] = VariableType.get_type_from_value(
                    self._dict[VALUE_KEY])
                self.notify()

            if VariableType.get_type_from_value(kwargs[VALUE_KEY]) == self.type:
                self._dict.update(kwargs)
                self.notify()
