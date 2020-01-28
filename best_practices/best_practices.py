import numpy as np

print(np.ones([2, 2]))

def fib(n: int) -> int:
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
