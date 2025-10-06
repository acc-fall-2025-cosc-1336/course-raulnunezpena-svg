

def get_factorial(n: int) -> int:
    """
    Return n! computed with a for-range loop.
    Raises ValueError if n < 0 or not an int.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sum_odd_numbers(n: int) -> int:
    """
    Return the sum of odd integers from 1 up to and including n (if n is odd),
    using a while loop. Raises ValueError if n < 1 or not an int.
    Example: n=7 -> 1+3+5+7 = 16; n=6 -> 1+3+5 = 9.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 1:
        raise ValueError("n must be >= 1")

    total = 0
    current = 1
    while current <= n:
        total += current
        current += 2
    return total
