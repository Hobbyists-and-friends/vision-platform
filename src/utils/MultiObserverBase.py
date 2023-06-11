from typing import (
    Callable,
)
from abc import (
    ABC,
    abstractmethod,
    abstractproperty,
)
from src.cores import (
    System,
)
from src.constants import *


class MultiObserverBase(ABC):
    def __init__(
        self,
        observer_id: str,
        observer_class: Callable,
        change_value_class: Callable,
        raise_error_class: Callable,
    ) -> None:
        self._params = {}
        self.src_params = {}
        self.__observer_id = observer_id
        self.__observer_class = observer_class
        self.__change_value_class = change_value_class
        self.__raise_error_class = raise_error_class

    def set_src_variable(self, param_key: str, variable_id: str) -> None:
        if self._verify_variable(param_key, variable_id):
            self._params[param_key] = variable_id
            self.src_params[param_key] = variable_id

            if param_key in self.default_params:
                self.__change_value_class(
                    variable_id=variable_id, new_value=self.default_params[param_key]
                ).run()
        else:
            self.__raise_error_class(
                error_message=f"Variable {variable_id} is not valid for {param_key}"
            ).run()

    def set_res_variable(self, param_key: str, variable_id: str) -> None:
        if self._verify_variable(param_key, variable_id):
            self._params[param_key] = variable_id

    def observer_all_src(self) -> None:
        for variable_id in self.src_params.values():
            self.__observer_class(
                variable_id=variable_id, observer_id=self.__observer_id, update=True
            ).run()

    @abstractmethod
    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        raise NotImplementedError

    def _get_params_value(self, param_key: str) -> object:
        if param_key in self._params:
            result = System.system.variables[self._params[param_key]].data[VALUE_KEY]
            return result
        else:
            return self.default_params[param_key]

    @abstractproperty
    def default_params(self) -> dict:
        raise NotImplementedError

    @property
    def params(self) -> dict:
        return self._params
