"""Module to scrape paginated book data."""
import requests
from bs4 import BeautifulSoup
from .utils import get_logger
from .parser import extract_elements

logger = get_logger()

BASE_URL = "http://books.toscrape.com/catalogue/page-1.html"


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


def fetch_soup(url, session=None, timeout=10, parser="lxml"):
    """Convert URL response into BeautifulSoup object."""
    response = fetch_response(url, session, timeout)
    return BeautifulSoup(response.text, parser) if response else None


def get_next_link(soup, selector="div .next a", attr="href"):
    """Get the 'next page' link if available."""
    links = extract_elements(soup, selector, attr)
    return links[0] if links else None


def extract_book_data(book):
    """Extract title, price, and rating from a single book tag."""
    title = (
        book
        .select_one("h3 a")['title']
        if book.select_one("h3 a") and book.select_one("h3 a").has_attr("title")
        else None
    )

    price = (
        book
        .select_one(".price_color")
        .text.strip()
        if book.select_one(".price_color")
        else None
    )

    rating = (
        book
        .select_one("p.star-rating")['class'][1]
        if book.select_one("p.star-rating") and len(book.select_one("p.star-rating")['class']) > 1
        else None
    )

    return {
        "title": title,
        "price": price,
        "rating": rating
    }


def scrape_paginated_books(start_url):
    """Scrape all books across paginated catalog pages."""
    url = start_url
    all_books = []

    while url:
        soup = fetch_soup(url)
        if not soup:
            logger.warning(f"Skipping page due to failed fetch: {url}")
            break

        books = extract_elements(soup, "article.product_pod")
        logger.info(f"Found {len(books)} books on {url}")

        for book in books:
            book_data = extract_book_data(book)
            book_data["page"] = url
            all_books.append(book_data)

        next_relative = get_next_link(soup)
        url = f"http://books.toscrape.com/catalogue/{next_relative}" if next_relative else None

    return all_books


if __name__ == "__main__":
    logger.info("starting scraper")
    books = scrape_paginated_books(BASE_URL)
    logger.info(f"Scraped {len(books)} books")

    for book in books:
        print(book)
