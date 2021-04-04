import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from utils.abcd import override
from utils.register import regist
from mediator2.mediated import Mediated

class TextArea(Mediated):
    def __init__(self) -> None:
        super().__init__()
        self.text: str = ""
    
    def changeText(self, text: str):
        self.text = text
        self.on_changed()