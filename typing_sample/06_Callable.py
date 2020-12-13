class A:
    pass


class Sub_A(A):
    pass

#メソッドの形式を指定する---------------------------------------------------------------
from typing import Callable, Any


def func1(x: A) -> float:
    pass #PyCharmではreturnなしの場合はチェックされない

def func2(x: Sub_A) -> float:
    pass

def func3(x: A) -> None:
    pass

def func4(x: int) -> None:
    pass

def func5() -> float:
    pass

h: Callable[[A], float]
h = func1  #メソッドの形式チェック：OK
h = func2  #メソッドの形式チェック：警告。引数のタイプが違う。サブクラスは含まない。
h = func3  #メソッドの形式チェック：警告。リターンのタイプが違う。
h = func4  #メソッドの形式チェック：警告。引数のタイプが違う。
h = func5  #メソッドの形式チェック：警告、引数数が違う。# Pycharmでは引数欠けている場合はOKとされてしまう。


h2: Callable[[Any], float] # リターンの型だけ制限したいとき
h2 = func1  #メソッドの形式チェック：OK
h2 = func2  #メソッドの形式チェック：OK
h2 = func3  #メソッドの形式チェック：警告。リターンのタイプが違う。
h2 = func4  #メソッドの形式チェック：警告。リターンのタイプが違う。
h2 = func5  #メソッドの形式チェック：警告。引数数が違う。

h3: Callable[..., float] # リターンの型だけ制限したいとき、引数の数も制限しない。
h3 = func1  #メソッドの形式チェック：OK
h3 = func2  #メソッドの形式チェック：OK
h3 = func3  #メソッドの形式チェック：警告。リターンのタイプが違う。
h3 = func4  #メソッドの形式チェック：警告。リターンのタイプが違う。
h3 = func5  #メソッドの形式チェック：OK

# 「...」はEllipsisと言う。

#メソッドの形式を指定するーその２：Decoratorの適用範囲を制限する-----------------------------
from typing import Callable

method_format = Callable[[int], None]

def print_name_when_runned(method: method_format) -> method_format:
    def wrapper(x: int) -> None:
        #元のメソッドを実行した上て、何らかの手を加えるのがdecoratorの目的。
        print(f"{method.__name__}が実行された！") 
        method(x)
    return wrapper

@print_name_when_runned # Decorator適用対象メソッドの形式チェック：警告
def method1():
    pass

@print_name_when_runned # Decorator適用対象メソッドの形式チェック：OK
def method2(x: int):
    pass

method2(1) #　Consoleに「method2が実行された！」と出力