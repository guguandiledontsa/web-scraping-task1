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


if __name__ == "__main__":
    ...