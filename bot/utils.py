import aiohttp


async def url_status(url: str):
    try:
        async with aiohttp.request('GET', url) as rspn:
            return rspn.status
    except aiohttp.client_exceptions.InvalidURL:
        return -1


async def get_url_title(url: str):
    async with aiohttp.request('GET', url) as rspn:
        t = await rspn.text()
        return t[t.find('<title>')+7 : t.find('</title>')]
