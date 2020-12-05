#overload--------------------------------------------------------------------
from typing import overload, Union

class SomeClass():
    @overload
    def method1(self, x: int) -> None: #関数可能な呼び出し方を定義のみ、実装できない。
        ...
        
    @overload
    def method1(self, x: str) -> None: #関数可能な呼び出し方を定義のみ、実装できない。
        ...
        
    @overload
    def method1(self, x: float, y: int) -> None: #関数可能な呼び出し方を定義のみ、実装できない。
        ...
    
    def method1(self, x, *y) -> None: #本番の実装。上記のoverloadで型チェックするため、こちらでは型定義は不要。
        if isinstance(x, int):
            print("int")
        elif isinstance(x, str):
            print("str")
        elif isinstance(x, float) and len(y) > 0 and isinstance(y[0], int):
            print("float, int")
        else:
            raise TypeError("処理できない型！")

instance = SomeClass()
instance.method1(1) #呼出型チェック：OK
instance.method1("1") #呼出型チェック：OK
instance.method1(1.0, 1) #呼出型チェック：OK
instance.method1(1.0) #呼出型チェック：警告