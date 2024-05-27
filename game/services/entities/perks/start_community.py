from game.entities import Perk, Community
from game.services.entities.person import PersonService


class StartCommunityPerk(Perk):
    title = 'Старт комьюнити'

    def __init__(self, community: Community):
        self.community = community

    def mixin(self):
        person_service = PersonService()
        people = person_service.perk__start_community()

        self.community.people = people
        self.community.people_amount = people.__len__
