from abc import abstractmethod
from utils.abcd import ABCD
from typing import Any


class Cloneable(ABCD):
    @abstractmethod
    def clone(self) -> Any:
        pass