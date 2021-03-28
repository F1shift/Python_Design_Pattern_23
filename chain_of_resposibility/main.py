import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from utils.abcd import override
from utils.register import regist

class NullHandler(ABCD):
    def __init__(self, successor: "NullHandler" = None) -> None:
        super().__init__()
        self.__seccessor__ = successor
    
    def handle(self, event : str) -> None:
        self.pass_to_successor(event)
    
    def pass_to_successor(self, event: str) -> None:
        if self.__seccessor__:
            self.__seccessor__.handle(event=event)


class MouseHandler(NullHandler):
    @regist(override)
    def handle(self, event: str) -> None:
        if event == "mouse_event":
            print("マウスイベントが見つかりました！")
        else:
            self.pass_to_successor(event)


class KeyHandler(NullHandler):
    @regist(override)
    def handle(self, event: str) -> None:
        if event == "key_event":
            print("キーボードイベントが見つかりました！")
        else:
            self.pass_to_successor(event)


class TimerHandler(NullHandler):
    @regist(override)
    def handle(self, event: str) -> None:
        if event == "timer_event":
            print("タイマーイベントが見つかりました！")
        else:
            self.pass_to_successor(event)


if __name__ == "__main__":
    handler_chain = MouseHandler(KeyHandler(TimerHandler()))
    
    handler_chain.handle("key_event")
    handler_chain.handle("timer_event")
    handler_chain.handle("mouse_event")