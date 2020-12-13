import inspect

class A():
    def __init__(self) -> None:
        super().__init__()
        self._x:int = 0
        
    @property
    def x(self) -> int:
        return self._x
    
list = inspect.getmembers(A, inspect.is)
print()