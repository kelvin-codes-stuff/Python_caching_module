import requests
import time
from main import *

request = requests.get("https://api.thecatapi.com/v1/breeds").content
key = "Breed" 


if cache.read(key=key) == None:
    cache.write(key=key, data = request, expire_time=3)
    print(request)
    print("Writing to cache")

elif cache.read("Breed") != None and cache.check("Breed") != None:
    print(cache.cache_read("Breed"))
    print("Reading from cache")
    
elif cache.read("Breed") != None and cache.check("Breed") == None:
    write_to_cache = cache.cache_write(key=key, data=request, expire_time=3)
    print(request)    
    print("Cache expire is expired, writing new to cache")

