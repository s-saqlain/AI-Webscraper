_cache = {}

def get_cached(url: str):
    return _cache.get(url)

def set_cache(url: str, data):
    _cache[url] = data
