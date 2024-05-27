"""
Realisation of pattern "observer"

More info: https://refactoring.guru/ru/design-patterns/observer
"""

from abc import ABC, abstractmethod


class Publisher(ABC):
    """
    Public any new news or updates
    """

    __observers_list: list

    def __init__(self) -> None:
        self.__observers_list = list()

    def update(self, *args, **kwargs):
        """
        Send signal to all objects about new update
        """
        for observer in self.__observers_list:
            observer.update_by_publisher(*args, **kwargs)

    def add_observer(self, new_observer: 'Observer'):
        self.__observers_list.append(new_observer)

    def remove_observer(self, observer_to_remove: 'Observer'):
        self.__observers_list.remove(observer_to_remove)


class Observer(ABC):
    """
    Object which need to override update event
    """

    @abstractmethod
    def update_by_publisher(self, *args, **kwargs):
        pass
