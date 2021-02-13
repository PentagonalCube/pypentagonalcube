def md5_(value: str) -> str:
    """
    A function to return the md5 hash of the given string.
    :param value:
    :return:
    """
    return str(hashlib.md5(value.encode()).hexdigest())
