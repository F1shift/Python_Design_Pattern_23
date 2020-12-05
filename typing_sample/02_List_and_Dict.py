class A:
    pass


class B1(A):
    pass


class B2(A):
    pass


class C1(B1):
    pass


#配列内容の型を与える----------------------------------------------------------------
from typing import List, Dict

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