from abc import abstractmethod
from utils.abcd import ABCD

class Sorter(ABCD):
    @abstractmethod
    def sort(self, ll: list) -> list:
        pass