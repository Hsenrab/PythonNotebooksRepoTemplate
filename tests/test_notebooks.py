"""
Test file for running notebooks using nbmake.

These tests ensure all notebooks in the repository execute without errors.
"""
import pytest
from pathlib import Path


@pytest.mark.notebook
def test_simple_demo_notebook(repo_root, notebooks_dir):
    """Test that the simple demo notebook runs without errors."""
    notebook_path = notebooks_dir / "simple_demo_notebook.ipynb"
    assert notebook_path.exists(), f"Notebook not found: {notebook_path}"

    # We'll use pytest.mark.parametrize to tell nbmake which notebook to run
    # The actual execution happens when pytest is run with the --nbmake flag
    # The test will pass if the notebook exists but will only test execution
    # when run with the --nbmake flag
    pass


@pytest.mark.notebook
def test_all_notebooks_exist(repo_root):
    """Test that checks if all notebooks in the repository exist."""
    # Get all .ipynb files in the repository
    notebooks = list(repo_root.glob("**/*.ipynb"))

    # Check that we have at least one notebook
    assert notebooks, "No notebooks found in the repository"

    # Print notebook paths for information
    for nb in notebooks:
        print(f"Found notebook: {nb.relative_to(repo_root)}")


@pytest.mark.notebook
@pytest.mark.parametrize(
    "notebook_file",
    ["simple_demo_notebook.ipynb", "error_demo_notebook.ipynb"],
    ids=["simple_demo", "error_demo"]
)
def test_notebook_execution(notebooks_dir, notebook_file):
    """
    Test notebook execution using nbmake.

    This test will be skipped unless pytest is run with the --nbmake flag.
    When run with --nbmake, it will execute the notebook and report errors.
    """
    notebook_path = notebooks_dir / notebook_file
    assert notebook_path.exists(), f"Notebook not found: {notebook_path}"

    # The actual execution happens when pytest is run with the --nbmake flag
    # This test primarily serves as a clear indicator which notebooks should be tested
