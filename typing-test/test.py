from typing import Any

class A():
    def __new__(cls) -> Any:
        print("new A")
        s = super()
        print(f"super is {s}")
        return s.__new__(cls)
    
    def __init__(self) -> None:
        print("A")
        
class A1(A):
    def __new__(cls) -> Any:
        print("new A1")
        s = super()
        print(f"super is {s}")
        return s.__new__(cls)
    
    def __init__(self) -> None:
        print("A1")

class B():
    def __new__(cls) -> Any:
        print("new B")
        s = super()
        print(f"super is {s}")
        return s.__new__(cls)
    
    def __init__(self) -> None:
        print("B")
        
class B1(B):
    def __new__(cls) -> Any:
        print("new B1")
        s = super()
        print(f"super is {s}")
        return s.__new__(cls)
    
    def __init__(self) -> None:
        print("B1")
        
class C(A1, B1):
    def __new__(cls) -> Any:
        ins = super(A1, cls).__new__(cls)
        return ins
    
    def __init__(self) -> None:
        super(A, self.__class__).__init__(self)
        
c = C()