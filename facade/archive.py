from typing import IO, Iterator, Optional, Callable, Any
from os import path
from zipfile import ZipFile
import tarfile
import gzip

class Archive:
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename
        self._file : Any = None
        self._unpack : Optional[Callable[..., Any]] = None
        self._getnames : Optional[Callable[...,Iterator[str]]] = None
        
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
    def names(self) -> Iterator[str]:
        if self._file is None:
            self.__prepare__()
        return self._getnames()

    def unpack(self):
        if self._file is None:
            self.__prepare__()
        return self._unpack()
    
    def __prepare__(self) -> None:
        if self.filename.endswith((".tar.gz", ".tar.bz2", ".tar.xz", ".zip")):
            self.__prepare_tarball_or_zip__()
        elif self.filename.endswith(".gz"):
            self.__prepare_gzip__()
        else:
            raise ValueError("未知のフォーマット: {}".format(self.filename))
        
    def __prepare_tarball_or_zip__(self):
        if self.filename.endswith(".zip"):
            self._file = ZipFile(self.filename)
            self._names = self._file.namelist
            self._unpack = self._file.extractall
        else:
            suffix = path.splitext(self.filename)[1]
            self._file = tarfile.open(self.filename, "r:" + suffix[1:])
            self._names = self._file.getnames
            self._unpack = self._file.extractall
    
    def __prepare_gzip__(self):
        filename = path.splitext(self.filename)[0]
        self._file = gzip.open(self.filename)
        def getnames():
            raise NotImplementedError("gzip内容をプレビューできません。") 
        self._names = getnames

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