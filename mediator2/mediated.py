import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from typing import Optional


class Mediated(ABCD):
    def __init__(self) -> None:
        super().__init__()
        self.mediator = None
    
    def on_changed(self) -> None:
        self.mediator.on_change(self)