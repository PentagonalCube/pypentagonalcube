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


def md5_(value: str) -> str:
    """

    A function to return the md5 hash of the given string.

    :param value: The string to hash.

        :return: The hashed string.

    """
    return str(hashlib.md5(value.encode()).hexdigest())
