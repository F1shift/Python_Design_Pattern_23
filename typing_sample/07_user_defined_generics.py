class A:
    pass


class B1(A):
    pass


class B2(A):
    pass


class C1(B1):
    pass

#ユーザー定義のジェネリック型--------------------------------------------------------------
from typing import TypeVar, Generic, Union

T1 = TypeVar("T1", B1, B2) #B1とB2を受け入れる。サブクラスを含まない。
T2 = TypeVar("T2", bound=Union[B1, B2]) #B1とB2を受け入れる。サブクラスを含む。
T3 = TypeVar("T3") #任意の型を受け入れる

class MyList_T1(Generic[T1]):
    ...

class MyList_T2(Generic[T2]):
    ...
    
class MyList_T3(Generic[T3]):
    ...
    
class MyDict_T3_T2(Generic[T3, T1]):
    ...


myList1 = MyList_T1[A]()  #Genericタイプチェック：警告
myList1 = MyList_T1[B1]() #Genericタイプチェック：OK
myList1 = MyList_T1[B2]() #Genericタイプチェック：OK
myList1 = MyList_T1[C1]() #Genericタイプチェック：警告

myList2 = MyList_T2[A]()  #Genericタイプチェック：警告
myList2 = MyList_T2[B1]() #Genericタイプチェック：OK
myList2 = MyList_T2[B2]() #Genericタイプチェック：OK
myList2 = MyList_T2[C1]() #Genericタイプチェック：OK

myList3 = MyList_T3[A]()  #Genericタイプチェック：OK
myList3 = MyList_T3[B1]() #Genericタイプチェック：OK
myList3 = MyList_T3[B2]() #Genericタイプチェック：OK
myList3 = MyList_T3[C1]() #Genericタイプチェック：OK