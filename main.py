from datetime import datetime



class cache():
    # Cache json storage
    files = {}

    def write(key, data, expire_time):
        now = datetime.now()

        cache.files[key] = {
            "data": data,
            "expire": int(now.strftime("%H%M%S")) + expire_time,
        }
        return cache.files[key]["data"]


    def read(key):
        if not (cache.files.get(key) is None):
            return cache.files[key]["data"]
        return None


    def check(key):
        now = datetime.now()

        cache_file_expire = cache.files[key]["expire"]
        if int(now.strftime("%H%M%S")) > cache_file_expire:
            return None
        else:
            return "OK"