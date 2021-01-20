from os import read
import sys
from pathlib import Path
from typing import Iterable, Optional, Tuple
# 上層ディレクトリをライブラリ検索パスに追加する。upto (str) : 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
from abc import abstractmethod, abstractproperty
from utils.abcd import ABCD
from utils.abcd import override
from utils.register import regist
from enum import Enum
import os
import shutil
from datetime import datetime


class Command(ABCD):
    @abstractmethod
    def execute(self) -> None:
        pass
    
    @abstractmethod
    def undo(self) -> None:
        pass


class CreateCommand(Command):
    def __init__(self, path: str, content: str) -> None:
        super().__init__()
        self.path: str = path
        self.content: str = content

    @regist(override)
    def execute(self) -> None:
        with open(self.path, mode="w") as f:
            f.write(self.content)
    
    @regist(override)
    def undo(self) -> None:
        if os.path.isfile(self.path):
            os.remove(self.path)


class DeleteCommand(Command):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path: str = path
        self.backup: Optional[str] = None
    
    @regist(override)
    def execute(self) -> None:
        if os.path.isfile(self.path):
            with open(self.path, mode="r") as f:
                self.backup = f.read()
            os.remove(self.path)
    
    @regist(override)
    def undo(self) -> None:
        if self.backup:
            with open(self.path, "w") as f:
                f.write(self.backup)


class CopyCommand(Command):
    def __init__(self, source_path: str, target_path: str) -> None:
        super().__init__()
        self.source_path: str = source_path
        self.target_path: str = target_path
        
    @regist(override)
    def execute(self) -> None:
        shutil.copyfile(self.source_path, self.target_path)
    
    @regist(override)
    def undo(self) -> None:
        if os.path.isfile(self.target_path):
            os.remove(self.target_path)


class CompositeCommand(Command):
    def __init__(self, *commands: Command) -> None:
        super().__init__()
        self.commands: Tuple[Command] = commands
        
    @regist(override)
    def execute(self) -> None:
        for command in self.commands:
            command.execute()
    
    @regist(override)
    def undo(self) -> None:
        for command in reversed(self.commands):
            command.undo()


class MoveCommand(CompositeCommand):
    def __init__(self, source_path: str, target_path: str) -> None:
        copycommand = CopyCommand(source_path, target_path)
        deletecommand = DeleteCommand(source_path)
        super().__init__(copycommand, deletecommand)


def print_file(path: str) -> None:
    with open(path, mode="r") as f:
        print(f.read())


if __name__ == "__main__":
    workdir_path = Path(__file__).parent.joinpath("workdir")
    workdir = workdir_path.__str__()
    dir1 = workdir_path.joinpath("dir1").__str__()
    dir2 = workdir_path.joinpath("dir2").__str__()
    if not os.path.exists(dir1):
        os.makedirs(dir1)
    if not os.path.exists(dir2):
        os.makedirs(dir2)
    
    text1_path = dir1 + "/text1.txt"
    createcommand = CreateCommand(text1_path, f"text1: created at: {datetime.now()}")
    print(f"############# Create {text1_path}")
    createcommand.execute()
    print(f"dir1: {os.listdir(dir1)}")
    print_file(text1_path)
    print(f"############# undo Create {text1_path}")
    createcommand.undo()
    print(f"dir1: {os.listdir(dir1)}")
    
    print(f"############# Create {text1_path}")
    createcommand.execute()
    print(f"dir1: {os.listdir(dir1)}")
    print_file(text1_path)
    
    deletecommand = DeleteCommand(text1_path)
    print(f"############# delete {text1_path}")
    deletecommand.execute()
    print(f"dir1: {os.listdir(dir1)}")
    
    print(f"############# Create {text1_path}")
    createcommand.execute()
    print(f"dir1: {os.listdir(dir1)}")
    print_file(text1_path)
    
    text1_copy_path = dir2 + "/text1.copy.txt"
    copycommand = CopyCommand(text1_path, text1_copy_path)
    print(f"############# Copy {text1_path} to {text1_copy_path}")
    copycommand.execute()
    print(f"dir1: {os.listdir(dir1)}")
    print(f"dir2: {os.listdir(dir2)}")
    print_file(text1_copy_path)
    
    text1_copy_moved_path = dir1 + "/text1.copy.txt"
    movecommand = MoveCommand(text1_copy_path, text1_copy_moved_path)
    print(f"############# Move {text1_copy_path} to {text1_copy_moved_path}")
    movecommand.execute()
    print(f"dir1: {os.listdir(dir1)}")
    print(f"dir2: {os.listdir(dir2)}")
    
    print(f"############# Undo move {text1_copy_path} to {text1_copy_moved_path}")
    movecommand.undo()
    print(f"dir1: {os.listdir(dir1)}")
    print(f"dir2: {os.listdir(dir2)}")
    
    shutil.rmtree(workdir)