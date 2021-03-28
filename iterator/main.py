import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from iterator.Reversed import Reversed

for i in Reversed([1, 2, 3]):
    print(i)
