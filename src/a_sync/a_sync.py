import asyncio
import aiohttp


def get_asyncio_loop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()


async def fetch(url,page):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,params={'page': page}) as response:
            return await response.json()


def get_async_items(url, pages):

    print(f'getting async pages: {str(len(pages))}')

    loop = get_asyncio_loop()
    
    tasks =  [loop.create_task(fetch( url, x)) for x in pages]

    responses = loop.run_until_complete(asyncio.gather(*tasks))

    return responses 




