from inspect import isclass, isfunction
from typing import Callable, Any, Dict, Union, Type, cast, TypeVar, Tuple

__AnyMethod = Callable[..., Any]
__FunctionDecorator = Callable[[__AnyMethod], __AnyMethod]
__FunctionOrPropertyDecorator = Union[Callable[[__AnyMethod], __AnyMethod], Type[property]]
__AnyMethodOrProperty = Union[__AnyMethod, property]
__registPool: Dict[__AnyMethodOrProperty, Tuple[__FunctionOrPropertyDecorator]] = {}

def registToMethod(*decorators: __FunctionDecorator) -> __FunctionDecorator:
    """デコレーターを適用する同時にmethod._decoratorsリストに追加する。
    また、method._decorator_namesリストにデコレーター名を追加する。
    
    @registToMethod(decorator1, decorator2, ...)
    def method(...) -> ...:
        ...
    
    :param decorators: デコレーター
    :return:
    """
    def wrapper(method: __AnyMethod) -> __AnyMethod:
        for deco in decorators:
            method = deco(method)
        __registPool[method] = decorators
        return method
    return wrapper

__propertyType__ = TypeVar("__propertyType__", bound=property)
        

def registToProperty(*decorators: __FunctionOrPropertyDecorator) :
    """デコレーターを適用する同時にmethod._decoratorsリストに追加する。
    また、method._decorator_namesリストにデコレーター名を追加する。
    
    @registToMethod(decorator1, decorator2, ...)
    def method(...) -> ...:
        ...
    
    :param decorators: デコレーター
    :return:
    """
    functionDecorators = [ cast(__FunctionDecorator, deco) for deco in decorators if isfunction(deco)]
    propertyDecorators = [ cast(Type, deco) for deco in decorators if isclass(deco)]
    def wrapper(method: __AnyMethod) -> property:
        for deco in functionDecorators:
            method = deco(method)
        for deco in propertyDecorators:
            method = deco(method)
        __registPool[method] = decorators
        return cast(property, method)
    return wrapper


def check_has_decorators(key: Any) -> bool:
    """methodに_decoratorsを持っているのかをチェックする。

    :param method:
    :return:
    """
    if not hasattr(key, "__hash__"):
        return False
    return key in __registPool


def get_decorators(method: __AnyMethodOrProperty):
    """_decoratorsを返す。存在しないば場合はNoneを返す。

    :param method:
    :return:
    """
    if not check_has_decorators(method):
        return None
    return __registPool[method]

def get_decorator_names(method: __AnyMethodOrProperty):
    """_decorator_namesを返す。存在しないば場合はNoneを返す。

    :param method:
    :return:
    """
    if not check_has_decorators(method):
        return None
    return map(lambda d: d.__name__, __registPool[method])


def check_has_decorator(method: __AnyMethodOrProperty, decorator_name: str):
    decorators_names = get_decorator_names(method)
    if decorators_names is None:
        return False
    else:
        return decorator_name in decorators_names
