from dataclasses import dataclass

from game.entities import Person


@dataclass(frozen=True)
class Alias:
    PersonList = list[Person]
