import time
import random

def hello_world():
    print("Hello, World!")


def fibonacci(n):
    """
    Generate the nth Fibonacci number.

    Parameters:
    n (int): The position in the Fibonacci sequence (n >= 0)

    Returns:
    int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Call the function
hello_world()
# Example usage:
fibonacci_pos = random.randint(1, 100)
print("The {}th Fibonacci number is {}!".format(fibonacci_pos, fibonacci(fibonacci_pos)))  # Output: 55

