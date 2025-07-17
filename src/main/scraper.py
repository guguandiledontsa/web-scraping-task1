import requests
from utils import get_logger

logger = get_logger()

def fetch_page(url, session=None, timeout=10):
    session = session or requests.Session()
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        logger.info(f"Fetched URL: {url}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return None
