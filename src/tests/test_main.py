import unittest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup

from main.scraper import fetch_response
from main.parser import (
    parse_html,
    select_elements,
    extract_from_elements,
    extract_elements
)


class TestParser(unittest.TestCase):
    def setUp(self):
        self.simple_html = "<div><a href='link1'>Link 1</a><a>Link 2</a><p>No link here</p></div>"
        self.soup = parse_html(self.simple_html)

    def test_parse_html(self):
        self.assertIsInstance(self.soup, BeautifulSoup)

    def test_select_elements(self):
        cases = [
            ("a", 2),
            ("nonexistent", 0),
            ("p", 1)
        ]
        for selector, expected_count in cases:
            with self.subTest(selector=selector):
                elements = select_elements(self.soup, selector)
                self.assertEqual(len(elements), expected_count)

    def test_extract_from_elements_text_and_attr(self):
        anchors = select_elements(self.soup, "a")

        test_cases = [
            ("text", ["Link 1", "Link 2"]),
            ("href", ["link1", ""])  # second <a> has no href attr
        ]
        for attr, expected in test_cases:
            with self.subTest(attr=attr):
                result = extract_from_elements(anchors, attr=attr)
                self.assertEqual(result, expected)

    def test_extract_from_elements_empty_list(self):
        self.assertEqual(extract_from_elements([], attr="text"), [])

    def test_extract_elements_end_to_end(self):
        class Response:
            text = self.simple_html

        test_cases = [
            ("a", "text", ["Link 1", "Link 2"]),
            ("a", "href", ["link1", ""]),
            ("p", "text", ["No link here"]),
        ]
        for selector, attr, expected in test_cases:
            with self.subTest(selector=selector, attr=attr):
                result = extract_elements(Response(), selector, attr)
                self.assertEqual(result, expected)

    def test_extract_elements_empty_html(self):
        class Response:
            text = ""

        self.assertEqual(extract_elements(Response(), "a", "text"), [])

    def test_extract_from_elements_nested_tags(self):
        html = "<div><a href='link'><span>Nested <b>Text</b></span></a></div>"
        soup = parse_html(html)
        elements = select_elements(soup, "a")
        texts = extract_from_elements(elements, attr="text")
        self.assertEqual(texts, ["Nested Text"])

    def test_extract_from_elements_missing_attr(self):
        html = "<a>Missing href</a>"
        soup = parse_html(html)
        elements = select_elements(soup, "a")
        hrefs = extract_from_elements(elements, attr="href")
        self.assertEqual(hrefs, [""])


class TestScraper(unittest.TestCase):

    @patch("src.scraper.requests.Session.get")
    def test_fetch_response_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "OK"
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = fetch_response("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")
        mock_get.assert_called_once()

    @patch("src.scraper.requests.Session.get")
    def test_fetch_response_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("404 Not Found")
        mock_get.return_value = mock_response

        response = fetch_response("https://example.com/notfound")
        self.assertIsNone(response)

    @patch("src.scraper.requests.Session.get", side_effect=Exception("Timeout"))
    def test_fetch_response_network_error(self, mock_get):
        response = fetch_response("https://example.com")
        self.assertIsNone(response)

    def test_fetch_response_with_custom_session(self):
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "mocked"
        mock_response.raise_for_status = Mock()
        mock_session.get.return_value = mock_response

        response = fetch_response("https://example.com", session=mock_session)
        self.assertEqual(response.text, "mocked")
        mock_session.get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
