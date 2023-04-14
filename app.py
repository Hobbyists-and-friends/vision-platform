import sys
from PyQt5.QtWidgets import QApplication

from src.gui import (
    ApplicationGUI,
)
from src.gui.customs import (
    IconButton,
    ImageDisplay,
)
from src.operations import (
    LoadLayoutOperation,
    CreateIconButtonOpeartion,
    AddGUIComponentOperation,
    LogVariableOperation,
    AddOperationObserverOperation,
    CreateVariableOperation,
    AddVariableObserverOperation,
)
# from src.gui.customs import (

# )
from src.cores import System


# The code below is used for testing purpose only.
import cv2 as cv
# The code above is used for testing purpose only.


VARIABLE_NAME = 'Test 1'
VARIABLE_VALUE = 'Hello World'
BUTTON_NAME = 'Test Button'


def main():
    app = QApplication(sys.argv)
    system = System()

    # Load the test image
    image = cv.imread('src/assets/images/test_image.jpg')
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    system.ui_components["Test Image Display Component"] = ImageDisplay(
        system,
        "Test Image Display Component",
        "Test Image"
    )

    operations = [
        LoadLayoutOperation(
            system,
            operation_id='load_layout',
            layout_name='src/assets/layouts/test_layout.ui'),
        CreateVariableOperation(
            system,
            operation_id='create_variable 2',
            variable_name="Test Image",
            variable_value=image),
        CreateVariableOperation(
            system,
            operation_id='create_variable 1',
            variable_name=VARIABLE_NAME,
            variable_value=VARIABLE_VALUE),
        CreateIconButtonOpeartion(
            system,
            operation_id='create_icon_button',
            component_id=BUTTON_NAME,
            text=BUTTON_NAME),
        AddGUIComponentOperation(
            system,
            operation_id='add image',
            component_id='Test Image Display Component',
            layout='test_layout'),
        AddGUIComponentOperation(
            system,
            operation_id='add button',
            component_id=BUTTON_NAME,
            layout='test_layout'),
        LogVariableOperation(
            system,
            operation_id='log_variable',
            variable_id=VARIABLE_NAME,
            store=True),
        AddOperationObserverOperation(
            system,
            operation_id='add_observer',
            observer_operation_id='log_variable',
            observer_ui_component_id=BUTTON_NAME),
        AddVariableObserverOperation(
            system,
            operation_id='add_variable_operation',
            variable_id='Test Image',
            observer_id='Test Image Display Component'),
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
