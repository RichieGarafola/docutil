"""
Centralized logging configuration.
"""

import logging
from pathlib import Path


def configure_logging(level: str = "INFO", log_file: Path | None = None) -> None:
    """
    Configure application logging.

    Ensures handlers are not duplicated.
    """

    logger = logging.getLogger()
    logger.setLevel(level.upper())

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    # Avoid duplicate console handlers
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)

        if not any(
            isinstance(h, logging.FileHandler) and h.baseFilename == str(log_file)
            for h in logger.handlers
        ):
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
