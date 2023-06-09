"""Tests for the utils module."""
import pytest

from .. import utils


def test_slugify():
    """Test for the slugify function."""
    assert utils.slugify("This is a test-test!") == "this_is_a_test_test"


def test_get_filename():
    """Test for the get_filename function."""
    assert utils.get_filename("/var/log/test.txt") == "test"
