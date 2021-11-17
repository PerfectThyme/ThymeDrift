import pytest
import os
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


def test_data_logger_azure() -> None:
    # # arrange
    # connection_string = os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING", default=None)
    # data_logger = DataLogger()
    # message = "This is a test."
    # level = DataLoggingLevels.INFO
    # if not connection_string:
    #     raise Exception("Application Insights Connection String not provided.")

    # # action
    # data_logger.add_azure_application_insights(connection_string=connection_string)
    # data_logger.log(
    #     message=message,
    #     level=level
    # )

    # # assert
    pass
