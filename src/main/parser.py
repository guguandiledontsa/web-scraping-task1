from .utils import get_logger

logger = get_logger()

def extract_elements(soup, selector, attr="text"):
    elements = soup.select(selector)
    extracted = extract_from_elements(elements, attr)
    logger.info(f"Extracted {len(extracted)} items using selector '{selector}' and attr '{attr}'")
    return extracted

def extract_from_elements(elements, attr="text"):
    extracted = []
    for el in elements:
        match attr:
            case "text":
                extracted.append(el.get_text(strip=True, separator=" "))
            case "html":
                extracted.append(str(el))
            case "inner_html":
                extracted.append("".join(str(c) for c in el.contents))
            case _:
                extracted.append(el.get(attr, ""))
    return extracted


def extract_blocks(soup, block_selector, fields):
    """
    Extract structured data blocks from soup.

    :param soup: BeautifulSoup object
    :param block_selector: CSS selector to identify each block
    :param fields: dict of {field_name: (selector, attr)}, relative to the block
    :return: List of dicts with extracted data
    """
    blocks = soup.select(block_selector)
    extracted_data = []

    for block in blocks:
        block_data = {}
        for field_name, (selector, attr) in fields.items():
            elements = block.select(selector)
            values = extract_from_elements(elements, attr)
            block_data[field_name] = values[0] if values else None
        extracted_data.append(block_data)

    logger.info(f"Extracted {len(extracted_data)} blocks using '{block_selector}'")
    return extracted_data
