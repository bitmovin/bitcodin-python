__author__ = 'David Moser <david.moser@bitmovin.net>'

import requests
from requests.exceptions import HTTPError


class RestClient(object):

    def __init__(self):
        pass

    @staticmethod
    def post(url=None, headers=None, content=None):
        result = requests.post(url, data=content, headers=headers)

        if result.status_code == 201 or result.status_code == 200:
            return result.json()

        else:
            raise HTTPError("\nStatus Code: %s Response: %s" % (result.status_code, result.json()))

    @staticmethod
    def get(url=None, headers=None):
        result = requests.get(url, headers=headers)

        if result.status_code != 200:
            raise HTTPError("\nStatus Code: %s Response: %s" % (result.status_code, result.json()))

        return result.json()

    def put(self):
        pass

    @staticmethod
    def delete(url=None, headers=None):
        result = requests.delete(url, headers=headers)

        if result.status_code == 204:
            return result.json

        else:
            raise HTTPError("\nStatus Code: %s Response: %s" % (result.status_code, result.json))
