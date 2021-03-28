import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from interpreter.IExpression import IExpression
from utils.abcd import override
from utils.register import regist
from enum import Enum
from typing import List

class CalcMethod(Enum):
    Constant = "Constant"
    Addition = "Addition"
    Subtraction = "Subtraction"
    Multiplication = "Multiplication"
    Division = "Division"

class CalcExpression(IExpression):
    def __init__(self, method: CalcMethod, expressions: List[IExpression]) -> None:
        super().__init__()
        self._expressions : List[IExpression] = expressions
        if method == CalcMethod.Addition:
            self._method = lambda x, y : x + y
        elif method == CalcMethod.Subtraction:
            self._method = lambda x, y : x - y
        elif method == CalcMethod.Multiplication:
            self._method = lambda x, y : x * y
        elif method == CalcMethod.Division:
            self._method = lambda x, y : x / y
        else:
            raise ValueError(f"予想外のCalcMethod:{method}。Constantの場合Constantクラスを利用してください。")
        
    
    @regist(override)
    def operate(self) -> float:
        n = len(self._expressions)
        if n < 1:
            raise ValueError("Expressionの引数が足りません。")
        result = self._expressions[0].operate()
        for i in range(1, n):
            result = self._method(result, self._expressions[i].operate())
        return result