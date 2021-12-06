from typing import Callable
from functools import update_wrapper
from abc import ABC, abstractclassmethod


class ValidationStep(ABC):
    @abstractclassmethod
    def __call__(self, function: Callable) -> Callable:
        self.function = function
        update_wrapper(self.create_validation_name.__func__, function)


class ValidationName(ABC):
    @abstractclassmethod
    def __call__(self, function: Callable) -> Callable:
        self.function = function
        update_wrapper(self.create_validation_name.__func__, function)
