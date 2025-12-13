.PHONY: clean
.PHONY: format
.PHONY: format-check
.PHONY: install
.PHONY: lint-check
.PHONY: test

clean:
	rm -rf dist/ logs/ .venv/

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
