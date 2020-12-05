import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abc import abstractmethod
from builder.Pizza import Pizza
from builder.Material import *
from utils.abcd import ABCD

class PizzaBuilder(ABCD):
    def __init__(self):
        self.__pizza__ = Pizza()

    @abstractmethod
    def add_dough(self, amount: float):
        pass

    @abstractmethod
    def add_source(self, amount: float):
        pass

    @abstractmethod
    def add_topping(self, amount: float):
        pass

    def build(self):
        return self.__pizza__
