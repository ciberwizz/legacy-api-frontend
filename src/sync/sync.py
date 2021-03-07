
import requests



def get_pages_sync(url, pages):
    responses = [requests.get( url, params={'page': x} ).json() for x in pages]
    return responses
