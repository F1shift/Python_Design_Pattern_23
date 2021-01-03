#平均値メソッドを実行するの前に、入力値を各タイプから数値に変換するデコレータを付ける。
from typing import Iterator, Union, Callable, Tuple

target_func = Callable[..., float]

def convert_str(target: target_func) -> target_func:
    """メソッドを実行する前に引数をfloatに変換する手順を加える。

    Args:
        target (target_func): 目標メソッド

    Returns:
        target_func: ラッパーメソッド
    """
    def wrapper(*numbers) -> float:
        float_numbers = map(lambda n: float(n), numbers)
        return target(*float_numbers)
    return wrapper

@convert_str
def average(*numbers: Union[int, float]) -> float:
    return sum(numbers) / len(numbers)

print(average(1, "2", 5))