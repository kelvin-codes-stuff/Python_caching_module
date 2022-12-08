from datetime import datetime

# Cache json storage
cache_files = {}

class cache():
    def write(key, data, expire_time):
        now = datetime.now()
        cache_files[key] = {
            "data": data,
            "expire": int(now.strftime("%H%M%S")) + expire_time,
        }
        return cache_files[data]["data"]


    def read(key):
        if not (cache_files.get(key) is None):
            return cache_files[key]["data"]
        return None


    def check(key):
        now = datetime.now()

        cache_file_expire = cache_files[key]["expire"]
        if int(now.strftime("%H%M%S")) > cache_file_expire:
            return None
        else:
            return "IDK"