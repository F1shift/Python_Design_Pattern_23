import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from adapter.abstractTextBuilder import AbstractTextBuilder
from adapter.adapterByInheritance import AdapterByInheritance
from adapter.adapterByInvoke import AdapterByInvoke

textBuilder1 : AbstractTextBuilder = AdapterByInheritance()
textBuilder1.add("line1")
textBuilder1.add_line("line2")
result = textBuilder1.build()
print("Result by AdapterByInheritance:")
print(result)
print()

textBuilder2 : AbstractTextBuilder = AdapterByInvoke()
textBuilder2.add("line1")
textBuilder2.add_line("line2")
result = textBuilder2.build()
print("Result by AdapterByInvoke:")
print(result)
print()
