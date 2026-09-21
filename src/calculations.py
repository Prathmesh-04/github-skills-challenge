# System Modules
import math

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    # Missing from coverage because tests do not pass a negative radius.
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    # Missing from coverage because tests do not pass a negative index.
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Missing from coverage because tests do not request n >= 2.
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
