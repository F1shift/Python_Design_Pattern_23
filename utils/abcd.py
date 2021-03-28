#【背景紹介】
#   PythonのABCMetaクラスでは、抽象クラスを宣告するabstractmethodデコレータがありますが、
#   override対象が存在しているかをチェックする方法が実装されていないため、
#   overrideするつもりでしたが、新しいメソッドを作ってしまったことが発生する可能性があります、
#   それクラス作成時自動的にチェックするために、ABCMetaの改良クラスABCDMetaを作成しました。

#【コード内容説明】
#   デコレータを使って、overrideチェックを実現したABCMetaの改良クラスABCDMetaを作成しました。
#   詳細はPython_Design_Pattern_23\utilsに参照してください。
#   utilsではregisterとoverrideデコレーターを新しく作成し、
#   それを利用して、overrideチェックを実現したABCDMetaを作成しました。

import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).resolve().parents[1].__str__())
import inspect
from utils.register import check_has_decorator
from abc import ABCMeta
from typing import Callable, Any, Tuple, Dict, Type, cast

AnyMethod = Callable[..., Any]
Decorator = Callable[[AnyMethod], AnyMethod]

class OverrideException(Exception):
    """overrideチェックに失敗すろ時のエラー。"""
    pass


def override(method: AnyMethod) -> AnyMethod:
    """utils.registerと併用して、タグとして使います。

from utils.override import override
@regist(override)
def method():
    ...
"""
    return method


class ABCDMeta(ABCMeta):
    def __init__(self, name: str, bases: Tuple[type, ...], dic: Dict[str, Any]) -> None:
        super().__init__(name, bases, dic)
        ABCDMeta.__check_override__(self)

    @staticmethod
    def __check_override__(class_to_check: Type["ABCDMeta"]):
        """overrideするメソッドが存在しているかをチェックする。

    from utils.register import regist
    from utils.override import override, check_override

    class A
        def method1():
            ...

    class B(A):
        @regist(override)
        def method1(): #OK
            ...

        @regist(override)
        def method2(): #OverrideException
            ...

    check_override(B)
    """
        override_targets = inspect.getmembers(class_to_check, lambda f: 
            check_has_decorator(f, override.__name__))
        for target in override_targets:
            exist = False
            if isinstance(target[1], property):
                for base in class_to_check.__bases__:
                    baseClass_properties = inspect.getmembers(cast(type, base), lambda f: isinstance(f, property))
                    if target[0] in map(lambda t: t[0], baseClass_properties):
                        exist = True
                        break
            elif inspect.isfunction(target[1]):
                for base in class_to_check.__bases__:
                    baseClass_functions = inspect.getmembers(cast(type, base), inspect.isfunction)
                    if target[0] in map(lambda t: t[0], baseClass_functions):
                        exist = True
                        break
            else:
                raise OverrideException(f"[{class_to_check.__name__}].{target[0]}はメソッドやプロパティーではありません！")
            if not exist:
                raise OverrideException(f"class:[{class_to_check.__name__}]:オーバーライドできるメソッドやプロパティー：[{target[0]}]が見つかりませんでした！")

class ABCD(metaclass = ABCDMeta):...