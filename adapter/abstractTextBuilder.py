import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod
from utils.abcd import ABCD

class AbstractTextBuilder(ABCD):
    @abstractmethod
    def add(self, text: str) -> "AbstractTextBuilder":
        pass
    
    @abstractmethod
    def add_line(self, text: str) -> "AbstractTextBuilder":
        pass
    
    @abstractmethod
    def build(self) -> str:
        pass
