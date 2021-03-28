import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from bridge.sorter import Sorter
from typing import TypeVar

_T = TypeVar("_T")

class SortableList(list):
    def __init__(self, sorter: Sorter, source: list = []) -> None:
        super().__init__(source)
        self.sorter: Sorter = sorter
        
    def getSorted(self) -> "SortableList":
        sortedList = self.sorter.sort(self)
        return SortableList(self.sorter, sortedList)
