"""Module to hold all utility functions."""

import os
import logging
import requests

__ = lambda _: [i for i in dir(_) if not i.startswith("_")]


_logger = None

def get_logger(name="books_scraper"):
    """Singleton logger to be used across the project.
    
    This version explicitly deletes the logs directory and its contents
    before recreating it to ensure a clean start for each program run.
    """
    global _logger
    if _logger:
        return _logger

    if os.path.exists("logs"):
        shutil.rmtree("logs")
    
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(levelname)s] %(filename)s:%(lineno)d %(funcName)s() %(message)s %(asctime)s"
        )

        file_handler = logging.FileHandler("logs/scraping.log", mode="w")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    _logger = logger
    return logger