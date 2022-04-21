"""
This is a project exceptions module
"""


class MongoSaveException(Exception):
    """Raise when there an error on try to save something on mongo"""


class MongoObjectsException(Exception):
    """Raise when there an error on try to query something on mongo"""


class NotFoundAnyUser(Exception):
    """Raise when cannot find any user on database"""


class CannotUpdateNotFoundCustomer(Exception):
    """Raise when trying to update a customer that not exists on database"""
