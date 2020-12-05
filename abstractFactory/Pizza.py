import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())

class Pizza:
    def __init__(self):
        self.materials = []

    def check(self):
        print("Pizza:")
        print(*list(map(lambda m: m.check(), self.materials)))