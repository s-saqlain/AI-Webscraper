import aiohttp
from config import BRIGHTDATA_TOKEN, ZONE

BRIGHTDATA_TOKEN = "https://api.brightdata.com/request"

async def fetch_html(url: str) -> str:
    headers = {
        "Authorization": f"Bearer {BRIGHTDATA_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "zone": ZONE,
        "url": url,
        "format": "raw",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            BRIGHTDATA_TOKEN, json=payload, headers=headers, timeout=60
        ) as response:
            response.raise_for_status()
            return await response.text()
