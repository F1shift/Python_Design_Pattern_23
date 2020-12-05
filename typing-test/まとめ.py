# Python version : 3.6.8
# IDE Tool: VS Code
# Pluging for IDE: Pyright

#変数の型チェック----------------------------------------------------------------------
a: int
a = 1  #変数型チェック：OK
a = 1.0  #変数型チェック：警告
b: float = "1" #変数型チェック：警告


def func(x: float) -> float: #警告：returnなしの可能性もある。PyCharmではチェックされない！
    if x > 1:
        return 1  #返値型チェック：OK
    elif x > 2:
        return 1.0  #返値型チェック：OK
    elif x > 3:
        return "a"  #返値型チェック：警告


a = func(1)  #引数型チェック：OK, a変数型チェック：警告
b = func(1.0)  #引数型チェック：OK, b変数型チェック：OK
b = func("1")  #引数型チェック：警告


#配列内容の型を与える----------------------------------------------------------------
from typing import List, Dict


class A:
    pass


class B1(A):
    pass


class B2(A):
    pass


class C1(B1):
    pass


c: List[B1]
c = [B1()]  #配列要素型チェック：OK
c = [C1()]  #配列要素型チェック：OK
c = [A()]  #配列要素型チェック：警告
c = [B2()]  #配列要素型チェック：警告
c = [A(), B1()]  #配列要素型チェック：警告, PyCharmではB1要素が含んでいればOKになってしまう。
c.remove(A())  #引数型チェック：警告
c.remove(B1())  #引数型チェック：OK
c.remove(B2())  #引数型チェック：警告
c.remove(C1())  #引数型チェック：OK

d: Dict[str, B1] = dict()
d["b"] = A()  #KeyとValue型チェック：警告
d["b"] = B1()  #KeyとValue型チェック：OK
d["b"] = B2()  #KeyとValue型チェック：警告
d["b"] = C1()  #KeyとValue型チェック：OK
d[1] = B1()  #KeyとValue型チェック：警告

#複数の型を許可する型を作る-----------------------------------------------
#C#のGenericsより高い自由度を持ち、
#無関係の複数型を許可できる。
#(C#では同じインターフェースまたは同じSuper Classの派生クラスである必要がある)
from typing import Union

class 

aa = A()
bb = B1()
cc = B2()
dd = C1()
e: List[Union[B1, B2]] = [bb, cc]
e.remove(aa)  #引数型チェック：警告
e.remove(bb)  #引数型チェック：OK
e.remove(cc)  #引数型チェック：OK
e.remove(dd)  #引数型チェック：OK


#変数型がクラスで特定のクラスのみを許可したいの場合-----------------------------------------------------
#配列内容がクラスで特定のクラスのみ許可したい場合
from typing import Type

x: Type[B1]
x = A  #変数型チェック：警告
x = B1  #変数型チェック：OK
x = B2  #変数型チェック：警告
x = C1  #変数型チェック：OK

#ケース１
f: List[Type[B1]] = []
f.append(A)   #引数型チェック：警告
f.append(B1)   #引数型チェック：OK
f.append(B2)   #引数型チェック：警告
f.append(C1)   #引数型チェック：OK

g: List[Union[Type[B1], Type[B2]]] = []
g.append(A)   #引数型チェック：警告
g.append(B1)   #引数型チェック：OK
g.append(B2)   #引数型チェック：OK
g.append(C1)   #引数型チェック：OK


#NewType----------------------------------------------------------------------------
#適用シーンが理解できない
from typing import NewType
NewInt = NewType("NewInt", int)#NewIntはintのサブクラスとみなされる。

intVar : int
newVar : NewInt
intVar = 1          #変数型チェック：OK
intVar = NewInt(1)  #変数型チェック：OK
newVar = 1          #変数型チェック：警告。スパークラスはサブクラスに黙然的に変換できないため。
newVar = NewInt(1)  #変数型チェック：OK


#メソッドの形式を指定する---------------------------------------------------------------
from typing import Callable, TypeVar


def func1(x: B1) -> float:
    pass #PyCharmではreturnなしの場合はチェックされない

def func2(x: B1) -> None:
    pass

def func3(x: C1) -> float:
    pass

def func4(x: int) -> None:
    pass

def func5() -> float:
    pass

h: Callable[[B1], float]
h = func1  #メソッドの形式チェック：OK
h = func2  #メソッドの形式チェック：警告
h = func3  #メソッドの形式チェック：警告。サブクラスは含まない。
h = func4  #メソッドの形式チェック：警告
h = func5  #メソッドの形式チェック：警告、Pycharmでは引数欠けている場合もOKとされてしまう。

h2: Callable[..., float] # リターンの型だけ制限したいとき、Anyと違い引数の数も制限しない。「...」はEllipsisと言う。
h2 = func1  #メソッドの形式チェック：OK
h2 = func2  #メソッドの形式チェック：警告
h2 = func3  #メソッドの形式チェック：警告
h2 = func4  #メソッドの形式チェック：OK


#メソッドの形式を指定するーその２：Decoratorの適用範囲を制限する-----------------------------
from typing import Callable
def some_decorator(method: Callable[[int], None]):
    def wrapper(x: int) -> None:
        ...
        return method(x)
    return wrapper

@some_decorator # Decorator適用対象メソッドの形式チェック：警告。some_decorator引数の型制限が働いでいる。
def method1():
    pass

@some_decorator # Decorator適用対象メソッドの形式チェック：OK
def method2(x: int):
    pass

#ユーザー定義のジェネリック型--------------------------------------------------------------
from typing import TypeVar, Generic

T = TypeVar("T", B1, B2) #B1とB2を受け入れる。サブクラスを含まない。
T2 = TypeVar("T2", bound=Union[B1, B2]) #B1とB2を受け入れる。サブクラスを含む。
S = TypeVar("S", int, str) #intとstrのみを受け入れる。サブクラスを含まない。
R = TypeVar("A") #任意の型を受け入れる

class MyList(Generic[T2]):
    def checkType(self):
        print(T)


class MyDict(Generic[S, T]):
    def checkType(self):
        print(S, T)


myList1 = MyList[A]() #Genericタイプチェック：警告
myList2 = MyList[B1]() #Genericタイプチェック：OK
myList2 = MyList[B2]() #Genericタイプチェック：OK
myList2 = MyList[C1]() #Genericタイプチェック：警告

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

#cast------------------------------------------------------------------------
from typing import cast
def cast_test_method(x: int) -> None:
    print(x + 1)

cast_test_method(cast(int, 1.0)) #「2.0」と出力
cast_test_method(cast(int, "1")) # エラー

#final------------------------------------------------------------------------
from typing import final #python 3.8から
from typing import Final #python 3.9から

class final_test_class():
    X_var : int = 1 # 一般変数
    X_final : Final[int] = 1 # Final変数
    Y_final : Final[int]  # Final変数。後で変更できないので、初期値が必須
    
    @final
    def method1(self) -> None:
        ...

class fsub_inal_test_class(final_test_class):
    X_var = 2    # 上書きチェック：OK
    X_final = 2  # 上書きチェック：警告
    def method1(self) -> None: # 上書きチェック：警告
        ...

#mypy_extention: TypedDict-------------------------------------------------------------------
#from mypy_extensions import TypedDict

#Student = TypedDict("Student", {"name": str, "age": int}) ??????????????????

# class Student(TypedDict):
#     name: str
#     age: int

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

#Metaclassの型チェック------------------------------------------------------------------------
from inspect import ismethod
inspect.ismethod(int)