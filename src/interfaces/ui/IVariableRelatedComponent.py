from abc import abstractmethod
from .IUIComponent import IUIComponent
from src.interfaces import IObserver


class IVariableRelatedComponent(IUIComponent, IObserver):
    @abstractmethod
    def set_variable(self, variable_id: str) -> None:
        """
        Set the variable which is related to this component (1-way binding or 2-way binding).

        Args:
            variable_id: str
                The id of the variable which will be displayed.
        """
        raise NotImplementedError
