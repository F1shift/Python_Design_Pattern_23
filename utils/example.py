import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override, ABCDMeta
from utils.register import registToMethod, registToProperty
from abc import abstractmethod

class TestAbstractClass(metaclass=ABCDMeta):
    method2 = 1
    @abstractmethod
    def method1(self):
        ...

    @property
    def X(self):
        return "X"

class TestConcreteClass(TestAbstractClass):
    @registToMethod(override)
    def method1(self):
        print("method1 in TestConcreteClass")
        
    @registToProperty(override, property)
    def X(self):
        return "X in TestConcreteClass";
    
    @registToMethod(override) # override対象がいないため、エラーになります。
    def method2(self):
        print("method2 in TestConcreteClass")
        
    
    
test = TestConcreteClass()
test.method1()
test.method2()