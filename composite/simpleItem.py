import sys
from pathlib import Path
from typing import Any, IO, Iterator
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import regist
from composite.abstractItem import AbstractItem


class SimpleItem(AbstractItem):
    def __init__(self, name: str, price: float = 0.0) -> None:
        super().__init__(name)
        self._price: float = price
        
    @regist(override, property)
    def composite(self) -> bool:
        return False
    
    @regist(override, property)
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        self._price = value
    
    @regist(override)
    def __iter__(self) -> Iterator["AbstractItem"]:
        return iter([self])
    
    @regist(override)
    def print(self, indent: str = "    ", file: IO[Any]=sys.stdout) -> None:
        print(f"{indent}${self.price:.2f} {self.name}", file=file)