"""Main entry point for scraping books."""

from .scraper import fetch_response
from .parser import extract_elements
from .utils import get_logger

logger = get_logger()

def main():
    """Main function to fetch and print book titles."""
    url = "https://books.toscrape.com"
    logger.info(f"Starting fetch for: {url}")
    response = fetch_response(url)
    soup = fetch_soup(url)
    if not response or not soup:
        logger.error("Fetch failed — exiting.")
        return

    titles = extract_elements(response, "h3 a", "title")
    for title in titles:
        print(title)
    next_link = extract_elements(response, "div .next a", "href")
    print(next_link)

if __name__ == "__main__":
    main()
