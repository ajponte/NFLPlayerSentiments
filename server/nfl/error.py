class DownstreamApiException(Exception):
    """Throw this error when there's an issue making a downstream API request."""
    def __init__(self, message: str, cause: Exception):
        self._msg = message
        self._cause = cause

    def message(self) -> str:
        return self._msg

    def cause(self) -> Exception | None:
        return self._cause
