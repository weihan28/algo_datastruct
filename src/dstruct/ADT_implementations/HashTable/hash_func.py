""" Hash function for strings.
"""


def uni_hash_str(key: str, table_size: int = 17, hash_base: int = 31) -> int:
    """ Universal hash function for strings.
    Applies polynomial rolling hash (Horner's method).
    """
    value = 0
    a = 31415
    for char in key:
        value = (value * a + ord(char)) % table_size
        a = a * hash_base % (table_size - 1)
    return value


def hash_str(key: str, table_size: int = 17) -> int:
    """ Simple hash function for strings.
    Applies polynomial rolling hash (Horner's method).
    """
    value = 0
    a = 31415
    for char in key:
        value = (value * a + ord(char)) % table_size
    return value


def simple_hash(key: str, table_size: int = 17) -> int:
    """ Simple hash function for strings.
    """
    return ord(key[0]) % table_size
