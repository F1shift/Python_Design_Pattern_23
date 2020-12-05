#cast------------------------------------------------------------------------
from typing import cast
def cast_test_method(x: int) -> None:
    print(x + 1)

cast_test_method(cast(int, 1.0)) #「2.0」と出力
cast_test_method(cast(int, "1")) # エラー