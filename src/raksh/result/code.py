from enum import auto, EnumMeta, IntEnum
from functools import cache
from typing import Any, Sequence, Union


__all__ = [
    "auto",
    "FailureCode",
    "GenericFailureCode",
    "GenericSuccessCode",
    "SuccessCode",
]


def _normalize_name(name: str) -> str:
    """Prettifies passed name.

    Args:
        name: The name to normalize.

    Returns:
        The passed name (in title case) with all underscores changed to spaces.
    """
    return name.replace("_", " ").title()


@cache
def _wrap_alias(member: IntEnum, access_name: str) -> "_AliasWrapper":
    """Wraps alias enum in distinct object.

    Args:
        member: The SuccessCode enum member to wrap
        access_name: The name used to access this member
    """
    return _AliasWrapper(member, access_name)


class _AliasWrapper:
    """Construct to preserve access name and object identity when using Enum Aliases."""

    def __init__(self, member: IntEnum, access_name: str) -> None:
        """Initialize wrapper with enum member and access name.

        Args:
            member: The actual SuccessCode enum member
            access_name: The name used to access this member (e.g., "FOO")
        """
        self._member = member
        self._access_name = access_name
        self._value_ = member._value_

    def __str__(self) -> str:
        """Return human-readable representation based on access name."""
        return _normalize_name(self._access_name)

    def __int__(self) -> int:
        """Return integer value of the wrapped enum member."""
        return int(self._member)

    def __eq__(self, other: Any) -> bool:
        """Check equality based on the wrapped enum member."""
        return self._member == other

    def __getattr__(self, name: str) -> Any:
        """Forward attribute access to the wrapped enum member."""
        return getattr(self._member, name)


class _NoAliasMeta(EnumMeta):
    """Custom metaclass for SuccessCode that wraps member access.

    Intercepts attribute accesses to return enum members as wrapped objects
    to retain identity and the expected name.
    """

    def __getattribute__(cls, name: str) -> Any:
        # Skip attributes unlikely to be enum members.
        if not name.startswith("_") and name in cls._member_map_:
            return _wrap_alias(cls._member_map_[name], name)

        return super().__getattribute__(name)


class _ResultCode(IntEnum):
    """Base class for result codes representing success or failure states."""

    def __str__(self) -> str:
        return _normalize_name(self.name)

    def __repr__(self) -> str:
        return f"({self.__class__.__name__}: {str(self)} ({int(self)})>"


class FailureCode(_ResultCode):
    """Represents a failure of an operation.

    These codes must be defined such that code != 0.
    Prefer using `raksh.result.auto` over manual definition.
    """

    def __init__(self, *_args):
        super().__init__()
        if self == 0:
            raise ValueError("Failure code alue must not equal zero")

    @staticmethod
    def _generate_next_value_(
        _name: str, _start: int, _count: int, last_values: Sequence[Union[int, tuple]]
    ):
        """Ensures all codes generated using `auto` have non-zero value."""
        retval = 1

        if last_values:

            # Get the last numeric value from the sequence
            last_value = last_values[-1]

            # Handle base conversion (i.e. ("1e", 16) for hexadecimal) arguments.
            if isinstance(last_value, tuple):
                last_value = int(*last_value)

            retval = int(last_value) + 1

        if retval == 0:
            retval += 1

        return retval


class GenericFailureCode(FailureCode):
    """Represents nondescript failures.

    Prefer defining context-specific failure codes
    rather than using these.
    """

    FAILURE = auto()
    UNEXPECTED_EXCEPTION_RAISED = auto()


class SuccessCode(_ResultCode, metaclass=_NoAliasMeta):
    """Represents the success of an operation.

    These codes must all equal 0.

    Custom metaclass implementation ensures that all defined members will
    be distinct. This may break some native Enum Alias functionality.
    """

    def __init__(self, *_args):
        super().__init__()
        if self != 0:
            raise ValueError("Value must equal zero.")

    @staticmethod
    def _generate_next_value_(*_args, **_kwargs):
        """Ensures all codes generated with `auto` are 0."""
        return 0


class GenericSuccessCode(SuccessCode):
    """Represents a successful operation."""

    NO_OPERATION = auto()
    SUCCESS = auto()
