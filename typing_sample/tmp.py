from inspect import ismethod
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