import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override
from utils.register import register
from adapter.abstractDocBuilder import AbstractDocBuilder

class DocBuilder(AbstractDocBuilder):
    def __init__(self) -> None:
        self.__strList = []
    
    @register(override)
    def append(self, text: str) -> "DocBuilder":
        self.__strList.append(text)
        return self
        
    @register(override)
    def append_line(self, text: str) -> "DocBuilder":
        self.__strList.append("\r\n" + text )
        return self
    
    @register(override)
    def build(self) -> str:
        return "".join(self.__strList)