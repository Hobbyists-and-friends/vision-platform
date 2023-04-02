import sys
from PyQt5.QtWidgets import QApplication

from src.gui import ApplicationGUI
from src.cores import System


def main():
    app = QApplication(sys.argv)
    system = System()
    win = ApplicationGUI(system)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
