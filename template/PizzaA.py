import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import registToMethod
from template.PizzaTemplate import PizzaTemplate
from template.Material import WheatDough, TomatoSource, CoanTopping


class PizzaA(PizzaTemplate):

    @registToMethod(override)
    def add_dough(self, amount):
        """小麦生地。

        :param amount: 量
        :return:
        """
        return WheatDough(amount)

    @registToMethod(override)
    def add_source(self, amount):
        """トマトソース。

        :param amount: 量
        :return:
        """
        return TomatoSource(amount)

    @registToMethod(override)
    def add_topping(self, amount):
        """コーントッピング

        :param amount: 量
        :return:
        """
        return CoanTopping(amount)