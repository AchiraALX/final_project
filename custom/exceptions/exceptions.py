# Empty strings Error
class StringNotFoundError(Exception):
    """Empty strings exception"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return "Empty string error"


# Graph query error
class GraphQueryError(Exception):
    """Graph query exception"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return super().__repr__()
