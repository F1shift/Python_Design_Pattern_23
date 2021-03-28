import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
import copy
from prototype_WithCopyModule.point import Point

p1 = Point(1, 2)
p2 = copy.deepcopy(p1)
print(p1)
print(p2)