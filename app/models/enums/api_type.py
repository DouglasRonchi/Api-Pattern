"""
A ApiType enum module
"""
from enum import Enum


class ApiType(str, Enum):
    """
    APIs can be divided into three major groups:

    Private: These are APIs that are consumed only between services of the same product.
    Public: They are consumed between services of different products, but within the same business tower.
    Corporate: They are consumed between services of different towers, or even by third-party companies (outside of company).

    To meet API Quality indices, each type above must meet a minimum of standardization, as shown below:

    Private: Naming, URL Format, Standard HTTP Verbs, HTTP Return Status, Idempotence, Data Types, Record Identifier, and Health-check.
    Public: All Private API items plus: Custom Methods, Paging, Sorting, Filters, Error Handling, and Long (asynchronous) Processes.
    Corporate: All Public API items plus versioning.

    To identify each operation (endpoint) of the API, a special key must be used, through an extension
    to the OpenAPI file. This extension is called x-techmetrics and inside it there must be a key called apiLevel,
    which can have one of the following values:

    private for private APIs
    public for public APIs
    corporate for enterprise APIs
    """
    private = "private"
    public = "public"
    corporate = "corporate"
