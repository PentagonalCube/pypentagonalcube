from unittest import TestCase
import os
#
#   :code:
from src.pypentagonalcube.requesting import (
    get_web_request_via_cache, read_from_cache, generate_cache_directory_path,
    generate_cached_file_path_for_url, url_response_is_cached
)
#
#   :packages:
import pytest

#
#   :statics:
EXAMPLE_GET_URL = "https://jsonplaceholder.typicode.com/todos/1"


class TestRequesting(TestCase):
    def tearDown(self) -> None:
        file_path = generate_cached_file_path_for_url(EXAMPLE_GET_URL)
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_read_from_cache(self):
        response = get_web_request_via_cache(url=EXAMPLE_GET_URL)
        cached_file_path = generate_cached_file_path_for_url(url=EXAMPLE_GET_URL)
        cached_response = read_from_cache(file_path=cached_file_path)
        assert response == cached_response

    def test_generate_cache_directory_path(self):
        cache_directory = generate_cache_directory_path()
        assert cache_directory == "/tmp/"

    def test_get_web_request_via_cache(self):
        response = get_web_request_via_cache(url=EXAMPLE_GET_URL)
        #
        #   Check it's in the cache now.
        assert url_response_is_cached(url=EXAMPLE_GET_URL) is not None
        #
        #   Re-requesting means I'll get the same file back.
        should_be_cached_response = get_web_request_via_cache(url=EXAMPLE_GET_URL)
        assert should_be_cached_response == response

    def test_generate_cached_file_path_for_url(self):
        result = generate_cached_file_path_for_url(url=EXAMPLE_GET_URL)
        assert result.endswith(".json") is True
        assert EXAMPLE_GET_URL not in result
        assert "-" in result

    def test_url_response_is_cached(self):
        #
        #   There is no file to start with.
        non_existent_file_result = url_response_is_cached(url=EXAMPLE_GET_URL)
        assert non_existent_file_result is None
        #
        #   Access and download this file.
        get_web_request_via_cache(url=EXAMPLE_GET_URL)
        should_now_exist = url_response_is_cached(url=EXAMPLE_GET_URL)
        assert should_now_exist is not None
        #
        #   Check that the time works too.
        get_web_request_via_cache(url=EXAMPLE_GET_URL)
        is_skipped_if_expired = url_response_is_cached(url=EXAMPLE_GET_URL, maximum_cached_seconds=0)
        assert is_skipped_if_expired is None
