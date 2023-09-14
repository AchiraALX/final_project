# Empty strings Error
class StringEmptyError(Exception):
    """Empty strings exception"""

    def __init__(self, *args: object):
        super().__init__(*args)

    def __str__(self) -> str:
        return "Empty string error"


# Graph query error
class GraphQueryError(Exception):
    """Graph query exception"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return super().__repr__()
