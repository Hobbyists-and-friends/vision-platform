import sys
from PyQt5.QtWidgets import QApplication

from src.gui import (
    ApplicationGUI,
)
from src.gui.customs import (
    IconButton,
)
# from src.gui.customs import (

# )
from src.cores import System


def main():
    app = QApplication(sys.argv)
    system = System()
    win = ApplicationGUI(system)
    win.load_layout('src/assets/layouts/test_layout.ui')
    win.add_component(IconButton('Test 1', system=system), 'test_layout')
    win.add_component(IconButton('Test 2', system=system), 'test_layout')
    win.add_component(IconButton('Test 3', system=system), 'test_layout')
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
