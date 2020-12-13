import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from builder.Pizza import Pizza
from builder.Material import *
from builder.PizzaBuilder import PizzaBuilder
from utils.abcd import override
from utils.register import registToMethod


class PizzaBBuilder(PizzaBuilder):
    @registToMethod(override)
    def add_dough(self, amount: float):
        self.__pizza__.materials.append(RiceFlourDough(amount))
        return self

    @registToMethod(override)
    def add_source(self, amount: float):
        self.__pizza__.materials.append(BasilSource(amount))
        return self

    @registToMethod(override)
    def add_topping(self, amount: float):
        self.__pizza__.materials.append(CheeseTopping(amount))
        return self