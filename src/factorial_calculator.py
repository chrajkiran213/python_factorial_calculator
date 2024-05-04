def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input cannot be negative")
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
