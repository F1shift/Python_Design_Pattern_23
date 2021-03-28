import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from interpreter.Context import Context

context = Context("interpreter/context.xml")
expression = context.buildexpression()
print(f"答えは：{expression.operate()}")