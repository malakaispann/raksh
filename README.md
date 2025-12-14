# Raksh

A Python library providing opinionated types and logic for handling operation results. Instead of the traditional exception-throwing approach, Raksh enables contextual information sharing about results while promoting safe programming practices.

## Tech Stack
- [Python](https://www.python.org/) - The one and only
- [UV](https://docs.astral.sh/uv/) - Fast, reliable Python package management

## Philosophy

In software development, there are often multiple discussions surrounding exception handling.

Python, in particular, advocates for a "do and ask for forgiveness" approach. This approach is further supported by its (relatively recent) implementation of [zero-cost exception handling](https://github.com/python/cpython/issues/84403#issuecomment-1093868126) in Python 3.11. Essentially, exceptions have no overhead unless they're caught. 

There's one glaring weakness to this approach, however – adherence to universal best practices. Software is only as good as the developers who spend time thinking about how it will be used, the appropriate boundaries, and edge cases to anticipate.

This module aims to encourage Pythonic and universal best practices by providing a context-specific delivery mechanism for operational results other than returning `None` which is one of the most vague, error-inducing patterns known in software (here's a [good primer discussion](https://softwareengineering.stackexchange.com/questions/373751/if-nulls-are-evil-what-should-be-used-when-a-value-can-be-meaningfully-absent) to get your toes wet on the subject). Through the use of these mechanisms, I hope that developers will:
- Spend a bit more time thinking about all reasonable failure cases the software can handle
- Distinguish between recoverable/expected and non-recoverable failures  
- Handle the predictable failure cases amicably and return context-specific information for upstream decision making.

Let's be clear, **exceptions have their place** and this module is no replacement for them. It won't ever be. Still, it's important to have mechanisms for the safe execution of logic.

The result? More predictable code with better error handling and clearer intent.

## Installation

```bash
pip install raksh
```

Or with UV:
```bash
uv add raksh
```

## Usage

### Basic Example

```python
from raksh.result import auto, Result, FailureCode

class RiskyOperationFailureCode(FailureCode):
    DIVISION_BY_ZERO = auto()

def my_risky_operation(a: float, b: float) -> Result[float]:
    if b == 0:
        return Result.failure(RiskyOperationFailureCode.DIVISION_BY_ZERO)
    return Result.success(a / b)

# Using the result
result = my_risky_operation(10, 2)
if result.is_success:
    print(f"Result: {result.value}")  # Result: 5.0
else:
    print(str(result))
    sys.exit(1)
```


## Final Note

This library is designed to make error handling more explicit and safer in Python applications. If you find it useful or use it as inspiration for your own projects, please link back to this repo or [MalakaiSpann.com](https://malakaispann.com).