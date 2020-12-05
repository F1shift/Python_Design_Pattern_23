import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from builder.PizzaABuilder import PizzaABuilder
from builder.PizzaBBuilder import PizzaBBuilder

pizza_A = PizzaABuilder().add_dough(1).add_source(1.5).add_topping(0.7).build()
pizza_B = PizzaBBuilder().add_dough(1.3).add_source(1).add_topping(1.5).build()

pizza_A.check()
pizza_B.check()
