# 📦 Web Scraping Task 1: Structured Data Extraction with Python

Professional-Grade Web Scraping, Data Transformation, and Automation

---

## 🚀 Project Overview

This repository demonstrates robust, ethical, and modular web scraping for extracting structured product and book data from multiple real-world sites. Built with **requests**, **BeautifulSoup**, and **Pandas**, it features:

- **Reusable Extraction Logic** (CSS selectors, dynamic field mapping)
- **Intelligent Pagination Handling**
- **Clean Data Transformation & Output**
- **Comprehensive Logging and Error Handling**
- **Automated Notebook Workflow**

---

## 🖥️ Target Sites

- **Webscraper.io Laptops & Phones Demo**
  - Complex product cards, multi-page navigation, mixed HTML structures
- **Books to Scrape**
  - Book listings, star ratings, categories, availability, and pagination

---

## 🧩 Key Features

### 1. **Modular Scraper Architecture**
- Functions for request handling, soup creation, data extraction, and pagination
- Centralized extraction field definitions for maintainability

### 2. **Robust HTTP Request Logic**
- Custom headers for ethical scraping
- Automatic retry with exponential backoff
- Graceful error logging and handling

### 3. **Dynamic Pagination**
- Follows “next” links or numbered pages
- Detects end-of-pagination automatically

### 4. **Flexible Data Extraction**
- Handles nested, optional, and inconsistent HTML elements
- Extracts images, prices, ratings, links, and more
- Supports multiple datasets (products, books, categories)

### 5. **Clean Data Transformation**
- Converts raw lists to tidy Pandas DataFrames
- Price and rating normalization
- Outputs structured CSVs for analysis

### 6. **Automated Workflow**
- Makefile for install, lint, format, run, and preview
- Jupyter Notebook for orchestration and reproducibility
- CI for linting, testing, and smoke tests

### 7. **Proven Reliability**
- Logs every request, extraction, and warning to `logs/scraping.log`
- Testable, maintainable code with clear separation of concerns

---

## 📂 Outputs

- **src/main/data/laptops_allinone.csv** – Laptops product data
- **src/main/data/phones_allinone.csv** – Phones product data
- **src/main/data/books_bookstoscrape.csv** – Book listings with ratings, price, and availability
- **src/main/data/categories_bookstoscrape.csv** – Book categories

---

## 🔧 Quick Start

```sh
git clone https://github.com/guguandiledontsa/web-scraping-task1
cd web-scraping-task1
make install
make main
```

CSV outputs are saved in `src/main/data/`.

---

## ℹ️ Why This Project Stands Out

- **Industry Best Practices**: Structured, ethical, and maintainable scraping methods
- **Adaptable Patterns**: Easily reusable for new sites and data types
- **Transparent Logging**: Traceable workflow for debugging and compliance
- **Ready for Analysis**: Outputs are clean and analysis-ready

---

## 📖 Learn More

See the [Jupyter notebook](src/main/scraping.ipynb) for a step-by-step walk-through and code comments.

---

## ⚖️ Ethical Considerations

- Scraping targets are demo sites intended for educational use.
- The code respects robots.txt and terms of service.

---

## 💡 Get Involved

Pull requests and suggestions are welcome! See the `tests/` folder to add new unit tests and help improve extraction reliability.
