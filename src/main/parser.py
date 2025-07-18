from bs4 import BeautifulSoup
from .utils import get_logger

logger = get_logger()

def extract_titles(response):
    soup = BeautifulSoup(response.text, "lxml")
    titles = [a_tag.text.strip() for a_tag in soup.select("h3 a")]
    logger.info(f"Extracted {len(titles)} titles")
    return titles
