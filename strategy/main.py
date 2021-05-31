import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from utils.abcd import override
from utils.register import regist

class Human:
    def __init__(self,name: str, height: float, weight: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.weight = weight
        self.age = age
    
    @regist(override)
    def __str__(self) -> str:
        return f"name: {self.name}, height: {self.height}, weight: {self.weight}, age: {self.age}"

class Comparator:
    @abstractmethod
    def compare(self, h1: Human, h2: Human) -> int:
        ...

class AgeComparator(Comparator):
    @regist(override)
    def compare(self, h1: Human, h2: Human) -> int:
        if h1.age > h2.age:
            return 1
        elif h1.age < h2.age:
            return -1
        elif h1.age == h2.age:
            return 0
        else:
            raise ValueError(f"比較できない値: h1.age = {h1.age}, h2.age = {h2.age}")

class HeightComparator(Comparator):
    @regist(override)
    def compare(self, h1: Human, h2: Human) -> int:
        if h1.height > h2.height:
            return 1
        elif h1.height < h2.height:
            return -1
        elif h1.height == h2.height:
            return 0
        else:
            raise ValueError(f"比較できない値: h1.height = {h1.height}, h2.height = {h2.height}")
        
class WeightComparator(Comparator):
    @regist(override)
    def compare(self, h1: Human, h2: Human) -> int:
        if h1.weight > h2.weight:
            return 1
        elif h1.weight < h2.weight:
            return -1
        elif h1.weight == h2.weight:
            return 0
        else:
            raise ValueError(f"比較できない値: h1.weight = {h1.weight}, h2.weight = {h2.weight}")

class MyClass:
    def __init__(self, comparator: Comparator) -> None:
        self.comparator: Comparator = comparator
    
    def compare(self, h1: Human, h2: Human):
        return self.comparator.compare(h1, h2)

def main():
    h1 = Human("Tony", 172, 69, 29)
    h2 = Human("Jack", 170, 73, 35)
    
    print(h1)
    print(h2)
    
    myClass = MyClass(HeightComparator())
    print(f"compare height: {myClass.compare(h1, h2)}")
    
    myClass = MyClass(WeightComparator())
    print(f"compare weight: {myClass.compare(h1, h2)}")
    
    myClass = MyClass(AgeComparator())
    print(f"compare age: {myClass.compare(h1, h2)}")

if __name__ == "__main__":
    main()