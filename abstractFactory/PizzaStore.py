import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abstractFactory.PizzaFactoryA import PizzaFactoryA
from abstractFactory.PizzaFactoryB import PizzaFactoryB
from abstractFactory.AbstractPizzaFactory import AbstractPizzaFactory
from typing import Dict

class PizzaStore:
    def __init__(self):
        self.factorys: Dict[str, AbstractPizzaFactory] = {}
        self.factorys["PizzaA"] = PizzaFactoryA()
        self.factorys["PizzaB"] = PizzaFactoryB()

    def order(self, pizza_type: str, dough_amount: float=1, source_amount: float=1, topping_amount: float=1):
        if pizza_type in self.factorys:
            return self.factorys[pizza_type].make_pizza(dough_amount, source_amount, topping_amount)
        else:
            raise Exception("no such pizza")
