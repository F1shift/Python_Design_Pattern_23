import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from adapter.docBuilder import DocBuilder
from adapter.abstractTextBuilder import AbstractTextBuilder
from utils.abcd import override
from utils.register import regist

class AdapterByInvoke(AbstractTextBuilder):
    def __init__(self) -> None:
        self.__docBuilder: DocBuilder = DocBuilder()
        
    @regist(override)
    def add(self, text: str) -> "AdapterByInvoke":
        self.__docBuilder.append(text)
        return self
    
    @regist(override)
    def add_line(self, text: str) -> "AdapterByInvoke":
        self.__docBuilder.append_line(text)
        return self
    
    @regist(override)
    def build(self) -> str:
        return self.__docBuilder.build()