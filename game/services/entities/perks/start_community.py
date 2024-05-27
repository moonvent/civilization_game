from typing import override
from game.entities import Perk, Community
from game.services.aliases import Alias
from game.services.constants import UILabelAttribute
from game.services.entities.person import PersonService


class StartCommunityPerk(Perk):
    title = 'Старт комьюнити'

    def __init__(self, community: Community):
        self.community = community

    @override
    def apply_perk(self):
        person_service = PersonService()
        people = person_service.perk__start_community()

        self.community.people = people
        self.community.people_amount = people.__len__

        self.community.update(
            data=Alias.WidgetUpdateData(
                widget_title=UILabelAttribute.StartCommunityPerkLabelName,
                value=self.community.people_amount(),
            )
        )
