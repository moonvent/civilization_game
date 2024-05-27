from dataclasses import dataclass


@dataclass(frozen=True)
class ConstantPerkAttribute:
    StartCommunityPeopleAmount = 10


@dataclass(frozen=True)
class UILabelAttribute:
    StartCommunityPerkLabelName = 'Новое комьюнити'
