import time
import sys
import os

sys.path.insert(1, '../src/')

from app import get_sync,get_async

def timeis(func): 
    '''Decorator that reports the execution time.'''
  
    def wrap(*args, **kwargs): 
        start = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 

        print(func.__name__, end-start) 
        return end-start
    return wrap 

@timeis
def sync_10000():
    get_sync(2,10000)

@timeis
def async_10000():
    get_async(2,10000)

if __name__ == '__main__':
    sync_10000()
    async_10000()
    sync_10000()
    async_10000()
