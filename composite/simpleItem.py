import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import registToMethod
from composite.abstractItem import AbstractItem

class SimpleItem(AbstractItem):
    def __init__(self, name: str, price: float = 0.0) -> None:
        super().__init__(name)
        self._price: float = price
        
    @registToMethod(override)
    def 