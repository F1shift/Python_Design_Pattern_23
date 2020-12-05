import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from prototype_WithoutCopyModule.point import Point


p1 = Point(1, 2)
p2 = p1.clone()
p2.X = 3
p2.Y = 4
p3 = p2.clone()
p3.X = 5
print(p1)
print(p2)
print(p3)