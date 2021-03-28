import sys
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
from bridge.quickSort import QuickSorter
from bridge.bubbleSort import BubbleSorter
from bridge.sortableList import SortableList
from timeit import timeit
from random import randrange

quickSorter = QuickSorter()
bubbleSorter = BubbleSorter()

ll = [randrange(0, 1000, 1) for i in range(100)]

sortableList_use_QuickSorter = SortableList(quickSorter, ll)
sortableList_use_BubbleSorter = SortableList(bubbleSorter, ll)

loop_number = 100

target1 = "sortableList_use_QuickSorter.getSorted()"
time1 = timeit(target1, globals=globals(), number=loop_number)
print(f'"{target1}"を{loop_number}回実行した結果、掛かった時間は: {time1}s')

target2 = "sortableList_use_BubbleSorter.getSorted()"
time2 = timeit(target2, globals=globals(), number=loop_number)
print(f'"{target2}"を{loop_number}回実行した結果、掛かった時間は: {time2}s')
