import pytest
import sys
import os

# Ensure repo root is on sys.path so `SRC` can be imported during pytest collection
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from SRC.app import add_two_numbers


def test_add_positive_integers():
    assert add_two_numbers(2, 3) == 5


def test_add_negative_integers():
    assert add_two_numbers(-2, -3) == -5


def test_add_mixed_signs():
    assert add_two_numbers(-2, 3) == 1


def test_add_floats():
    assert add_two_numbers(2.5, 1.25) == 3.75


def test_add_zero():
    assert add_two_numbers(0, 5) == 5
