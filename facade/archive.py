from typing import Iterator, Optional, Callable, Any, List
from os import path
from zipfile import ZipFile
import tarfile
import gzip

class Archive:
    def __init__(self, filename: str) -> None:
        super().__init__()
        self._file : Any = None
        self._unpack : Optional[Callable[..., Any]] = None
        self._getnames : Optional[Callable[...,List[str]]] = None
        self.filename = filename
        
    @property
    def filename(self) -> str:
        return self._filename
    
    @filename.setter
    def filename(self, value: str):
        self.close()
        self._filename = value
    
    def close(self) -> None:
        if self._file is not None:
            self._file.close()
            self.__init__("")
    
    @property
    def names(self) -> List[str]:
        if self._file is None:
            self.__prepare__()
        if self._getnames is not None:
            return self._getnames()
        else:
            raise ReferenceError("_getnamesメソッドが見つからない")

    def unpack(self):
        if self._file is None:
            self.__prepare__()
        if self._unpack is not None:
            return self._unpack()
        else:
            raise ReferenceError("_getnamesメソッドが見つからない")
    
    def __prepare__(self) -> None:
        if self.filename.endswith(".zip"):
            self.__prepare_zip__()
        elif self.filename.endswith((".tar", ".tar.gz", ".tar.bz2", ".tar.xz")):
            self.__prepare_tarball__()
        elif self.filename.endswith(".gz"):
            self.__prepare_gzip__()
        else:
            raise ValueError("未知のフォーマット: {}".format(self.filename))
    
    def __prepare_zip__(self):
        self._file = ZipFile(self.filename)
        self._getnames = self._file.namelist
        def extractall():
            self._file.extractall(path = path.dirname(self.filename))
        self._unpack = extractall
    
    def __prepare_tarball__(self):
        suffix = path.splitext(self.filename)[1]
        if suffix == ".tar":
            self._file = tarfile.open(self.filename, "r:")
        else:
            self._file = tarfile.open(self.filename, "r:" + suffix[1:])
        self._getnames = self._file.getnames
        def extractall():
            self._file.extractall(path = path.dirname(self.filename))
        self._unpack = extractall
    
    def __prepare_gzip__(self):
        filename = path.splitext(self.filename)[0]
        self._file = gzip.open(self.filename)
        def getnames() -> List[str]:
            return ["gzip内容をプレビューできません。"]
        self._getnames = getnames

        def extractall():
            with open(filename, "wb") as f:
                f.write(self._file.read())
        self._unpack = extractall
    
    def __str__(self):
        return "{}({})".format(self.filename, self._file is not None)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()