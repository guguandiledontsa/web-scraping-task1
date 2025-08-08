"""Module to scrape paginated book data."""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
            elements = block.select(selector)

            values = []
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
            
            block_data[field_name] = values if values else None
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
    while (counter <= max_pages) and (fetched_page := fetcher(url=base)):
        page_soup = fetched_page
        link = extract_blocks(page_soup, block_selector, {element_selector: (element_selector, "href")})[block_index].get(element_selector)[item_index]
        next_url = urljoin(base, link)
        pages[next_url] = (page_soup, callback(page_soup) if callback else None)
    
        base = next_url
        counter += 1
    return pages

if __name__ == "__main__":
    ...