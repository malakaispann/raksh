from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Union

from raksh.result.code import (
    auto,
    FailureCode,
    GenericFailureCode,
    GenericSuccessCode,
    SuccessCode,
)


# pylint: disable-next-line=duplicate-code
__all__ = [
    "auto",
    "FailureCode",
    "GenericFailureCode",
    "GenericSuccessCode",
    "Result",
    "SuccessCode",
]

T = TypeVar("T")


@dataclass(frozen=True, init=True)
class Result(Generic[T]):
    """A construct for providing operational results.

    This class provides a structured method to represent operation outcomes
    without the overhead of exception handling for known failure outcomes. It enables
    the use of context-specific status codes that clearly communicate the result of
    an operation, making it ideal for operation with multiple outcomes .

    Examples:
        >>> # Creating a successful result with a value
        >>> result = Result.success(value=42)
        >>> assert result.is_success
        >>> assert result.value == 42

        >>> # Creating a failure with context-specific error code
        >>> from raksh.result import FailureCode
        >>> class NetworkError(FailureCode):
        ...     CONNECTION_TIMEOUT = 1
        ...     DNS_RESOLUTION_FAILED = 2
        ...     RATE_LIMITED = 3
        >>> result = Result.failure(code=NetworkError.CONNECTION_TIMEOUT)
        >>> assert result.is_failure
        >>> # The specific error code tells us exactly why it failed

    Args:
        code: The result code providing context about success or failure reason.
        value: Optional value associated with the result. Defaults to None.
    """

    code: Union[FailureCode, SuccessCode]

    value: Optional[T] = None

    @property
    def is_success(self) -> bool:
        """Returns whether the result can be considered a success."""
        return self.code == 0

    @property
    def is_failure(self) -> bool:
        """Returns whether the result can be considered a failure."""
        return not self.is_success

    @staticmethod
    def success(
        value: Optional[T] = None,
        code: Optional[SuccessCode] = GenericSuccessCode.SUCCESS,
    ) -> "Result[T]":
        """Factory method for generating 'successful' Results.

        Args:
            value: The value return with the result. Defaults to None.
            code: The success code to associate with the result.
                  Defaults to GenericSuccessCode.SUCCESS.
        """
        return Result(code, value)

    @staticmethod
    def failure(
        code: Optional[FailureCode] = GenericFailureCode.FAILURE,
        value: Optional[T] = None,
    ) -> "Result[T]":
        """Factory method for generating 'failure' Results.

        Args:
            code: The failure code to give the result. Defaults to GenericFailureCode.FAILURE.
            value: The value return with the result. Defaults to None.
        """
        return Result(code, value)

    def __str__(self) -> str:
        return f"({str(self.code.__class__.__name__)}) {str(self.code)}"
