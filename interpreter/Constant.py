import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from utils.abcd import override
from utils.register import regist
from interpreter.IExpression import IExpression

class Constant(IExpression):
    def __init__(self, value: float) -> None:
        super().__init__()
        self._value_ = value
    
    @regist(override)
    def operate(self) -> float:
        return self._value_