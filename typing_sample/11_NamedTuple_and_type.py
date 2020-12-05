#NamedTupleとtype----------------------------------------------------------------------------------
from typing import NamedTuple, Any

#NamedTuple*******************************************
Point1 = NamedTuple("Point1", [("x", float), ("y", float), ("clone", Callable[[Any], Any])]) #クラスの代わりに使う。

def clone(self):
    return Point1(x=self.x, y=self.y, clone=self.clone)

p1 = Point1(x=1, y=2, clone=clone)
p2 = Point1(x=1, y="2", z=3) # y:引数型エラー。z:許可されていない変数
p3 = Point1() # 引数エラー。引数が必須

#typeでクラスを動的に生成する方法***********************
def point2_init(self, x: float, y:float):
    self.x = x
    self.y = y

Point2 = type('Point2',
            (object,),
            {'x': 0,
            'y': 0,
            '__init__': point2_init,
            'clone': clone})
p4 = Point2(1, 2) #static type checkerはエラーを示していますが、コードの実行には問題ない。


#伝統的なclassの書き方*********************************
class Point3():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = x
    
    def clone(self):
        return self.__class__(self.x, self.y)
p5 = Point3(1, 2)
