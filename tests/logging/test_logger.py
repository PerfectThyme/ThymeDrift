import pytest
from thymedrift.logging.logger import QualityLogger


def test_quality_logger_singleton() -> None:
    # arrange
    quality_logger1 = QualityLogger()
    quality_logger2 = QualityLogger()

    # action

    # assert
    assert quality_logger1 is quality_logger2
