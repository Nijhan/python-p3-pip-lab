# lib/testing_env/module_test.py

import sys
import requests
import pytest

# Functions to get versions
def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__

# Tests
def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor >= 8  # Accept Python 3.8 or newer

def test_requests_version():
    assert requests_version() == "2.31.0"  # Update to your installed requests version

def test_pytest_version():
    assert pytest_version() == "7.4.4"  # Update to your installed pytest version
