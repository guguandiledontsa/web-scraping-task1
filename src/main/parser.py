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
