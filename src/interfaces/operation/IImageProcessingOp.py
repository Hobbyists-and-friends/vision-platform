from abc import (
    abstractmethod,
)

from src.interfaces.operation import (
    IObserverOp,
)


class IImageProcessingOp(IObserverOp):
    """
    The Image Processing interface for the image processing operations (convert image to gray,
    finding object, ...).
    """

    @abstractmethod
    def update_parameter_var(self, variable_id: str, value: str) -> None:
        """
        Update the parameter variable.

        Args:
            variable_id: str
                The id of the variable which is updated.
            value: str
                The value of the variable.
        """
        raise NotImplementedError

    @abstractmethod
    def set_parameter_var(self, parameter_id: str, variable_id: str) -> None:
        """
        Set the variable for the specific parameters.

        Args:
            parameter_id: str
                The id of the parameter, which is used in this operation.
            variable_id: str
                The id of the variable which is stored in the system, the value of this variable 
                will be used for this operation.
        """
