import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from utils.abcd import override
from utils.register import regist
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from typing import List, Text


class Model(ABCD):
    def __init__(self) -> None:
        super().__init__()
        self.__observers__ : List["Observer"] = []
    
    def add_observer(self, observer: "Observer") -> None:
        self.__observers__.append(observer)
    
    def notify_observers(self):
        for observer in self.__observers__:
            observer.update(self)


class ConcreteModel(Model):
    def __init__(self) -> None:
        super().__init__()
        self.__text__ : str = "default test"
        self.__fontsize__ : float = 12
    
    @property
    def text(self) -> str:
        return self.__text__
    
    @text.setter
    def text(self, text: str) -> None:
        if self.__text__ != text:
            self.__text__ = text
            self.notify_observers()
    
    @property
    def fontsize(self) -> float:
        return self.__fontsize__
    
    @fontsize.setter
    def fontsize(self, fontsize: float) -> None:
        if self.__fontsize__ != fontsize:
            self.__fontsize__ = fontsize
            self.notify_observers()
        

class Observer(ABCD):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def update(self, model: Model) -> None:
        pass


class CLIView(Observer):
    @regist(override)
    def update(self, model: ConcreteModel) -> None:
        print(f"CLIView : {model.text}")


class GUIView(Observer):
    @regist(override)
    def update(self, model: ConcreteModel) -> None:
        print(f"GUIView : {model.text}(fontsize:{model.fontsize})")
        
if __name__ == "__main__":
    model = ConcreteModel()
    cliview = CLIView()
    guiview = GUIView()
    
    model.add_observer(cliview)
    model.add_observer(guiview)
    
    model.text = "text1"
    model.fontsize = 14
    model.text = "text2"
    model.fontsize = 16