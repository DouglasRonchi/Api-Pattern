"""
This is a project exceptions module
"""


class MongoSaveException(Exception):
    """Raise when there an error on try to save something on mongo"""


class MongoObjectsException(Exception):
    """Raise when there an error on try to query something on mongo"""


class NotFoundAnyCustomer(Exception):
    """Raise when cannot find any customer on database"""


class CannotUpdateNotFoundCustomer(Exception):
    """Raise when trying to update a customer that not exists on database"""


class UnauthorizedException(Exception):
    """ Raise when got some error on decode token"""


class ForbiddenException(Exception):
    """ Raise when got denied access to operation or resource, not authorized to access"""

