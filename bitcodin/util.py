import re
from six import string_types

__author__ = 'David Moser <david.moser@bitmovin.net>'


def convert_dict(d):
    """
    Converts all camelCase styles attributes in the dictionary d to snake_case attributes.
    Returns the new dictionary which contains the snake_case attributes.
    :param d
    """
    if d is None:
        return

    new_d = {}
    for k, v in d.items():
        if isinstance(v, string_types):
            if isint(v):
                v = int(v)
            elif isfloat(v):
                v = float(v)
            else:
                v = v

        if isinstance(v, list):
            index = 0
            for d in v:
                if isinstance(d, dict):
                    v[index] = convert_dict(d)
                index += 1
            del index

        new_d[convert(k)] = convert_dict(v) if isinstance(v, dict) else v

    return new_d


def convert(name):
    """
    Converts camelCase strings to snake_case ones.
    :param name
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b
