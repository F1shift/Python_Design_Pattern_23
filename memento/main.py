import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
import pickle

class Hoge:
    def __init__(self, name : str) -> None:
        self.name : str = name
    
    def print_hoge(self):
        print(f"Hoge: {self.name}")
        
hoge = Hoge("onamae")


home_dir = Path(__file__).resolve().parent
filename = Path.joinpath(home_dir, "hoge.pickle")
with open(filename, "wb") as f:
    pickle.dump(hoge, f)
    hoge.print_hoge()

with open(filename, "rb") as f:
    hoge_restored:Hoge = pickle.load(f)
    hoge_restored.print_hoge()
    
# リストアしたオブジェクトが同じクラスなのかをチェックする。
print(f"type(hoge) is type(hoge_restored) => {type(hoge) is type(hoge_restored)}")
print(f"hoge == hoge_restored => {hoge is hoge_restored}")