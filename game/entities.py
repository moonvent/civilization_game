from enum import IntEnum
from typing import Callable
from pydantic import BaseModel, Field, conint
import random


class Race(IntEnum):
    White = 1
    Yellow = 2
    Black = 3


class HairColor(IntEnum):
    Black = 1
    Blond = 2
    Brown = 3
    Red = 4


type UsualParametrRange = conint(ge=0, le=100)
type PositiveInteger = conint(ge=0)


DEFAULT_ZERO_FIELD = Field(default=0)
DEFAULT_HALF_FIELD = Field(default=50)


class Mood(BaseModel):
    happiness: UsualParametrRange = DEFAULT_HALF_FIELD
    pro_political: UsualParametrRange = DEFAULT_HALF_FIELD
    oppositional: UsualParametrRange = DEFAULT_HALF_FIELD
    political_activity: UsualParametrRange = DEFAULT_HALF_FIELD


class Education(BaseModel):
    political: UsualParametrRange = DEFAULT_HALF_FIELD
    information_technology_literacy: UsualParametrRange = DEFAULT_HALF_FIELD
    economical: UsualParametrRange = DEFAULT_HALF_FIELD
    literacy: UsualParametrRange = DEFAULT_HALF_FIELD


class PhysicalCulture(BaseModel):
    healthy_lifestyle: UsualParametrRange = DEFAULT_ZERO_FIELD
    health_status: UsualParametrRange = DEFAULT_ZERO_FIELD
    warrior_ability: UsualParametrRange = DEFAULT_ZERO_FIELD


class Person(BaseModel):
    age: int = Field(default=18)
    race: Race = Field(default_factory=lambda x: random.choice(tuple(Race)))
    hair_color: HairColor = Field(
        default_factory=lambda x: random.choice(tuple(HairColor))
    )
    mood: Mood = Field(default_factory=Mood)
    education: Education = Field(default_factory=Education)
    physical_culture: PhysicalCulture = Field(default_factory=PhysicalCulture)


class Perk:
    community: 'Community'
    title: str

    def mixin(self):
        raise NotImplementedError


class PreciousMetals(BaseModel):
    gold: PositiveInteger = DEFAULT_ZERO_FIELD
    platinum: PositiveInteger = DEFAULT_ZERO_FIELD


class PreciousStones(BaseModel):
    diamond: PositiveInteger = DEFAULT_ZERO_FIELD
    ruby: PositiveInteger = DEFAULT_ZERO_FIELD
    emerald: PositiveInteger = DEFAULT_ZERO_FIELD


class Currencies(BaseModel):
    money: PositiveInteger = DEFAULT_ZERO_FIELD
    oil: PositiveInteger = DEFAULT_ZERO_FIELD
    gas: PositiveInteger = DEFAULT_ZERO_FIELD
    precious_stones: PreciousStones = Field(default=PreciousStones())
    precious_metals: PreciousMetals = Field(default=PreciousMetals())


class Structure(BaseModel):
    title: str

    def mixin(self):
        raise NotImplementedError


class Community(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    people_amount: Callable = None
    general_mood: Mood = Field(default=Mood())
    general_education: Education = Field(default=Education())
    general_physical_culture: PhysicalCulture = Field(default=PhysicalCulture())
    skills: list[Perk] = Field(default=list())
    people: list[Person] = Field(default=list())
    structures: list[Structure] = Field(default=list())
    currencies: Currencies = Field(default=Currencies())
