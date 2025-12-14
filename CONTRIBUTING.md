# Contributing to Raksh

Thanks for checking out the project! Here's how to get started with development.

## Getting Set Up

First, you'll need UV. Install it using any of the [blessed methods](https://docs.astral.sh/uv/getting-started/installation/). 

Also grab Make if you don't already have it.

### Quick Start

1. Clone and jump in:
   ```bash
   git clone https://github.com/your-username/raksh.git
   cd raksh
   ```

2. Install dependencies:
   ```bash
   make install
   ```

### Handy Commands

```bash
make clean         # Clean up all the local junk
make format        # Auto-format your code
make format-check  # See if formatting is needed
make lint-check    # Check code quality 
make test          # Run tests
make install       # Install development dependencies
```

## Making Changes

### Commit Messages

Raksh uses conventional commits which is important for automated releases.

- `feat:` New stuff
- `fix:` Bug fixes
- `docs:` Documentation
- `style:` Formatting, missing semicolons, etc
- `refactor:` Rewriting/restructuring code
- `test:` Adding or fixing tests
- `chore:` Boring stuff like updating dependencies
- `perf:` Performance improvements
- `ci:` CI/build stuff

## Testing

Tests live in `src/tests/`. Raksh uses pytest.

```bash
make test  # Run everything
pytest src/tests -k "specific_test"  # Run specific tests
```

## Code Style

Black for formatting:
```bash
make format  # Format everything
make format-check  # Just check, don't change
```

And Pylint for linting:
```bash
make lint-check
```

## How Releases Work

1. Features get merged to `develop`
2. Trigger "Release Module" workflow
3. Magic happens:
   - Version gets bumped based on commits
   - Changelog gets updated
   - GitHub release gets created
   - Package gets built and published to PyPI