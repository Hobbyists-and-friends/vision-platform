from abc import abstractmethod
from .IUIComponent import IUIComponent
from src.interfaces import IObserver


class IVariableRelatedComponent(IUIComponent, IObserver):
    pass
