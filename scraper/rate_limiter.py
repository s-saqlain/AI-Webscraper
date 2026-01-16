import asyncio
import random
from config import MAX_RETRIES, BASE_DELAY

async def retry_async(func, *args):
    for attempt in range(MAX_RETRIES):
        try:
            return await func(*args)
        except Exception:
            if attempt == MAX_RETRIES - 1:
                raise
            delay = BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
            await asyncio.sleep(delay)
