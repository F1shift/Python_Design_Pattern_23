#継承で実現したAdapter
from os import terminal_size
import sys
from pathlib import Path
from utils.register import register
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from adapter.docBuilder import DocBuilder
from adapter.abstractTextBuilder import AbstractTextBuilder
from utils.abcd import override
from utils.register import register

class AdapterByInheritance(DocBuilder, AbstractTextBuilder):
    @register(override)
    def add(self, text: str) -> "AdapterByInheritance":
        self.append(text)
        return self
    
    @register(override)
    def add_line(self, text: str) -> "AdapterByInheritance":
        self.append_line(text)
        return self