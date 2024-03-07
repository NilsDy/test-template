import pytest
from test_template import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from test_template import Fibonacci
    except ImportError:
        assert False


def test_edge_cases():
    fib = Fibonacci()

    for n in [1, 2]:
        assert fib.fib(n) == 1


def test_error():
    fib = Fibonacci()

    for n in [0, -1, -2]:
        try:
            fib.fib(n)
            assert False
        except ValueError:
            assert True

def test_regular():
    fib = Fibonacci()

    for n, r in [(3, 2), (4,3), (5,5), (7,13)]:
        assert fib.fib(n) == r