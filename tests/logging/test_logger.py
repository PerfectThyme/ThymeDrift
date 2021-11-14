import pytest
from thymedrift.logging.logger import QualityLogger


def test_quality_logger_singleton() -> None:
    # arrange
    logger1 = QualityLogger()
    logger2 = QualityLogger()

    # action

    # assert
    assert logger1 is logger2
