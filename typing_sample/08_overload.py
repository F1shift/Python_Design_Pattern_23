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
    
    def method1(self, x: Union[int, str, float], *y: int) -> None: #本番の実装。上記のoverloadで型チェックする。
        if isinstance(x, int):
            print("int")
        elif isinstance(x, str):
            print("str")
        elif len(y) > 0: #ここでx,とyの型をチェックすると逆に余計なチェックと見なされ、警告が出されます。
            print("float, int")
        else:
            raise TypeError("処理できない型！")

instance = SomeClass()
instance.method1(1) #呼出型チェック：OK
instance.method1("1") #呼出型チェック：OK
instance.method1(1.0, 1) #呼出型チェック：OK
instance.method1(1.0) #呼出型チェック：警告