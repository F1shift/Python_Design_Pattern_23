import tracemalloc, sys
from random import random
from typing import Dict, Any

# 0~9の数値をそれぞれ100回繰り返したindexesリストを作成する。
# Flyweightパターンを使用することで、重複のインスタンスを作成することを回避し、メモリ消費量が1/100になると想定されています。
indexes =  list(i for i in range(0, 10) for j in range(0, 100))

# Flayweightパターンを使わない
class A_Not_Flyweight():
    def __init__(self) -> None:
        super().__init__()
        self.a = [random() for i in range(0,1000)]


tracemalloc.start()
list1 = [A_Not_Flyweight() for i in indexes]
peak1 = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

# Flayweightパターンを使う
class A_Flyweight():
    __pool__: Dict[int, "A_Flyweight"] = {}
    
    def __new__(cls, index: int) -> Any:
        instance = cls.__pool__.get(index)
        if instance is not None:
            return instance
        else:
            instance = super().__new__(cls)
            cls.__pool__[index] = instance
            return instance
    
    def __init__(self, index: int) -> None:
        super().__init__()
        self.a = [random() for i in range(0,1000)]

tracemalloc.start()
list2 = [A_Flyweight(i) for i in indexes]
peak2 = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()



print(f"想定された結果では、メモリ消費量が元の{1/100}倍になるはずです。")
print("実際の結果は：")
print(f"Flayweightパターンを使わない場合の最大メモリ消費量は: {peak1} bytes")
print(f"Flayweightパターンを使う場合の最大メモリ消費量は:     {peak2} bytes")
print(f"Flayweightパターンを使うことで、最大メモリ消費量が{peak2/peak1:.3f}倍になりました。")
