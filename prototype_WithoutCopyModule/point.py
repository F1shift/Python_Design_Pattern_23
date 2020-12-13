from os import pipe
import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from prototype_WithoutCopyModule.cloneable import Cloneable
from utils.abcd import override
from utils.register import registToMethod

class Point(Cloneable):
    def __init__(self, x: float, y: float) -> None:
        """2Dポイント。

        Args:
            x (float): X座標
            y (float): Y座標
        """
        self.__X: float = x
        self.__Y: float = y
        
    @property
    def X(self) -> float:
        return self.__X
    
    @X.setter
    def X(self, value: float) -> None:
        self.__X = value
        
    @property
    def Y(self) -> float:
        return self.__Y
    
    @Y.setter
    def Y(self, value: float) -> None:
        self.__Y = value
        
    @registToMethod(override)
    def clone(self) -> "Point":
        p = Point(self.X, self.Y)
        return p 

    @registToMethod(override)
    def __str__(self) -> str:
        return f"{{id:{ id(self)}, X:{self.X}, Y:{self.Y}, __X:{self.__X}, __Y:{self.__Y}}}"
