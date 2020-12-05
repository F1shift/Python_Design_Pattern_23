from typing import Any, cast

# __new__、__init__、と多重継承----------------------------------------------------------------------------------
# __new__()メソッドはstaticmethod（classmethodではない）
# __init__はインスタンスメソッド

# 多重継承の複数のベースクラスからメンバーを呼び出す時、
# デフォルトの検査優先順位があります。
# この場合、検索の優先順位は A1 -> A -> B1 -> b -> object
# 
# super()で呼び出すとき、一番優先順位の高いA1のメソッドを呼び出す。
# super(t: Type, c: Type　or instanec object)で呼び出すとき(tはcのスーパークラス)、
# cクラスの検索順位リストから、tの次（つまりtは検索対象外）から検索していきます。
# 
# また、cがinstanec objectの時、メンバー呼出しはinstanec objectからの呼出と同じです。
# つまり、instanec objectはinstanec methodの第一引数として自動的に渡されます。
# ex:　super(A, self).__init__()　※selfはCのインスタンス。__init__にselfを渡す必要がない。
# ex:　super(A, C).__init__(self)　※__init__にselfを渡す必要がある。

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
        
        super(A, self).__init__() 
        
c = C()


# typeクラス---------------------------------------------------------------------------------------------
# クラスを宣告したとき、そのクラスを生成するにはtypeメソッドが呼び出されます。

#クラス宣告
class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = x
    
    def clone(self):
        return self.__class__(self.x, self.y)

# 以下と等価
# def __init__(self, x, y) -> None:
#     self.x = x
#     self.y = x
#
# def clone(self):
#     return self.__class__(self.x, self.y)
#
# Point = type('Point',
#             (object,),
#             {'__init__': __init__,
#             'clone': clone})

# metaclass----------------------------------------------------------------------------------------------
# Class生成する時にtypeの代わりに使うクラス