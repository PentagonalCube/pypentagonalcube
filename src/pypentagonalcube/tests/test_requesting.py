from unittest import TestCase

#
#   :code:
from src.pypentagonalcube.requesting import (
    get_web_request_via_cache, read_from_cache, generate_cache_directory_path,
    generate_cached_filename_for_url, url_response_is_cached
)


class TestRequesting(TestCase):
    def test_generate_cache_directory_path(self):
        assert 1 == 1
