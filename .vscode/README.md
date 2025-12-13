# VS Code Setup

## Required Extension

This project uses the **Run on Save** extension to automatically execute formatting when code files are saved.

### Installation

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
3. Search for "Run on Save" by emeraldwalk
4. Click Install

### Alternative Installation

You can also install via command line:
```bash
code --install-extension emeraldwalk.runonsave
```

## How it Works

The extension is configured in `settings.json` to automatically run `make format` whenever you save any Python files.

## Manual Formatting

If you need to format files manually, you can run:
```bash
make format
```