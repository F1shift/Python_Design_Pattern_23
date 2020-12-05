import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from typing import Any, Union


class SingletonClass():
    __instance__: Union["SingletonClass", None] = None
    
    def __new__(cls) -> Any:
        if not cls.__instance__:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__
    
    @classmethod
    def getInstance(cls) -> "SingletonClass":
        return SingletonClass()