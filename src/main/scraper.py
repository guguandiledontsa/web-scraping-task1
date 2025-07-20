"""module to handle request logic."""
import requests
from bs4 import BeautifulSoup
from .utils import get_logger
from .parser import extract_elements

logger = get_logger()

def fetch_response(url, session=None, timeout=10):
    """Returns response from a request to URL."""
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
    return BeautifulSoup(response.text, parser) if (response is not None) else None


def get_next_link(url, selector="div .next a", attr="href"):
    return extract_elements(fetch_soup(url), selector, attr)
    

BASE_URL = "http://books.toscrape.com/catalogue/page-1.html"

def scrape_paginated_books(start_url):
    url = start_url
    all_books = []

    while url:
        soup = fetch_soup(url)
        if not soup:
            break

        books = extract_elements(soup, 'article.product_pod')
        for book in books:
            title = book.h3.a['title']
            price = book.select_one('.price_color').text if book.select_one('.price_color') else None
            rating = book.p['class'][1] 
            all_books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "page": url
            })

        next_link = get_next_link(url)
        url = f"http://books.toscrape.com/catalogue/{next_link[0]}" if next_link else None

    return all_books


if __name__ == "__main__":
    logger.info("starting scraper")
    books = scrape_paginated_books(BASE_URL)
    logger.info(f"got {len(books)} books from {BASE_URL}")
    
    for book in books:
        print(book)