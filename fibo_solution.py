# Fibonacci numbers module

def fib(n):
    """
    Write the Fibonacci series up to n.
    
    Args:
        n: Any numeric.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """
    Return the Fibonacci series up to n.

    Args:
        n: Any numeric.

    Returns:
        list: A list representation of the Fibonacci series up to n.
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
