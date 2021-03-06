import logging
from enum import IntEnum
from typing import Any

from ..util import Singleton


class DataLoggingLevels(IntEnum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class DataLogger(Singleton):
    def __init__(self) -> None:
        self.logger = logging.Logger(
            name=__name__,
            level=logging.INFO
        )

    def log(self, message: str, level: DataLoggingLevels) -> None:
        self.logger.log(
            level=level,
            msg=message,
        )

    def add_azure_application_insights(self, connection_string: str) -> None:
        try:
            from opencensus.ext.azure.log_exporter import AzureEventHandler
        except ImportError:
            raise ImportError("Could not import 'opencensus.ext.azure.log_exporter' which is required for this Azure feature.")

        # Create quality logger
        quality_logger = DataLogger()

        # Create stream handler
        logger_stream_handler = logging.StreamHandler()
        logger_stream_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
        quality_logger.logger.addHandler(logger_stream_handler)

        # Add azure event handler
        azure_event_handler = AzureEventHandler(connection_string=connection_string)
        azure_event_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
        quality_logger.logger.addHandler(azure_event_handler)
