from flask import Flask,request,Response
import requests
from math import ceil,floor
from cache_manager import get_cache,set_cache_app
import items_calc


from a_sync import get_async_items

from sync import get_pages_sync

app = Flask(__name__)

set_cache_app(app)

cache = get_cache()


items_calc.legacy_api = {
    'url':'https://sf-legacy-api.now.sh/items',
    'perPage': 100
}

def get_sync(page,perPage):
    pages = items_calc.calc_pages(page,perPage)

    pages_to_get, cached_res = items_calc.cached_pages(pages)


    resps = get_pages_sync(items_calc.legacy_api['url'],pages_to_get)

    for r in resps:
        cache.set(str(r["metadata"]["page"]), r)
        
    resps += cached_res

    response = items_calc.filter_responses(resps,page,perPage)

    return response
def get_async(page,perPage):
    pages = items_calc.calc_pages(page,perPage)

    pages_to_get, cached_res = items_calc.cached_pages(pages)

    resps = get_async_items(items_calc.legacy_api['url'],pages_to_get)

    for r in resps:
        cache.set(str(r["metadata"]["page"]), r)
        
    resps += cached_res

    response = items_calc.filter_responses(resps,page,perPage)

    return response



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/items/page/<int:page>')
@cache.cached()
def items_page(page):
    if page:
        resp = requests.get(
            items_calc.legacy_api['url'],
            params={'page': page}
        )

    return resp.json()



@app.route('/sync/items/page/<int:page>/perpage/<int:perPage>')
def sync_items_per_page(page,perPage):
    if page and perPage:
        return get_sync(page,perPage)
    else:
        return Response("{'ERROR':'Invalid request'}", status=403, mimetype='application/json')

@app.route('/items/page/<int:page>/perpage/<int:perPage>')
def async_items_per_page(page,perPage):
    if page and perPage:
        try:
            return get_async(page,perPage)
        except Exception as ex:
            return Response("{'ERROR':'" + str(ex) + "'}", status=501, mimetype='application/json')
    else:
        return Response("{'ERROR':'Invalid request'}", status=403, mimetype='application/json')


if __name__ == '__main__':
    pass
