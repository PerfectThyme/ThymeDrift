import pytest
from thymedrift.logging.logger import DataLogger, DataLoggingLevels


def test_data_logger_singleton() -> None:
    # arrange
    data_logger1 = DataLogger()
    data_logger2 = DataLogger()

    # action

    # assert
    assert data_logger1 is data_logger2

def test_data_logger_logging() -> None:
    # arrange
    data_logger = DataLogger()
    message = "This is a test."
    level = DataLoggingLevels.INFO

    # action
    data_logger.log(
        message=message,
        level=level
    )

    # assert
