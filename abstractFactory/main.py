import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abstractFactory.PizzaStore import PizzaStore

amount_dict = {"double": 1.5, "normal": 1, "half": 0.5}

pizzaStore = PizzaStore()

pizzaA = pizzaStore.order("PizzaA", amount_dict["normal"], amount_dict["double"], amount_dict["half"])
pizzaB = pizzaStore.order("PizzaB", amount_dict["half"], amount_dict["double"], amount_dict["double"])
pizzaA.check()
pizzaB.check()
