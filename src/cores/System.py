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
)


class System(PublisherBase, ISystem):
    def __init__(self, **kwargs):
        PublisherBase.__init__(self, **kwargs)
        self.__error = Variable(
            system=self,
            **{
                VALUE_KEY: '',
            },
        )
        self.__variables = {}

    @property
    def variables(self) -> dict:
        return self.__variables

    @property
    def error(self) -> 'IVariable':
        return self.__error

    def run_operation(self, operation: 'IOperation'):
        pass
