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
)
# from src.gui.customs import (

# )
from src.cores import System


def main():
    app = QApplication(sys.argv)
    system = System()
    operations = [
        LoadLayoutOperation(system, 'load_layout',
                            'src/assets/layouts/test_layout.ui')
    ]
    win = ApplicationGUI(system)
    win.load_layout('src/assets/layouts/home_screen_layout.ui')
    system.add_application(win)

    # for operation in operations:
    #     system.run_operation(operation)

    win.add_component(IconButton('Test 1', system=system), 'test_layout')
    win.add_component(IconButton('Test 2', system=system), 'test_layout')
    win.add_component(IconButton('Test 3', system=system), 'test_layout')
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
