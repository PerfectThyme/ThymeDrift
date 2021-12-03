# import pyspark
import inspect
from typing import Callable, Any
from functools import update_wrapper
from ..logging.logger import DataLogger, DataLoggingLevels


class ValidationStage(object):
    def __init__(self, name: str) -> None:
        self.name = name
    
    def __call__(self, function: Callable) -> Callable:
        self.function = function
        update_wrapper(self.create_validation_name.__func__, function)
        return self.create_validation_name
    
    def create_validation_name(self, *args, **kwargs) -> Any:
        print("naming")
        value = self.function(*args, **kwargs)
        return value


class TabularValidationStep(object):
    def __init__(self, expectation: str, log_level: DataLoggingLevels = DataLoggingLevels.INFO) -> None:
        self.expectation = expectation
        self.log_level = log_level
        self.logger = DataLogger()
    
    def __call__(self, function: Callable) -> Callable:
        self.function = function
        update_wrapper(self.check_quality.__func__, function)
        return self.check_quality
    
    def check_quality(self, *args, **kwargs) -> Any:
        value = self.function(*args, **kwargs)
        self.logger.log(message="Logging result", level=self.log_level)
        return value + self.expectation
