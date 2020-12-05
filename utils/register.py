from typing import Callable, Any, Optional

AnyMethod = Callable[..., Any]
Decorator = Callable[[AnyMethod], AnyMethod]

def register(*decorators: Decorator, target: Optional[AnyMethod] = None):
    """デコレーターを適用する同時にmethod._decoratorsリストに追加する。
    また、method._decorator_namesリストにデコレーター名を追加する。
    
    @register(decorator1, decorator2, ...)
    def method(...) -> ...:
        ...
    
    :param decorators: デコレーター
    :return:
    """
    def wrapper(method: AnyMethod):
        for deco in decorators:
            method = deco(method)
        setattr(method, "_decorators", decorators)
        setattr(method, "_decorator_names", tuple(map(lambda f: f.__name__, decorators)))
        return method
    return wrapper

def check_has_decorators(method: AnyMethod):
    """methodに_decoratorsを持っているのかをチェックする。

    :param method:
    :return:
    """
    if hasattr(method, "_decorators"):
        return True
    else:
        return False


def get_decorators(method: AnyMethod):
    """_decoratorsを返す。存在しないば場合はNoneを返す。

    :param method:
    :return:
    """
    return getattr(method, "_decorators", None)


def get_decorator_names(method: AnyMethod):
    """_decorator_namesを返す。存在しないば場合はNoneを返す。

    :param method:
    :return:
    """
    return getattr(method, "_decorator_names", None)


def check_has_decorator(method: AnyMethod, decorator_name: str):
    decorators_names = get_decorator_names(method)
    if decorators_names is None:
        return False
    else:
        return decorator_name in decorators_names
