import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abstractFactory.AbstractPizzaFactory import AbstractPizzaFactory
from utils.abcd import override
from utils.register import register
from abstractFactory.Material import WheatDough, TomatoSource, CoanTopping


class PizzaFactoryA(AbstractPizzaFactory):
    def __init__(self):
        super().__init__(self)

    @register(override)
    def add_dough(self, amount):
        return WheatDough(amount)

    @register(override)
    def add_source(self, amount):
        return TomatoSource(amount)

    @register(override)
    def add_topping(self, amount):
        return CoanTopping(amount)