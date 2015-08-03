__author__ = 'Dominic Miglar'


class ApiMessages:
    UNKNOWN_API_REQUEST_URL = {
        'status':   404,
        'message':  'unknown api-request-url'
    }

    API_KEY_NOT_AUTHORIZED = {
        'status':   401,
        'message':  'Given bitcodin-api-key is not authorized!'
    }
