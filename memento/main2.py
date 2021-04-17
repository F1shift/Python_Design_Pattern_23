# このファイル歯クラス

import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())

import pickle

home_dir = Path(__file__).resolve().parent
filename = Path.joinpath(home_dir, "hoge.pickle")

try:
    with open(filename, "rb") as f:
        hoge_restored = pickle.load(f) # Hogeクラスが見つからないため、Errorになる。
        print(f"type(hoge_restored) => {type(hoge_restored)}")
except Exception as e:
    print(str(e))