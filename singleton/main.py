import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from singleton.singletonClass import SingletonClass


a = SingletonClass()
b = SingletonClass()
print(f"id of a : {id(a)}")
print(f"id of b : {id(b)}")
assert id(a) == id(b), "違うインスタンスです！Singletonではなありません！"