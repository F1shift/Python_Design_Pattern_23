import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abc import abstractmethod
from utils.abcd import ABCD
from utils.abcd import override
from utils.register import regist


class Material(ABCD):
    """素材"""
    @abstractmethod
    def check(self):
        """素材内容を出力"""
        pass


class Dough(Material):
    """生地"""
    def __init__(self, amount=1):
        self.amount = amount

    @abstractmethod
    def check(self):
        pass


class WheatDough(Dough):
    """小麦生地。"""
    @regist(override)
    def check(self):
        """素材内容を出力"""
        return f"WheatDough(amount = {self.amount})"


class RiceFlourDough(Dough):
    """米粉生地。"""
    @regist(override)
    def check(self):
        """素材内容を出力"""
        return f"RiceFlourDough(amount = {self.amount})"


class Source(Material):
    """ソース"""
    def __init__(self, amount=1):
        self.amount = amount

    @abstractmethod
    def check(self):
        pass


class TomatoSource(Source):
    """トマトソース。"""
    @regist(override)
    def check(self):
        """素材内容を出力"""
        return f"TomatoSource(amount = {self.amount})"


class BasilSource(Source):
    """バジルソース。"""
    @regist(override)
    def check(self):
        """素材内容を出力"""
        return f"BasilSource(amount = {self.amount})"


class Topping(Material):
    """トッピング"""
    def __init__(self, amount=1):
        self.amount = amount

    @abstractmethod
    def check(self):
        pass


class CoanTopping(Topping):
    """コーントッピング"""
    @regist(override)
    def check(self):
        """素材内容を出力"""
        return f"CoanTopping(amount = {self.amount})"


class CheeseTopping(Topping):
    """チーズトッピング。"""
    @regist(override)
    def check(self):
        """素材内容を出力"""
        return f"CheeseTopping(amount = {self.amount})"