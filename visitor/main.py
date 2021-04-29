from inspect import currentframe, formatargspec
import sys
from pathlib import Path
from typing import Any, List, Union, overload
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from utils.abcd import override
from utils.register import regist
from pathlib import Path

class Element(ABCD):
    @abstractmethod
    def accept(self, visitor: "Visitor") -> None:
        ...

class Entry(Element):
    @abstractmethod
    def getName(self) -> str:
        ...
    
    def __str__(self) -> str:
        return self.getName()

class File(Entry):
    def __init__(self, name: str) -> None:
        self.__name__:str = name
        
    @regist(override)
    def getName(self) -> str:
        return self.__name__
    
    @regist(override)
    def accept(self, visitor: "Visitor") -> None:
        visitor.visit(self)

class Directory(Entry):
    def __init__(self, name: str) -> None:
        self.__name__:str = name
        self.__dir__: List[Entry] = list()
        
    @regist(override)
    def getName(self) -> str:
        return self.__name__
    
    @regist(override)
    def accept(self, visitor: "Visitor") -> None:
        visitor.visit(self)
    
    def append(self, entry: Entry) -> Entry:
        self.__dir__.append(entry)
        return self
    
    def remove(self, entry: Entry) -> Entry:
        self.__dir__.remove(entry)
        return self
    
    def __iter__(self):
        return self.__dir__.__iter__()
    

class Visitor(ABCD):
    @overload
    @abstractmethod
    def visit(self, entry: File) -> None:
        ...
    
    @overload
    @abstractmethod
    def visit(self, entry: Directory) -> None:
        ...
    
    @abstractmethod
    def visit(self, entry: Union[File, Directory]) -> None:
        ...

class ListVisitor(Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.__pwd__: str = ""
    
    @regist(override)
    def visit(self, entry: Union[File, Directory]) -> None:
        if isinstance(entry, File):
            self.visitFile(entry)
        elif isinstance(entry, Directory):
            self.visitDirectory(entry)
        else:
            raise ValueError("未知のタイプ")
            
    
    def visitFile(self, entry: File) -> None:
        print(Path.joinpath(Path(self.__pwd__), entry.getName()).__str__())
    
    def visitDirectory(self, entry: Directory) -> None:
        print(Path.joinpath(Path(self.__pwd__), entry.getName()).__str__())
        current_dir = self.__pwd__
        self.__pwd__ = Path.joinpath(Path(self.__pwd__), entry.getName()).__str__()
        for ent in entry:
            ent.accept(self)
        self.__pwd__ = current_dir

def main() -> None:
    workspaceDir = Directory("workspace")
    compositeDir = Directory("Visitor")
    testDir1 = Directory("test1")
    testDir2 = Directory("test2")
    workspaceDir.append(compositeDir)
    workspaceDir.append(testDir1)
    workspaceDir.append(testDir2)

    element = File("Element.py")
    entity = File("Entity.py")
    file = File("file.py")
    directory = File("Directory.py")
    visitor = File("Visitor.py")
    listVisitor = File("ListVisitor.py")
    main = File("main.py")
    compositeDir.append(element)
    compositeDir.append(entity)
    compositeDir.append(file)
    compositeDir.append(directory)
    compositeDir.append(visitor)
    compositeDir.append(listVisitor)
    compositeDir.append(main)

    workspaceDir.accept(ListVisitor())
    
if __name__ == "__main__":
    main()