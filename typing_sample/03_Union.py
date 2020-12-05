class A:
    pass

class B:
    pass

class B_sub(B):
    pass

class C():
    pass

#複数の型を許可する型を作る-----------------------------------------------
#C#のGenericsより高い自由度を持ち、
#無関係の複数型を許可できる。
#(C#では同じインターフェースまたは同じSuper Classの派生クラスである必要がある)
from typing import Union, List

e: List[Union[A, B]]
e = [A()]     # 内容物型チェック：OK
e = [B()]     # 内容物型チェック：OK
e = [B_sub()] # 内容物型チェック：OK
e = [C()]     # 内容物型チェック：警告
e.append(C()) # 引数型チェック：警告
