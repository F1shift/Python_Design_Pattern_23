import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from utils.abcd import override
from utils.register import regist
from iterator.Iterator import Iterator


class Reversed(Iterator):
    def __init__(self, items):
        self.items = items
        self.index = len(items)

    @regist(override)
    def __iter__(self):
        return self

    @regist(override)
    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.items[self.index]
        else:
            raise StopIteration