import sys
from pathlib import Path
# 親ディレクトリをsys.pathに追加。upto (int): 遡る階層。
sys.path.append(Path(__file__).parents[1].__str__())
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
@register(override)
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

    from utils.register import register
    from utils.override import override, check_override

    class A
        def method1():
            ...

    class B(A):
        @register(override)
        def method1(): #OK
            ...

        @register(override)
        def method2(): #OverrideException
            ...

    check_override(B)
    """
        override_methods = inspect.getmembers(class_to_check, lambda f: check_has_decorator(f, override.__name__))
        for method in override_methods:
            exist = False
            for base in class_to_check.__bases__:
                if method[0] in dir(cast(type, base)):
                    exist = True
                    break
            if not exist:
                raise OverrideException(f"class:[{class_to_check.__name__}]:オーバーライドできるメソッド：[{method[0]}]が見つかりませんでした！")

class ABCD(metaclass = ABCDMeta):...