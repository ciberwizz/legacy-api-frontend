from math import ceil,floor
from cache_manager import get_cache

legacy_api = {}

def calc_pages(page,perPage):
    pages = []


    n_pages = ceil(perPage/legacy_api['perPage'])
    start_index = (page-1)*perPage # item index starts at 0
    start_page = floor(start_index/legacy_api['perPage']) +1 # page index starts at 1

    pages = [ start_page + x for x in range(n_pages) ]

    return pages
    
def filter_responses(arr, page, perPage):
    start_index = (page-1)*perPage # item index starts at 0
    last_index = page *perPage -1

    cache = get_cache()

    totalItems = cache.get('totalItems')

    header = {        
            "page": page,
            "perPage": perPage
        }

    #finish building header and check if cache should be invalidated
    if len(arr) > 0 and  arr[0]["metadata"] and arr[0]["metadata"]["totalItems"]:
        if totalItems != arr[0]["metadata"]["totalItems"]:
            cache.clear()
            header['totalItems'] = arr[0]["metadata"]["totalItems"]
            cache.set('totalItems',header['totalItems'])
        else:
            header['totalItems'] = totalItems


    data = []

    if len(arr) > 0:
        arr.sort(key=lambda a: a["metadata"]["page"])

    for req in arr:
        data += [x for x in req["data"] if x["absoluteIndex"] >= start_index and x["absoluteIndex"] <= last_index]

    return {"metadata": header, "data": data}

def cached_pages(pages):
    cached_res = []
    pages_to_get = pages[:]

    cache = get_cache()

    for p in pages:
        c = cache.get(str(p))
        if c:
            cached_res.append(c)
            pages_to_get.remove(p)
    
    print(f'got {str(len(cached_res))} pages from {str(len(pages))} will fetch {str(len(pages_to_get))}')

    return (pages_to_get,cached_res)
