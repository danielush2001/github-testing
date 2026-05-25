from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from app import add_two_numbers

def test_add_positive_integers():
    assert add_two_numbers(2, 3) == 5

def test_add_negative_integers():
    assert add_two_numbers(-4, -6) == -10

def test_add_mixed_sign_integers():
    assert add_two_numbers(-4, 10) == 6

def test_add_with_zero():
    assert add_two_numbers(0, 7) == 7

def test_add_floats():
    assert add_two_numbers(2.5, 3.1) == 5.6
