import unittest
import logging
from main.utils import get_logger

class TestGetLogger(unittest.TestCase):
    def test_get_logger_returns_logger_instance(self):
        logger = get_logger("test_logger")
        self.assertIsInstance(logger, logging.Logger)

if __name__ == "__main__":
    unittest.main()
