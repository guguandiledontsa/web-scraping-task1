"""Module to scrape paginated book data."""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .utils import get_logger
from .parser import extract_elements

logger = get_logger()

def fetch_response(url, session=None, timeout=10):
    if not isinstance(url, str) or not url.startswith("http"):
        logger.warning(f"Invalid URL: {url}")
        return None
    session = session or requests.Session()

    if not hasattr(session, "_retry_configured"):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "HEAD"],
            backoff_factor=1,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        session._retry_configured = True

    headers = {
        "User-Agent": "Mozilla/5.0",
        'Accept-Charset': 'utf-8',
    }
    try:
        response = session.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        logger.info(f"fetched: {url} [{response.status_code}]")
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
    
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "lxml")
    logger.info("Soup's ready!")
    return soup


def extract_blocks(soup, block_selector, fields):
    """
    Extract structured data blocks from soup.

    :param soup: BeautifulSoup object
    :param block_selector: CSS selector to identify each block
    :param fields: dict of {field_name: (selector, attr)}, relative to the block
    :return: List of dicts with extracted data
    """
    if not soup or not (blocks := soup.select(block_selector)):
        logger.info(f"No blocks found with selector '{block_selector}'. soup: {soup}")
        return []

    extracted_data = []
    for block in blocks:
        block_data = {}
        for field_name, (selector, attr) in fields.items():
            values = []
            elements = block.select(selector)
            for el in elements:
                match attr:
                    case "text":
                        values.append(el.get_text(strip=True, separator=" "))
                    case "html":
                        values.append(str(el))
                    case "inner_html":
                        values.append("".join(str(c) for c in el.contents))
                    case _:
                        values.append(el.get(attr, ""))

                if not value:
                    logger.info(f"for element ({el}) of attribute ({attr}) appended value ({value})")
            
            field_default = None
            block_data[field_name] = values if values else field_default
            if not values:
                logger.warning(f"field_name ({field_name}) found no data with selector ({selector}) and attribute ({attr}), used default ({field_default})")

        extracted_data.append(block_data)

    logger.info(f"Extracted {len(extracted_data)} blocks using '{block_selector}'")
    return extracted_data


def pager(base, max_pages, block_selector, element_selector, fetcher, callback, block_index=0, item_index=0):
    """
    Iterate through paginated links starting from `base`.
    Optionally inject:
      - `fetcher`: custom page-fetching logic.
      - `callback`: function to call with each (url, soup) pair.
    """

    pages = {}
    counter = 1
    while (counter <= max_pages) and (page_soup := fetcher(url=base)):
        link = extract_blocks(page_soup, block_selector, {element_selector: (element_selector, "href")})[block_index].get(element_selector)[item_index]
        next_url = urljoin(base, link)
        pages[next_url] = (page_soup, callback(page_soup) if callback else None)
    
        base = next_url
        counter += 1
        
    return pages

if __name__ == "__main__":
    ...
