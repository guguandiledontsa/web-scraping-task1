# parser.py
from bs4 import BeautifulSoup

def extract_titles(response):
    soup = BeautifulSoup(response.text, "lxml")
    return [tag['title'] for tag in soup.select("h3 a")]
