import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from utils.abcd import override, ABCDMeta, ABCD
from utils.register import register
from abc import abstractmethod

class TestAbstractClass(metaclass=ABCDMeta):
    @abstractmethod
    def method1(self):
        ...

class TestConcreteClass(TestAbstractClass):
    @register(override)
    def method1(self):
        print("method1 in TestConcreteClass")
        
    @register(override) # override対象がいないため、エラーになります。
    def method2(self):
        print("method2 in TestConcreteClass")
    
test = TestConcreteClass()
test.method1()
test.method2()