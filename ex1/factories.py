from ex0.factories import CreatureFactory
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        s = Sproutling("Sproutling", "Grass")
        return s

    def create_evolved(self) -> Bloomelle:
        b = Bloomelle("Bloomelle", "Grass/Fairy")
        return b


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        s = Shiftling("Shiftling", "Normal")
        return s

    def create_evolved(self) -> Morphagon:
        m = Morphagon("Morphagon", "Normal/Dragon")
        return m
