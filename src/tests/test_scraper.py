import unittest
from unittest.mock import Mock
import requests
from main.scraper import fetch_response

class TestFetchResponse(unittest.TestCase):
    def test_fetch_response_success(self):
        mock_session = Mock()
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response

        response = fetch_response("http://example.com", session=mock_session)
        self.assertEqual(response, mock_response)
        mock_session.get.assert_called_once_with("http://example.com", timeout=10)

    def test_fetch_response_failure(self):
        mock_session = Mock()
        mock_session.get.side_effect = requests.exceptions.Timeout

        response = fetch_response("http://example.com", session=mock_session)
        self.assertIsNone(response)

if __name__ == "__main__":
    unittest.main()
    
