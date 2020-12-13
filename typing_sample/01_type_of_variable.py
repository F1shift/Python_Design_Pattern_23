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