"""Main entry point for scraping books."""

from .scraper import fetch_soup
from .parser import extract_elements
from .utils import get_logger

logger = get_logger()

def main():
    """Main function to fetch and print book titles."""
    url = "https://books.toscrape.com"
    logger.info(f"Starting fetch for: {url}")
    soup = fetch_soup(url)
    if not soup:
        logger.error("Fetch failed - exiting.")
        return

    next_link = extract_elements(soup, "div .next a", "href")
    print(next_link)


if __name__ == "__main__":
    main()
