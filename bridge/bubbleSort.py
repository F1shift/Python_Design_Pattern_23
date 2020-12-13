import sys
from pathlib import Path
from typing import Iterable
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import regist
from bridge.sorter import Sorter

class BubbleSorter(Sorter):
    @regist(override)
    def sort(self, ll: list) -> list:
        for i in range(len(ll) - 2):
            for j in range(0, len(ll) - 2 - i):
                if ll[j] < ll[j + 1]:
                    ll[j], ll[j + 1] = ll[j + 1], ll[j]
        return ll
