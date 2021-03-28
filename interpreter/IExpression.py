import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD

class IExpression(ABCD):
    @abstractmethod
    def operate(self) -> float:
        pass