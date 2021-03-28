import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from typing import Any, IO, Iterator

class AbstractItem(ABCD):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    
    @abstractproperty
    def composite(self) -> bool:
        ...
    
    @abstractproperty
    def price(self) -> float:
        ...
    
    @abstractmethod
    def __iter__(self) -> Iterator["AbstractItem"]:
        ...

    @abstractmethod
    def print(self, indent: str="    ", file: IO[Any]=sys.stdout) -> None:
        ...
