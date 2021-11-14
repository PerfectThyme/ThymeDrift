from typing import Type, TypeVar

T = TypeVar(name="T")


class Singleton(object):
    _instances = {}
    
    def __new__(cls: Type[T], *args, **kwds) -> T:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls=cls, *args, **kwds)
        return cls._instances[cls]
