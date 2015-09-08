__author__ = 'Dominic Miglar'


class BitcodinError(Exception):
    def __init__(self, message, error):
        self.message = message
        self.error = error


class BitcodinInternalServerError(BitcodinError):
    pass


class BitcodinBadRequestError(BitcodinError):
    pass


class BitcodinNotFoundError(BitcodinError):
    pass


class BitcodinUnknownApiRequestUrlError(BitcodinError):
    pass


class BitcodinApiKeyNotAuthorizedError(BitcodinError):
    pass


class BitcodinApiKeyNotSetError(BitcodinError):
    pass
