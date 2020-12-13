import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import registToMethod
from adapter.abstractDocBuilder import AbstractDocBuilder

class DocBuilder(AbstractDocBuilder):
    def __init__(self) -> None:
        self.__strList = []
    
    @registToMethod(override)
    def append(self, text: str) -> "DocBuilder":
        self.__strList.append(text)
        return self
        
    @registToMethod(override)
    def append_line(self, text: str) -> "DocBuilder":
        self.__strList.append("\r\n" + text )
        return self
    
    @registToMethod(override)
    def build(self) -> str:
        return "".join(self.__strList)