import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abc import abstractmethod
from abstractFactory.Pizza import Pizza
from utils.abcd import ABCD

class AbstractPizzaFactory(ABCD):
    def __init__(self, factory):
        self.factory = factory

    def make_pizza(self, dough_amount=1, source_amount=1, topping_amount=1):
        pizza = Pizza()
        pizza.materials.append(self.factory.add_dough(dough_amount))
        pizza.materials.append(self.factory.add_source(source_amount))
        pizza.materials.append(self.factory.add_topping(topping_amount))
        return pizza

    @abstractmethod
    def add_dough(self, amount):
        pass

    @abstractmethod
    def add_source(self, amount):
        pass

    @abstractmethod
    def add_topping(self, amount):
        pass



