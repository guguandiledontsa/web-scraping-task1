from scraper import fetch_page
from parser import extract_titles
from utils import get_logger

logger = get_logger()

def main():
    URL = "https://books.toscrape.com"
    logger.info(f"Starting fetch for: {URL}")
    
    response = fetch_page(URL)
    if not response:
        logger.error("Fetch failed — exiting.")
        return

    titles = extract_titles(response)
    for title in titles:
        print(title)

if __name__ == "__main__":
    main()
