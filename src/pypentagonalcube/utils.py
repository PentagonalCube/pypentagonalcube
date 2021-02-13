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
