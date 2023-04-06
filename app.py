import sys
from PyQt5.QtWidgets import QApplication

from src.gui import (
    ApplicationGUI,
)
from src.gui.customs import (
    IconButton,
)
from src.operations import (
    LoadLayoutOperation,
    CreateIconButtonOpeartion,
    AddGUIComponentOperation,
    LogVariableOperation,
    AddOperationObserverOperation,
    CreateVariableOperation,
)
# from src.gui.customs import (

# )
from src.cores import System


VARIABLE_NAME = 'Test 1'
VARIABLE_VALUE = 'Hello World'
BUTTON_NAME = 'Test Button'


def main():
    app = QApplication(sys.argv)
    system = System()
    operations = [
        LoadLayoutOperation(system, 'load_layout',
                            'src/assets/layouts/test_layout.ui'),
        CreateVariableOperation(
            system, 'create_variable 1', VARIABLE_NAME, VARIABLE_VALUE),
        CreateIconButtonOpeartion(system, 'create_icon_button',
                                  BUTTON_NAME),
        AddGUIComponentOperation(system, 'add button',
                                 BUTTON_NAME, 'test_layout'),
        LogVariableOperation(system, 'log_variable',
                             VARIABLE_NAME, store=True),
        AddOperationObserverOperation(
            system, 'add_observer', 'log_variable', BUTTON_NAME),
    ]
    win = ApplicationGUI(system)
    win.load_layout('src/assets/layouts/home_screen_layout.ui')
    system.add_application(win)

    for operation in operations:
        operation.run()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
