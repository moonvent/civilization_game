"""
Realisation of pattern "observer"

More info: https://refactoring.guru/ru/design-patterns/observer
"""

from abc import ABC, abstractmethod

from game.services.aliases import Alias


class Publisher(ABC):
    """
    Public any new news or updates
    """

    _observers_list: list

    def __init__(self) -> None:
        self._observers_list = list()

    def update(self, data: Alias.WidgetUpdateData):
        """
        Send signal to all objects about new update
        """
        for observer in self._observers_list:
            observer.update_by_publisher(data=data)

    def add_observer(self, new_observer: 'Observer'):
        self._observers_list.append(new_observer)

    def remove_observer(self, observer_to_remove: 'Observer'):
        self._observers_list.remove(observer_to_remove)


class Observer:
    """
    Object which need to override update event
    """

    @abstractmethod
    def update_by_publisher(self, data: Alias.WidgetUpdateData):
        pass
