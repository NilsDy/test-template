import argparse
from test_template.fibonacci import Fibonacci


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m test_template` and `$ test_template `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(description="Fibonacci computation")
    parser.add_argument("n", type=int, help="An integer input")

    args = parser.parse_args()

    f = Fibonacci()
    print("Fibonacci result = ", f.fib(args.n))
