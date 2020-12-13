import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abstractFactory.AbstractPizzaFactory import AbstractPizzaFactory
from utils.abcd import override
from utils.register import regist
from abstractFactory.Material import RiceFlourDough, BasilSource, CheeseTopping


class PizzaFactoryB(AbstractPizzaFactory):
    def __init__(self):
        super().__init__(self)

    @regist(override)
    def add_dough(self, amount):
        return RiceFlourDough(amount)

    @regist(override)
    def add_source(self, amount):
        return BasilSource(amount)

    @regist(override)
    def add_topping(self, amount):
        return CheeseTopping(amount)
