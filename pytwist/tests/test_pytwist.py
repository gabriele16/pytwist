"""
Unit and regression test for the pytwist package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import pytwist


def test_pytwist_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "pytwist" in sys.modules
