import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod
from utils.abcd import ABCD


class PizzaTemplate(ABCD):
    def __init__(self, dough_amount=1, source_amount=1, topping_amount=1):
        self.materials = []
        self.materials.append(self.add_dough(dough_amount))
        self.materials.append(self.add_source(source_amount))
        self.materials.append(self.add_topping(topping_amount))

    @abstractmethod
    def add_dough(self, amount):
        """生地を追加するメソッド。"""
        pass

    @abstractmethod
    def add_source(self, amount):
        """ソースを追加するメソッド。"""
        pass

    @abstractmethod
    def add_topping(self, amount):
        """トッピングを追加するメソッド。"""
        pass

    def check(self):
        """Pizzaの材料をプリントするメソッド。"""
        print("Pizza:")
        print(*list(map(lambda m: m.check(), self.materials)))
