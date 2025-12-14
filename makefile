.PHONY: benchmark
.PHONY: clean
.PHONY: docs-serve
.PHONY: docs-build
.PHONY: format
.PHONY: format-check
.PHONY: install
.PHONY: lint-check
.PHONY: test

benchmark:
	uv run src/benchmark/error_handling_delta.py

clean:
	rm -rf dist/ logs/ .venv/ site/

docs-serve:
	uv run mkdocs serve

docs-build:
	uv run mkdocs build

format:
	uv run black src

format-check:
	uv run black --check src

install:
	uv run sync

lint-check:
	uv run pylint src

test:
	uv run pytest
