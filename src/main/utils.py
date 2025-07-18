"""Module to hold all utility functions."""
import logging
import os

_logger = None

def get_logger(name="books_scraper"):
    """Singleton logger to be used across the project."""
    global _logger
    if _logger:
        return _logger

    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s"
        )

        file_handler = logging.FileHandler("logs/scraper.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    _logger = logger
    return logger
