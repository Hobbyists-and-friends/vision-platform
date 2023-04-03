from src.interfaces import (
    ISystem,
    IOperation,
    IVariable,
)
from src.utils import PublisherBase
from src.cores import Variable
from src.constants import (
    VALUE_KEY,
    EMPTY_STRING,
    VARIABLES_KEY,
    OPERATION_KEY,
    APPLICATION_KEY,
)


class System(PublisherBase, ISystem):
    def __init__(self, **kwargs):
        PublisherBase.__init__(self, **kwargs)
        self.__error = Variable(
            system=self,
            **{
                VALUE_KEY: EMPTY_STRING,
            },
        )
        self.__variables = {}
        self.application = None
        self.__operations = {}

    @property
    def variables(self) -> dict:
        return self.__variables

    @property
    def error(self) -> 'IVariable':
        return self.__error

    def add_application(self, application):
        self.application = application

    def run_operation(self, operation: 'IOperation') -> None:
        operation.run(self, {
            OPERATION_KEY: self.__operations,
            VARIABLES_KEY: self.__variables,
            APPLICATION_KEY: self.application,
        })

    def add_variable(self, variable: 'IVariable'):
        self.__variables[variable.name] = variable

    def add_operation(self, operation: 'IOperation'):
        self.__operations[operation.operation_id] = operation
