import unittest
from unittest.mock import patch, Mock
import requests
from main.scraper import fetch_response

class TestFetchResponse(unittest.TestCase):

    @patch("main.scraper.logger")
    @patch("main.scraper.requests.Session.get")
    def test_fetch_response_http_error(self, mock_get, mock_logger):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        result = fetch_response("https://example.com/notfound")

        self.assertIsNone(result)
        mock_logger.error.assert_called_once()
        self.assertIn("404 Not Found", mock_logger.error.call_args[0][0])

    @patch("main.scraper.logger")
    @patch("main.scraper.requests.Session.get", side_effect=requests.exceptions.Timeout("Request timed out"))
    def test_fetch_response_timeout_error(self, mock_get, mock_logger):
        result = fetch_response("https://example.com")

        self.assertIsNone(result)
        mock_logger.error.assert_called_once()
        self.assertIn("Request timed out", mock_logger.error.call_args[0][0])

    @patch("main.scraper.logger")
    @patch("main.scraper.requests.Session.get", side_effect=requests.exceptions.ConnectionError("DNS failure"))
    def test_fetch_response_connection_error(self, mock_get, mock_logger):
        result = fetch_response("https://example.com")

        self.assertIsNone(result)
        mock_logger.error.assert_called_once()
        self.assertIn("DNS failure", mock_logger.error.call_args[0][0])

    def test_fetch_response_with_custom_session(self):
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "mocked"
        mock_response.raise_for_status = Mock()
        mock_session.get.return_value = mock_response

        result = fetch_response("https://example.com", session=mock_session)

        self.assertEqual(result.text, "mocked")
        mock_session.get.assert_called_once()

if __name__ == "__main__":
    unittest.main()
