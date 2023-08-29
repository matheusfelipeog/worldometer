class ScraperException(Exception):
    """Base exception of the scraper package."""


class ParserError(ScraperException):
    """Generic parser error."""


class HTMLTablesNotFoundError(ParserError):
    """No HTML tables found by the parsing engine."""


class ColumnNamesLengthError(ParserError):
    """Length of column names different than expected."""
