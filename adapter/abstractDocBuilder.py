import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abc import abstractmethod
from utils.abcd import ABCD


class AbstractDocBuilder(ABCD):
    @abstractmethod
    def append(self, text: str) -> "AbstractDocBuilder":
        pass
    
    @abstractmethod
    def append_line(self, text: str) -> "AbstractDocBuilder":
        pass
    
    @abstractmethod
    def build(self) -> str:
        pass
