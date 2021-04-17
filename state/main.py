import sys
from pathlib import Path
from typing import Optional, overload
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from utils.abcd import override
from utils.register import regist

class State(ABCD):
    @abstractmethod
    def takeumbrella(self):
        pass
    
    @abstractmethod
    def laundry(self):
        pass


class Sunny(State):
    @regist(override)
    def takeumbrella(self):
        return "bring no umbrella"
    
    @regist(override)
    def laundry(self):
        return "dry outdoor"


class Cloudy(State):
    @regist(override)
    def takeumbrella(self):
        return "bring folding umbrella"
    
    @regist(override)
    def laundry(self):
        return "dry indoor"


class Rainy(State):
    @regist(override)
    def takeumbrella(self):
        return "bring normal umbrella"
    
    @regist(override)
    def laundry(self):
        return "dry indoor"


class Context:
    def __init__(self) -> None:
        self.__state__: State = Sunny()
    
    @property
    def state(self) -> State:
        return self.__state__

    @state.setter
    def state(self, sta: State) -> None:
        if self.__state__ is not sta:
            self.__state__ = sta
            print(f"Set state to : {self.__state__.__class__.__name__}")
    
    def takeumbrella(self):
        print(self.state.takeumbrella())
    
    @regist(override)
    def laundry(self):
        print( self.state.laundry())
    
    def showState(self):
        print(f"State: {self.state.__class__.__name__}")

def changeState(context: Context, sta: str) -> None:
    if sta.lower() == "sunny":
        context.state = Sunny()
    elif sta.lower() == "cloudy":
        context.state = Cloudy()
    elif sta.lower() == "rainy":
        context.state = Rainy()
    else:
        raise ValueError(f"unknow state：{sta}")

if __name__ == "__main__":
    context = Context()
    
    changeState(context, "sunny")
    context.showState()
    context.takeumbrella()
    context.laundry()
    
    changeState(context, "cloudy")
    context.showState()
    context.takeumbrella()
    context.laundry()
    
    changeState(context, "rainy")
    context.showState()
    context.takeumbrella()
    context.laundry()