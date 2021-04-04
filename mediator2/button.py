import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from utils.abcd import override
from utils.register import regist
from mediator2.mediated import Mediated

class Button(Mediated):
    def __init__(self) -> None:
        super().__init__()
        self.isActive: bool = False
    
    def click(self):
        print("button pressed!")
        self.on_changed()
        
    
