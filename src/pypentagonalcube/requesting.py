"""

    r e q u e s t i n g
    Requesting
    ===================

    :description:
    A basic file to wrap up a simple requesting function to include more than is available with just
    requests.get().

"""
#
#   :builtins:
import time
import os
import json
import logging
import pathlib
from datetime import datetime, timedelta

#
#   :code:
from .utils import md5_
from .settings import PYPENTAGONALCUBE_CACHE_SECONDS, CACHE_DATABASE_PATH


#
#   :packages:
import requests


def generate_cache_directory_path() -> str:
    """

    A function to make our cache folder if it doesn't exist, returns the path.

        :return:

    """
    tmp_dir = "C:\\temp\\"
    if os.sep == "/":
        tmp_dir = "/tmp/"
    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)
    return tmp_dir


def url_response_is_cached(url: str, maximum_cached_seconds: int = PYPENTAGONALCUBE_CACHE_SECONDS) -> str or None:
    """

    A function to determine if the given url is cached.
    If found and still within our cache age, the file path of the cached file is returned.

    :param url:
    :param maximum_cached_seconds:
    :return:
    """
    if maximum_cached_seconds is None:
        maximum_cached_seconds = 0
    #
    #   Render the md5 hash for this url.
    md5_hash = md5_(url)
    #
    #   Check all the files in our cache directory.
    cache_directory_path = generate_cache_directory_path()
    for f in os.listdir(cache_directory_path):
        if "-" in f:
            if md5_hash in f:
                #
                #   Check the time is valid.
                file_ = pathlib.Path(os.path.join(cache_directory_path, f))
                file_modified_at = datetime.fromtimestamp(file_.stat().st_mtime)
                maximum_file_age = file_modified_at + timedelta(seconds=maximum_cached_seconds)
                if maximum_file_age > datetime.now():
                    #
                    #   Time is valid, the file isn't too old.
                    return f"{cache_directory_path}{f}"
    return None


def generate_cached_file_path_for_url(url: str) -> str:
    """

    A function to generate a cached file path.

    :param url:
    :return:
    """
    unix_ts = str(time.time()).split(".")[0]
    filename = f"{md5_(url)}-{unix_ts}.json"

    cached_filepath = f"{generate_cache_directory_path()}{filename}"
    return cached_filepath


def read_from_cache(file_path) -> dict or list:
    """

    A function to read data from the cache.

    :param file_path:
    :return:
    """
    cached_data = None
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                cached_data = json.loads(f.read())
                return cached_data
            except json.decoder.JSONDecodeError:
                #
                #   Likely the cached file is corrupt, delete it.
                os.remove(file_path)
                return None


def save_to_cache(url, response):
    with open(generate_cached_file_path_for_url(url), "w", encoding="utf-8") as f:
        f.write(json.dumps(response, indent=2))


def get_web_request_via_cache(url: str, maximum_cached_seconds: int = None) -> dict or list:
    """

    A function to make a web request to a url via our local disk cache.

    :param url:
    :param maximum_cached_seconds: Optional maximum seconds.
    :return:
    """
    #
    #   Check the cache to see if we have a saved version.
    cached_filepath = url_response_is_cached(url, maximum_cached_seconds=maximum_cached_seconds)
    if cached_filepath:
        #
        #   Return the saved version from the disk.
        cached_data = read_from_cache(cached_filepath)
        if cached_data:
            logging.info(f"returning the data from cache for: {url}")
            return cached_data
    #
    #   Return the response from the web.
    logging.info(f"requesting data from the web for: {url}")
    web_response = requests.get(url, headers={
        "Content-Type": "application/json",
        "Referrer": "https://www.google.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like "
                      "Gecko) Chrome/87.0.4280.101 Safari/537.36"
    })
    if web_response.status_code < 400:
        #
        #   Make sure to save this new response.
        web_response_data = web_response.json()
        save_to_cache(url, web_response_data)
        #
        #   Now update our response in place.
        return web_response_data
    #
    #   We failed to make the request, return {}.
    return {}
