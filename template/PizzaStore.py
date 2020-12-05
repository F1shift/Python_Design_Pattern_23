import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from template.PizzaTemplate import PizzaTemplate
from template.PizzaA import PizzaA
from template.PizzaB import PizzaB
from typing import Dict, Type


class PizzaStore:
    def __init__(self):
        self.pizza_menu: Dict[str, Type[PizzaTemplate]] = {}
        self.pizza_menu["PizzaA"] = PizzaA
        self.pizza_menu["PizzaB"] = PizzaB

    def order(self, pizza_type, dough_amount=1, source_amount=1, topping_amount=1):
        if pizza_type in self.pizza_menu:
            return self.pizza_menu[pizza_type](dough_amount, source_amount, topping_amount)
        else:
            raise Exception("no such pizza")
