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