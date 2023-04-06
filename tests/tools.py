from unittest.mock import PropertyMock

from src.constants import (
    VALUE_KEY,
    NAME_KEY,
)
from tests.constants import (
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_OPERATION_NAME,
    TEST_UI_COMPONENT_NAME,
)


def create_mocked_int_variable(variable):
    data = PropertyMock(return_value={
        VALUE_KEY: TEST_VARIABLE_VALUE,
        NAME_KEY: TEST_VARIABLE_NAME
    })
    type(variable).data = data

    variable_id = PropertyMock(return_value=TEST_VARIABLE_NAME)
    type(variable).variable_id = variable_id


def creat_mocked_operation(operation):
    operation_id = PropertyMock(return_value=TEST_OPERATION_NAME)
    type(operation).operation_id = operation_id


def create_mocked_ui_component(ui_component):
    component_id = PropertyMock(return_value=TEST_UI_COMPONENT_NAME)
    type(ui_component).component_id = component_id


def create_mocked_system(system, ui_component, application):
    type(system).application = PropertyMock(
        return_value=application)

    ui_components = PropertyMock(return_value={
        TEST_UI_COMPONENT_NAME: ui_component
    })
    type(system).ui_components = ui_components


def add_no_vars_system(system):
    variables = PropertyMock(return_value={})
    type(system).variables = variables


def add_vars_system(system, variable):
    variables = PropertyMock(return_value={
        TEST_VARIABLE_NAME: variable
    })

    type(system).variables = variables
