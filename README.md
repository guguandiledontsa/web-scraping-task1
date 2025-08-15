# web-scraping-task1

Data Collection and Web  Scraping - scrape data using requests and beautifulSoup from a selected website and store it in structured format

## Prerequisites

- Install GNU Make: `choco install make`
- Python 3.x installed

## Overview

This project demonstrates professional-grade web scraping of multiple sites using Python. It emphasizes modular, reusable code, robust HTTP handling, dynamic pagination, and clean data extraction aligned with best practices in the web scraping industry.

The main objectives of this project are to:

Scrape structured product data from multiple websites with varying HTML structures.

Handle pagination, dynamic content, and inconsistent DOM structures.

Transform raw HTML data into clean, ready-to-analyze datasets.

Maintain ethical scraping practices with proper request handling and logging.

Target Sites:

Webscraper Laptops Test Site

Demonstrates nested HTML, product cards, and pagination.

Books to Scrape

Demonstrates multiple categories, ratings, availability, and paginated book listings.


Project Structure
src/
├─ main/
│  ├─ data/                  # CSV outputs
│  ├─ scraper.py             # Scraping functions: fetch_response, make_soup, extract_blocks, pager
│  ├─ parser.py              # Extraction mapping & helper functions
│  ├─ utils.py               # Logger, common utilities
├─ tests/                    # Unit tests for extractors and scraper modules
scraping_notebook.ipynb      # Notebook orchestrating scraping, transformation, and saving
README.md

Features & Methodology
1. Site Selection & Justification

Sites were chosen to cover static and dynamic structures, multiple data formats, and pagination.

Ethical and legal compliance verified through robots.txt and terms of use.

2. HTML Structure Analysis

Each data field mapped to a stable CSS selector.

Accounts for optional/missing tags, extra whitespace, and nested structures.

Selectors centralized for maintainability.

3. HTTP Request Handling

Custom headers (User-Agent, Accept-Charset) used.

Retry logic with exponential backoff and max retry limit.

Adaptive delays avoid server overload.

HTTP errors are logged; requests fail gracefully.

4. Data Extraction Logic

Modular extraction functions (extract_blocks, extract_multiple_blocks) per logical group.

Handles missing or malformed fields.

Uses dictionaries for field mapping (allinone_extractions, all_book_extractions).

Transformers convert lists to flat DataFrames.

5. Pagination & Navigation

Dedicated pager function handles multi-page scraping.

Supports both “next” links and numbered pagination.

Detects end of pages and logs progress.

6. Dynamic Content Handling

Only uses browser automation if necessary (here, static scraping suffices).

Extraction works reliably even for AJAX-like HTML structures.

7. Data Cleaning & Transformation

Text normalized (strip whitespace, remove HTML entities).

Prices converted to float, ratings mapped to integers, currencies extracted.

Vectorized Pandas operations used for efficiency.

Metadata such as scrape date or page number can be added.

8. Output Formatting & Storage

Clean datasets saved in CSV format (UTF-8, index=False).

Separate files for laptops, books, and categories.

Centralized data/ folder for all outputs.

File naming includes dataset context.


Running the Notebook

Clone the repository:

git clone <repo_url>
cd <repo_dir>


Install dependencies:

make install


Run the scraping notebook:

make main


Outputs:

laptops_allinone.csv

books_bookstoscrape.csv

categories_bookstoscrape.csv


Logging

All logs stored in logs/scraping.log.

Tracks requests, extraction errors, warnings, and pagination info.