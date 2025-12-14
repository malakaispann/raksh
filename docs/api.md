# API Reference

::: raksh.result.Result
    options:
      heading_level: 3

## Result Codes

::: raksh.result.SuccessCode

::: raksh.result.FailureCode

### Built-in Codes

These codes are provided for convenience. Prefer defining context-specific codes for failures.

::: raksh.result.GenericSuccessCode

::: raksh.result.GenericFailureCode

## Utilities

### auto

The `auto()` function is imported from Python's `enum` module for convenient automatic value assignment in custom result codes:

```python
from raksh.result import auto, FailureCode

class MyErrors(FailureCode):
    NETWORK_ERROR = auto()
    TIMEOUT = auto()
```

Prefer using it over manual definition of values.