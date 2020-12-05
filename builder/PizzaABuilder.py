import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from builder.Pizza import Pizza
from builder.Material import *
from builder.PizzaBuilder import PizzaBuilder
from utils.abcd import override
from utils.register import register


class PizzaABuilder(PizzaBuilder):

    @register(override)
    def add_dough(self, amount: float):
        self.__pizza__.materials.append(WheatDough(amount))
        return self

    @register(override)
    def add_source(self, amount: float):
        self.__pizza__.materials.append(TomatoSource(amount))
        return self

    @register(override)
    def add_topping(self, amount: float):
        self.__pizza__.materials.append(CoanTopping(amount))
        return self
