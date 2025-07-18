"""module to handle request logic."""
import requests
from bs4 import BeautifulSoup
from .utils import get_logger

logger = get_logger()

def fetch_response(url, session=None, timeout=10):
    """Returns the reposne from a request to URL."""
    session = session or requests.Session()
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        logger.info(f"Fetched URL: {url}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return None

def fetch_soup(url, session=None, timeout=10, parser="lxml"):
    """Use fetch_response to make soup from url response."""
    response = fetch_response(url, session,timeout)
    soup = BeautifulSoup(response.text, parser)
    return soup
