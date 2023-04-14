from typing import (
    Dict,
)

from src.interfaces import (
    ISystem,
    IOperation,
    IVariable,
    IGUIComponent,
    IApplicationGUI,
    IObserver,
)
from src.utils import PublisherBase
from src.cores import Variable
from src.constants import (
    NAME_KEY,
    VALUE_KEY,
    EMPTY_STRING,
    VARIABLES_KEY,
    OPERATION_KEY,
    APPLICATION_KEY,
)


class System(PublisherBase, ISystem):
    """
    The System class is the core of this platform which will store all data, operations, application
        ui components, ...
    The System object will be passed to all other objects in this platform.

    Attributes:
        variables: dict
            The dictionary which stores all variables in this platform.

        error: IVariable
            The variable which stores the error message.

        ui_components: dict
            The dictionary which stores all ui components in this platform.

        operations: dict
            The dictionary which stores operations which are set up to be stored in this platform.
            Not all operation will be stored in the system.

        application: IApplication
            The application which is running in this platform.
    """

    def __init__(self, **kwargs):
        PublisherBase.__init__(self, **kwargs)
        self.__error = Variable(
            system=self,
            **{
                VALUE_KEY: EMPTY_STRING,
            },
        )
        self.__ui_components = {}
        self.__variables = {}
        self.application = None
        # self.__error = Variable()
        self.__operations = {}

    @property
    def variables(self) -> dict:
        return self.__variables

    @property
    def error(self) -> 'IVariable':
        return self.__error

    @property
    def ui_components(self) -> dict:
        return self.__ui_components

    @property
    def operations(self) -> dict:
        return self.__operations

    @property
    def observerable_components(self) -> Dict[str, 'IObserver']:
        return dict(
            **self.operations,
            **self.ui_components,
        )
