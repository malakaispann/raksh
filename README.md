# Python Package Template

A modern Python package template with automated releases, testing, and publishing to PyPI. Built with [uv](https://github.com/astral-sh/uv) for fast, reliable Python package management and [python-semantic-release](https://python-semantic-release.readthedocs.io/) for automated versioning.

## Features

- Modern Python packaging with [uv](https://github.com/astral-sh/uv) and `pyproject.toml`
- Automated semantic versioning and releases using [python-semantic-release](https://python-semantic-release.readthedocs.io/)
- Testing setup with [pytest](https://docs.pytest.org/)
- Code formatting with [black](https://black.readthedocs.io/) and linting with [pylint](https://pylint.readthedocs.io/)
- GitHub Actions workflows for CI/CD
- Automated changelog generation
- PyPI publishing with [trusted publishing](https://docs.pypi.org/trusted-publishers/) support

## Getting Started

### Using This Template

1. Click "Use this template" on GitHub to create a new repository
2. Clone your new repository
3. Update the template files with your project information

### Initial Setup

Install uv if not already installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Clone and setup your repository:
```bash
git clone <your-repo-url>
cd <your-repo-name>
uv sync --all-groups
```

### Configuration

#### Update `pyproject.toml`

Replace the following placeholders:
- `name = "foo"` - Your package name
- `authors` - Your name and email
- `description` - Your package description
- `Repository` - Your repository URL

#### Update `.github/workflows/release.yaml`

Replace `<foo>` in the PyPI URL with your package name:
```yaml
url: https://pypi.org/project/<foo>
```

#### Configure GitHub Repository

**PyPI Publishing Setup**

Choose one of the following methods:

Option A: API Token
1. Generate an API token on [PyPI](https://pypi.org/manage/account/token/)
2. Add it as a repository secret named `PYPI_API_TOKEN`

Option B: Trusted Publishing (Recommended)
1. Go to your [PyPI account settings](https://pypi.org/manage/account/publishing/)
2. Add a new trusted publisher:
   - Repository owner: your GitHub username/organization
   - Repository name: your repository name
   - Workflow name: `release.yaml`
   - Environment: `pypi`

## Development Workflow

### Making Changes

Create a feature branch from `develop`:
```bash
git checkout -b feat/your-feature
```

Make your changes following the existing code style and conventions.

Commit using [Conventional Commits](https://www.conventionalcommits.org/):
```bash
git add .
git commit -m "feat: add new feature"
```

Commit types:
- `feat:` New features (minor version bump)
- `fix:` Bug fixes (patch version bump)
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Maintenance tasks
- `perf:` Performance improvements
- `ci:` CI configuration changes

For breaking changes, add `BREAKING CHANGE:` in the commit body or use `!` after the type.

### Testing

Run tests locally:
```bash
make test
```

Format code:
```bash
make format
```

Check code formatting:
```bash
make format-check
```

Run linting:
```bash
make lint-check
```

### Release Process

1. Merge feature branches to `develop`
2. Navigate to Actions → "Release Module" workflow
3. Click "Run workflow" and select the `develop` branch
4. The workflow will:
   - Analyze commits to determine version bump
   - Update version in `pyproject.toml`
   - Generate changelog
   - Create GitHub release
   - Build package distributions
   - Publish to PyPI

## Project Structure

```
.
├── .github/
│   ├── actions/
│   │   └── setup/          # Reusable setup action
│   └── workflows/
│       └── release.yaml    # Release and publishing workflow
├── docs/
│   └── CHANGELOG.md       # Auto-generated changelog
├── src/
│   ├── <package_name>/    # Package source code
│   └── tests/             # Test files
├── pyproject.toml         # Project configuration
├── uv.lock               # Dependency lock file
└── README.md             # This file
```

## Troubleshooting

**Version Not Updating**
- Verify commits follow conventional commit format
- Ensure workflow runs from `develop` branch
- Check [python-semantic-release documentation](https://python-semantic-release.readthedocs.io/) for configuration options

**Build Failures**
- Run `uv sync` to ensure dependencies are installed
- Check `uv.lock` is committed to repository
- Verify Python version compatibility in `pyproject.toml`

For additional help, consult:
- [uv documentation](https://github.com/astral-sh/uv)
- [python-semantic-release documentation](https://python-semantic-release.readthedocs.io/)
- [PyPI packaging guide](https://packaging.python.org/)