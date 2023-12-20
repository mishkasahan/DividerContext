from contextlib import contextmanager


@contextmanager
def divider_context(symbol):
    print(symbol)
    yield
    print(symbol)


with divider_context("my_symbol1") as manager:
    for i in range(5):
        print(i * i)

print(100 * "*")


class DividerContext:
    def __init__(self, symbol):
        self.symbol = symbol

    def __enter__(self):
        print(self.symbol)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.symbol)


with DividerContext("my_symbol2") as manager:
    for i in range(5):
        print(i * i)
