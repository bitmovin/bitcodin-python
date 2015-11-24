__author__ = 'Dominic Miglar'

import datetime


class BitcodinError(Exception):
    def __init__(self, message, error):
        self.message = message
        self.error = error

    def __str__(self):
        error_string = super(BitcodinError, self).__str__()
        return '%s\nError Message: %s\nAPI Response: %s\nOccurred at: %s' % (error_string, self.message, self.error,
                                                                             datetime.datetime.now())


class BitcodinInternalServerError(BitcodinError):
    pass


class BitcodinBadRequestError(BitcodinError):
    pass


class BitcodinNotFoundError(BitcodinError):
    pass


class BitcodinApiKeyNotAuthorizedError(BitcodinError):
    pass


class BitcodinApiKeyNotSetError(BitcodinError):
    pass
