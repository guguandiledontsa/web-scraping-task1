import unittest
from unittest.mock import Mock
from main.parser import extract_titles

class TestExtractTitles(unittest.TestCase):
    def test_extract_titles(self):
        html = '''
        <html>
          <body>
            <h3><a title="Title 1">Link 1</a></h3>
            <h3><a title="Title 2">Link 2</a></h3>
            <h3><a>No title here</a></h3>
          </body>
        </html>
        '''
        mock_response = Mock()
        mock_response.text = html

        titles = extract_elements(mock_response, attr="h3 a")
        self.assertEqual(titles, ["Link 1", "Link 2", "No title here"])

if __name__ == "__main__":
    unittest.main()
