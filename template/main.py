import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from template.PizzaStore import PizzaStore

pizzaStore = PizzaStore()

pizzaA = pizzaStore.order("PizzaA", 1, 1, 1)
pizzaB = pizzaStore.order("PizzaB", 0.5, 1, 1.2)
pizzaA.check()
pizzaB.check()
