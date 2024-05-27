from game.entities import Person
from game.services.aliases import Alias
from game.services.constants import ConstantPerkAttribute


class PersonService:
    def perk__start_community(self) -> Alias.PersonList:
        result = [
            Person() for _ in range(ConstantPerkAttribute.StartCommunityPeopleAmount)
        ]
        return result
