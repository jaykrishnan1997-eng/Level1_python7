from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    def __init__(self):
        self._transformed = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass
