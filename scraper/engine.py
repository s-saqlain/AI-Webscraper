import asyncio

from scraper.async_brightdata import fetch_html
from scraper.selenium_fallback import fetch_html_selenium
from scraper.parser import extract_text_and_tables
from scraper.captcha_detector import is_captcha_page
from scraper.rate_limiter import retry_async
from scraper.cache import get_cached, set_cache

async def scrape(url: str):
    cached = get_cached(url)
    if cached:
        return cached

    try:
        html = await retry_async(fetch_html, url)

        if is_captcha_page(html):
            raise RuntimeError("CAPTCHA detected")

    except Exception:
        # Selenium fallback
        html = fetch_html_selenium(url)

    text, tables = extract_text_and_tables(html)

    result = {
        "url": url,
        "text": text,
        "tables": tables,
    }

    set_cache(url, result)
    return result
