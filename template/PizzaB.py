import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import register
from template.PizzaTemplate import PizzaTemplate
from template.Material import RiceFlourDough, BasilSource, CheeseTopping


class PizzaB(PizzaTemplate):

    @register(override)
    def add_dough(self, amount):
        """米粉生地。

        :param amount:量
        :return:
        """
        return RiceFlourDough(amount)

    @register(override)
    def add_source(self, amount):
        """バジルソース。

        :param amount:量
        :return:
        """
        return BasilSource(amount)

    @register(override)
    def add_topping(self, amount):
        """チーズトッピング。

        :param amount:量
        :return:
        """
        return CheeseTopping(amount)