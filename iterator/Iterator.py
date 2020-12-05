import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abc import abstractmethod
from utils.abcd import ABCD


class Iterator(ABCD):

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
