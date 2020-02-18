"""
Unit and regression test for the rc_learn package.
"""

# Import package, test suite, and other packages as needed
import rc_learn
import pytest
import sys

def test_rc_learn_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "rc_learn" in sys.modules
