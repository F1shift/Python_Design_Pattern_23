
class A():
    def __init__(self) -> None:
        super().__init__()
    
    def __get__(self, obj, objtype):
        print("called5")
        return 1

class B():
    a = A()
    
    def __init__(self) -> None:
        super().__init__()
        self.aa = A()

b = B()
print(b.a)