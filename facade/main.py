import sys
import os
from pathlib import Path
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from facade.archive import Archive

os.chdir(Path(__file__).parent)

filename_gz = "test_files/doc1.txt.gz"
filename_tar = "test_files/test.tar"
filename_targz = "test_files/test.tar.gz"
filename_zip = "test_files/test.zip"

for filename in [filename_gz, filename_tar, filename_targz, filename_zip]:
    with Archive(filename) as archive:
        print(f"files in {filename}: {archive.names}", end="\n\n")
        archive.unpack()