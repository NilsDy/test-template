class Fibonacci:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1

        if n <= 0:
            raise ValueError(f"n <= 0 is not allowed. You provided {n}.")

        if n not in self.mem:
            self.mem[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.mem[n]
