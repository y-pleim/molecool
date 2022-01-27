"""
Unit and regression test for the molecool2 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import molecool2


def test_molecool2_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molecool2" in sys.modules
