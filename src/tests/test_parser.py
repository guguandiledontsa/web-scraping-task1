import unittest
from bs4 import BeautifulSoup
from unittest.mock import Mock
from main.parser import extract_elements

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
        soup = BeautifulSoup(html, "lxml")
        titles = extract_elements(soup, "h3 a", "text")
        self.assertEqual(titles, ["Link 1", "Link 2", "No title here"])

if __name__ == "__main__":
    unittest.main()
