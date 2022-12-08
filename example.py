import requests
import time
from main import *


while True:
    user_input = input("> ").lower()

    if user_input == "yes":
        # Making a get request to the cats api
        request = requests.get("https://api.thecatapi.com/v1/breeds").content
        
        # Setting key and expire time for the cache (Default == None)
        key = "Breed" 
        expire = 3

        # If there isn't data with key in it, write new stuff to cache 
        if cache.read(key=key) == None:
            cache.write(key=key, data = request, expire_time=expire)
            print(request)
            print("Writing to cache")

        # If there is data in the cache with the key and didn't past expire time, read from cache
        elif cache.read(key) != None and cache.check(key) != None:
            print(cache.read(key))
            print("Reading from cache")

        # If the is data inside cache with the key, and id did past expire time, write new to cache
        elif cache.read(key) != None and cache.check(key) == None:
            write_to_cache = cache.write(key=key, data=request, expire_time=expire)
            print(request)    
            print("Cache expire is expired, writing new to cache")

    else:
        print("Vul yes in!")

