__author__ = 'dmoser'

import re


def convert_dict(d):
    new_d = {}
    for k, v in d.iteritems():
        new_d[convert(k)] = convert_dict(v) if isinstance(v, dict) else v
    return new_d


def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()