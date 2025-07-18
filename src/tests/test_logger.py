import unittest
import logging
from main.utils import get_logger

class TestGetLogger(unittest.TestCase):
    def test_get_logger_returns_logger_instance(self):
        logger = get_logger("test_logger")
        self.assertIsInstance(logger, logging.Logger)
        
    def test_singleton_logger(self):
        logger1 = get_logger("test_logger")
        logger2 = get_logger("test_logger")
        self.assertIs(logger1, logger2)
        self.assertTrue(logger1.hasHandlers())

if __name__ == "__main__":
    unittest.main()
