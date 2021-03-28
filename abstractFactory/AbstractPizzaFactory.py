import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod
from abstractFactory.Pizza import Pizza
from utils.abcd import ABCD

class AbstractPizzaFactory(ABCD):
    def __init__(self, factory: "AbstractPizzaFactory"):
        self.factory: AbstractPizzaFactory = factory

    def make_pizza(self, dough_amount: float=1, source_amount: float=1, topping_amount: float=1):
        pizza: Pizza = Pizza()
        pizza.materials.append(self.factory.add_dough(dough_amount))
        pizza.materials.append(self.factory.add_source(source_amount))
        pizza.materials.append(self.factory.add_topping(topping_amount))
        return pizza

    @abstractmethod
    def add_dough(self, amount: float):
        pass

    @abstractmethod
    def add_source(self, amount: float):
        pass

    @abstractmethod
    def add_topping(self, amount: float):
        pass



