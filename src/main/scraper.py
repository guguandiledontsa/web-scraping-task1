"""Module to scrape paginated book data."""
import requests
from bs4 import BeautifulSoup
from .utils import get_logger
from .parser import extract_elements

logger = get_logger()


def fetch_response(url, session=requests.Session()):
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        logger.info(f"fetched: {url}")
        return response
    except requests.exceptions.HTTPError as errh:
        logger.warning(f"HTTP error occurred:\n{errh}")
    except requests.exceptions.RequestException as err:
        logger.warning(f"{type(err).__name__}\n{err}")
    except Exception as e:
        logger.warning(f"Unhandled exception:\n{type(e).__name__}: {e}")

def make_soup(response=None, url=None):
    if isinstance(url, str):
        response = fetch_response(url)
    if not (response and response.status_code == 200):
        logger.warning(f"Couldn't make soup with: {response}")
        return None
    soup = BeautifulSoup(response.text, "lxml")
    logger.info("Soup's ready!")
    return soup

if __name__ == "__main__":
    ...