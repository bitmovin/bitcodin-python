__author__ = 'David Moser <david.moser@bitmovin.net>'

import requests

from .exceptions import BitcodinError
from .exceptions import BitcodinInternalServerError
from .exceptions import BitcodinApiKeyNotAuthorizedError
from .exceptions import BitcodinBadRequestError
from .exceptions import BitcodinNotFoundError


class RestClient(object):

    def __init__(self):
        pass

    @staticmethod
    def _raise_error(result):
        if result.status_code == 500:
            raise BitcodinInternalServerError('An HTTP 500 Internal Server Error occured', result.text)

        try:
            json_result = result.json()
        except ValueError:
            raise BitcodinError('An error occured which response could not be JSON-decoded.', result.text)

        if result.status_code == 404:
            raise BitcodinNotFoundError(
                'The API URL you requested does not exist',
                json_result
            )
        elif result.status_code == 401:
            raise BitcodinApiKeyNotAuthorizedError(
                'The API Key used in the request was not authorized to access the API.',
                json_result
            )
        elif result.status_code == 400:
            raise BitcodinBadRequestError('The API received a invalid request.', json_result)
        else:
            raise BitcodinError('An error occured while communicating with the bitcodin API', json_result)

    @staticmethod
    def post(url=None, headers=None, content=None):
        result = requests.post(url, data=content, headers=headers)

        if result.status_code == 201 or result.status_code == 200:
            if result.text == '':
                return result.text
            return result.json()
        else:
            RestClient._raise_error(result)

    @staticmethod
    def get(url=None, headers=None):
        result = requests.get(url, headers=headers)

        if result.status_code != 200:
            RestClient._raise_error(result)

        return result.json()

    @staticmethod
    def put(self):
        pass

    @staticmethod
    def patch(url=None, headers=None, content=None):
        result = requests.patch(url, data=content, headers=headers)

        if result.status_code != 200:
            RestClient._raise_error(result)

        return result.json()

    @staticmethod
    def delete(url=None, headers=None):
        result = requests.delete(url, headers=headers)

        if result.status_code == 204:
            return True
        elif result.status_code == 200:
            return result.json()
        else:
            RestClient._raise_error(result)
