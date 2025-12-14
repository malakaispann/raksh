import shutil

def copy_files(**kwargs):
    """Copy README and CONTRIBUTING to docs."""
    shutil.copy2("README.md", "docs/index.md")
    shutil.copy2("CONTRIBUTING.md", "docs/contributing.md")