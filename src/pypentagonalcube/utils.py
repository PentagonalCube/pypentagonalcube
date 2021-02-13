"""

    u t i l s
    Utils
    ===================

    :description:
    A general file to hold utility functions.

"""
#
#   :builtins:
import hashlib
import os
import json
import re
import base64
import time


def md5_(value: str) -> str:
    """

    A function to return the md5 hash of the given string.

    :param value: The string to hash.

        :return: The hashed string.

    """
    return str(hashlib.md5(value.encode()).hexdigest())


def read_from_environment(variable_name: str, default_value: any = None, decode_from_json: bool = False):
    """

    A function to read an environment variable into the application.

    :param variable_name: The name of the variable in the OS.
    :param default_value: A default value to provide for the variable, note should be correct type.
    :param decode_from_json: Should the value in the environment be decoded from a JSON string?

        :return: The default value or the value from the environment.

    """
    value_from_environment = os.getenv(variable_name)
    if not value_from_environment:
        return default_value
    if decode_from_json:
        value_from_environment = json.loads(value_from_environment)
    return value_from_environment


def milliseconds_since(timestamp: float) -> int:
    diff = time.time() - timestamp
    #
    #   Convert into int ms.
    diff *= 1000
    diff = int(diff)
    return diff


def read_data_via_regex(find_re, look_here: str) -> str or None:
    """

    A basic function to find the first element that matches the regex and return it as a singular object.

    :param find_re: Regex to use.
    :param look_here: Text to analyse.

        :return: If it it exists, return the first element found in the text given.

    """
    content_ = re.findall(find_re, look_here)
    if content_:
        return content_[0]


def from_base_64(encoded_string: str) -> str:
    decoded = base64.b64decode(encoded_string.encode("utf-8")).decode()
    return str(decoded)


def to_base_64(unencoded_string: str) -> str:
    encoded = base64.b64encode(unencoded_string.encode("utf-8")).decode()
    return str(encoded)
