import logging
from typing import Any
from enum import Enum
from ..util import Singleton


class QualityLoggingLevels(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class QualityLogger(Singleton):
    def __init__(self) -> None:
        self.logger = logging.Logger(
            name=__name__,
            level=logging.INFO
        )
    
    def log(self, message: str, level: QualityLoggingLevels) -> None:
        self.logger.log(
            level=level,
            msg=message,
        )


@staticmethod
def add_azure_application_insights(connection_string: str) -> None:
    from opencensus.ext.azure.log_exporter import AzureEventHandler

    # Create logger singleton
    logger = QualityLogger()

    # Create stream handler
    logger_stream_handler = logging.StreamHandler()
    logger_stream_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
    logger.addHandler(logger_stream_handler)

    # Add azure event handler
    azure_event_handler = AzureEventHandler()
    azure_event_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
    logger.addHandler(azure_event_handler)
