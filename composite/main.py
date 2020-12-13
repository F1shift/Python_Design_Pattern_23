import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from composite.compositeItem import CompositeItem
from composite.simpleItem import SimpleItem

ruler = SimpleItem("Ruler", 1.60)
eraser = SimpleItem("Eraser", 0.20)
pencil = SimpleItem("Pencil", 0.40)
bunbougu_set = CompositeItem("Bunbougu Set", pencil, eraser, ruler)

box = SimpleItem("Box", 1.00)
boxedpencil_set = CompositeItem("Boxed Bunbougu Set", box, bunbougu_set)
boxedpencil_set.add(pencil)

for item in [pencil, ruler, eraser, bunbougu_set, boxedpencil_set]:
    item.print()