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