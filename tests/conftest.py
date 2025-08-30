"""
Pytest configuration for notebook testing.

This file sets up fixtures and configurations needed for testing notebooks.
"""
import os
import sys
from pathlib import Path

import pytest

# Add the parent directory to the path so we can import modules from the root
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

# Define fixtures that can be reused in tests

@pytest.fixture(scope="session")
def repo_root():
    """Return the root directory of the repository."""
    return root_dir

@pytest.fixture(scope="session")
def notebooks_dir():
    """Return the directory containing notebooks."""
    return root_dir / "notebooks"
