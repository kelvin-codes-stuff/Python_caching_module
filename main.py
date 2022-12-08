import datetime

# Cache module
cache_files = {}


def cache_write(key, data):
    now = datetime.now()
    cache_files[key] = {
        "data": data,
        "expire": int(now.strftime("%H%M%S")) + 10,
    }
    return cache_files[data]["data"]


def cache_read(key):
    if not (cache_files.get(key) is None):
        return cache_files[key]["data"]
    return None


def check_cache(key):
    now = datetime.now()

    cache_file_expire = cache_files[key]["expire"]
    if int(now.strftime("%H%M%S")) > cache_file_expire:
        return None
    else:
        return "IDK"