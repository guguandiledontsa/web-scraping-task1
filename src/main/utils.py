"""Module to hold all utility functions."""
import logging
import os

_logger = None

def get_logger(name="books_scraper"):
    """Singleton logger to be used across the project."""
    global _logger
    if _logger:
        return _logger

    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s"
        )

        file_handler = logging.FileHandler("logs/scraper.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    _logger = logger
    return logger



def demo_urljoin_cases():
    cases = [
        # Basic relative file in same directory
        ("https://example.com/articles/page-1.html", "page-2.html"),

        # Go up one level
        ("https://example.com/articles/page-1.html", "../page-2.html"),
        ("https://example.com/articles/page-1.html", "./page-2.html"),
        

        # Absolute path (starts from root)
        ("https://example.com/articles/page-1.html", "/page-2.html"),

        # Base ends with slash (treated as folder)
        ("https://example.com/articles/", "page-2.html"),

        # Base without slash (treated as file)
        ("https://example.com/articles", "page-2.html"),

        # Base is domain only
        ("https://example.com", "page-2.html"),

        # href is an absolute URL (should override base)
        ("https://example.com/articles/page-1.html", "https://other.com/page-2.html"),

        # href starts with ./ (same folder)
        ("https://example.com/articles/", "./page-2.html"),

        # href with nested folder
        ("https://example.com/articles/", "2025/page-2.html"),

        # href goes up two levels
        ("https://example.com/a/b/c/index.html", "../../other.html"),

        # href starts with //
        ("https://example.com/articles/", "//cdn.example.com/lib.js"),

        # href is empty string
        ("https://example.com/articles/page-1.html", ""),

        # href is a fragment
        ("https://example.com/articles/page-1.html", "#section2"),

        # href is query only
        ("https://example.com/articles/page-1.html", "?page=2"),

        # href repeats current folder name (looks nested but isn't)
        ("https://example.com/articles/", "articles/page-2.html"),

        # href repeats current folder name with ./ (actually nested)
        ("https://example.com/articles/", "./articles/page-2.html"),

        # Weird case: base with trailing slash, href with leading slash
        ("https://example.com/articles/", "/page-2.html"),

        # Weird case: base with file, href with full path including ./ and ..
        ("https://example.com/blog/posts/post-1.html", "./../other/post-2.html"),

        # base is a "file", href has fragment and query
        ("https://example.com/page.html", "next.html?x=1#top"),

        # href is just a fragment
        ("https://example.com/articles/page-1.html", "#top")
    ]

    for base, href in cases:
        result = urljoin(base, href)
        print(f"{base:<45}\n{href:<35}\n{result}\n\n\n")


__ = lambda _: [i for i in dir(_) if not i.startswith("_")]