from bs4 import BeautifulSoup
from .utils import get_logger

logger = get_logger()

def extract_titles(response):
    soup = BeautifulSoup(response.text, "lxml")
    titles = [a_tag.text.strip() for a_tag in soup.select("h3 a")]
    logger.info(f"Extracted {len(titles)} titles")
    return titles
    
def extract_elements(response, selector, attr="text"):
    soup = parse_html(response.text)
    elements = select_elements(soup, selector)
    extracted = extract_from_elements(elements, attr)
    logger.info(f"Extracted {len(extracted)} items using selector '{selector}' and attr '{attr}'")
    return extracted


def parse_html(html):
    return BeautifulSoup(html, "lxml")

def select_elements(soup, selector):
    return soup.select(selector)

def extract_from_elements(elements, attr="text"):
    return [
        el.get_text(strip=True, separator=" ") if attr == "text" else el.get(attr, "")
        for el in elements
    ]
