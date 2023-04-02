from abc import abstractmethod, ABC

from src.interfaces import (
    IObserver,
    IApplicationGUI,
)


class IGUIComponent(IObserver):
    pass
