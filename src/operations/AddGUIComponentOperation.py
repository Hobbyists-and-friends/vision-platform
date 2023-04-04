from src.interfaces import (
    ISystem,
    IOperation,
    IVariable,
    IGUIComponent,
    IPublisher,
)


class AddGUIComponentOperation(IOperation):
    def __init__(self, system: 'ISystem',
                 component_id: str,
                 layout: str) -> None:
        self.system = system
        self.__component_id = component_id
        self.__layout = layout

    @property
    def operation_id(self) -> str:
        return self.__component_id

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def run(self, publisher: 'IPublisher' = None, data: dict = None) -> None:
        self.system.application.add_component(
            self.system.ui_components[self.__component_id], self.__layout)

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
