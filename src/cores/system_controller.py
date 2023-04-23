from src.interfaces import (
    ISystem,
)
from src.interfaces.ui import (
    IWindow,
)
from src.interfaces.operation import (
    ISystemCall,
)


class SystemController:
    def __init__(self, system: 'ISystem', window: 'IWindow') -> None:
        self.system = system
        self.window = window

    def dispatch_operation(self, operation: 'ISystemCall') -> None:
        operation.run()