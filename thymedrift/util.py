from typing import Type, TypeVar

T = TypeVar(name="T")


class Singleton(object):
    _instances = {}
    
    def __new__(cls: Type[T], *args, **kwargs) -> T:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]
