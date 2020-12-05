import sys
from pathlib import Path
from typing import Iterable
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import register
from bridge.sorter import Sorter

class QuickSorter(Sorter):
    @register(override)
    def sort(self, ll: list) -> list:
        if len(ll) < 2:
            return ll
        
        p = ll[0]
        left = [x for x in ll[1:] if x < p]
        right = [x for x in ll[1:] if x >= p]
        
        return self.sort(left) + [ll] + self.sort(right)
