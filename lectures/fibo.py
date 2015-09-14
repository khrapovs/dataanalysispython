"""
Fibonacci numbers module

"""

def fib(n):
    """write Fibonacci series up to n"""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    """return Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


if __name__ == '__main__':

    # These instructions are perfromed only if the module is run as a script,
    # like
    # > python fibo.py
    print(fib2(10))
