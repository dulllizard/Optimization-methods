"""
Fibonacci Search Algorithm
"""

def task_function(x: float) -> float:
    """
    Example function for finding minimum

    Args:
        x: The value corresponding to the abscissa axis

    Returns:
        float: The value corresponding to the ordinate axis
    """
    return (x + 1) ** 2 - 7 * x + 6


def get_fibonacci_sequence(sequence: list, n: int) -> None:
    """
    Fibonacci Sequence Replenishment

    Args:
        sequence: Fibonacci sequence
        n: Sequence n-index value
    """
    sequence.append(sequence[n - 1] + sequence[n - 2])


def fibonacci_search(a: int, b: int, l: float, epsilon: float, target_function: callable) -> float:
    """
    Fibonacci method for finding an unconditional extremum

    Args:
        a: Beginning of the uncertainty interval
        b: End of uncertainty interval
        l: Step in the uncertainty interval
        epsilon: Parameter epsilon
        target_function: function for finding minimum

    Returns:
        float: Unconditional extremum
    """
    fibonacci_sequence = [1, 1]
    n = 1
    k = 0
    while (b - a) / l > fibonacci_sequence[n]:
        n += 1
        get_fibonacci_sequence(fibonacci_sequence, n)

    y = a + fibonacci_sequence[n - 2] / fibonacci_sequence[n] * (b - a)
    z = a + fibonacci_sequence[n - 1] / fibonacci_sequence[n] * (b - a)

    while k != n - 2:
        if target_function(y) <= target_function(z):
            b = z
            z = y
            y = a + fibonacci_sequence[n - k - 3] / fibonacci_sequence[n - k - 1] * (b - a)
        else:
            a = y
            y = z
            z = a + fibonacci_sequence[n - k - 2] / fibonacci_sequence[n - k - 1] * (b - a)

        k += 1
    y = z
    z = y + epsilon

    if target_function(y) <= target_function(z):
        b = z
    else:
        a = y

    return (a + b) / 2
