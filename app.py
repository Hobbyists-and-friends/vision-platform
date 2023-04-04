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
)
# from src.gui.customs import (

# )
from src.cores import System


def main():
    app = QApplication(sys.argv)
    system = System()
    operations = [
        LoadLayoutOperation(system, 'load_layout',
                            'src/assets/layouts/test_layout.ui'),
        CreateIconButtonOpeartion(system, 'create_icon_button',
                                  'Test 1'),
        AddGUIComponentOperation(system, 'Test 1', 'test_layout')
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
