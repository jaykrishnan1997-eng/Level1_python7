from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        f = Flameling("Flameling", "Fire")
        return f

    def create_evolved(self) -> Pyrodon:
        p = Pyrodon("Pyrodon", "Fire/Flying")
        return p


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        a = Aquabub("Aquabub", "Water")
        return a

    def create_evolved(self) -> Torragon:
        t = Torragon("Torragon", "Water")
        return t
