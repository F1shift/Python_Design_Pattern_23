import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from typing import Any, IO, Iterator, List
from composite.abstractItem import AbstractItem
from utils.abcd import override
from utils.register import regist

class CompositeItem(AbstractItem):
    def __init__(self, name: str, *items: AbstractItem) -> None:
        super().__init__(name)
        self.children: List[AbstractItem] = list(items)
        
    def add(self, *items: AbstractItem) -> None:
        self.children.extend(items)
    
    def remove(self, item: AbstractItem) -> None:
        self.children.remove(item)
    
    @regist(override, property)
    def composite(self) -> bool:
        return True
    
    @regist(override, property)
    def price(self) -> float:
        return sum([item.price for item in self.children])
    
    @regist(override)
    def __iter__(self) -> Iterator["AbstractItem"]:
        return iter(self.children)

    @regist(override)
    def print(self, indent: str="    ", file: IO[Any]=sys.stdout) -> None:
        print(f"{indent}${self.price:.2f} {self.name}", file=file)
        for item in self.children:
            print(f"{indent}{indent}${item.price:.2f} {item.name}", file=file)