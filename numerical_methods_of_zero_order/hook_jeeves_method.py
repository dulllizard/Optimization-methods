"""
Hook Jeeves Method.
"""

def target_function_1(x1: float, x2: float) -> float:
    """
    Example function for finding minimum

    Args:
        x1: The value corresponding to the first abscissa axis.
        x2: The value corresponding to the second abscissa axis.

    Returns:
        float: The value corresponding to the ordinate axis
    """
    return (x1 - 1) ** 2 + (x2 + x1) ** 2


def target_function_2(x1: float, x2: float) -> float:
    """
    Example function for finding minimum.

    Args:
        x1: The value corresponding to the first abscissa axis.
        x2: The value corresponding to the second abscissa axis.

    Returns:
        float: The value corresponding to the ordinate axis.
    """
    return 4 * (x1 - 5) ** 2 + (x2 - 6) ** 2


def target_function_3(x1: float, x2: float) -> float:
    """
    Example function for finding minimum.

    Args:
        x1: The value corresponding to the first abscissa axis.
        x2: The value corresponding to the second abscissa axis.

    Returns:
        float: The value corresponding to the ordinate axis.
    """
    return 2 * x1 ** 2 + x1 * x2 + x2 ** 2


def util_search(f: callable, y: list, delta: list) -> list:
    """
    Research searching.

    Args:
        f: Function for finding minimum.
        y: Basis.
        delta: Increment.

    Returns:
        list: New basis.
    """
    fy = f(*y)
    if f(*(y[0] + delta[0], y[1])) < fy:
        y[0] = y[0] + delta[0]
        fy = f(*(y[0], y[1]))
    if f(*(y[0], y[1] + delta[0])) < fy:
        y[1] = y[1] + delta[1]
        fy = f(*(y[0], y[1]))
    if f(*(y[0] - delta[0], y[1])) < fy:
        y[0] = y[0] - delta[0]
        fy = f(*(y[0], y[1]))
    if f(*(y[0], y[1] - delta[1])) < fy:
        y[1] = y[1] - delta[1]
    return y


def sample_search(x: list, y: list, lmbda: float) -> list:
    """
    Searching by sample.

    Args:
        x: Old basis.
        y: Current basis.
        lmbda: Acceleration multiplier.

    Returns:
        list: New basis.
    """
    y = [y[0] + lmbda * (y[0] - x[0]), y[1] + lmbda * (y[1] - x[1])]
    return y


def hook_jeeves_method(f: callable, x0: list, delta: list, epsilon: float, lmbda: float, alpha: int) -> list:
    """
    Method of configurations (Hooke-Jeeves method [R. Hooke, T. A. Jeeves]).

    Args:
        f: Function for finding minimum.
        x0:  Starting point.
        delta: Increment.
        epsilon: Number greater than 0 to stop the algorithm.
        lmbda: Acceleration multiplier.
        alpha: Step reduction factor.

    Returns:
        list: Coordinates of the minimum function.
    """
    y = x0.copy()
    x = x0.copy()

    y = util_search(f, y, delta)
    while not (delta[0] <= epsilon and delta[1] <= epsilon):

        fy = f(*y)

        if fy < f(*x):
            temp_x = x
            x = y
            y = sample_search(temp_x, y, lmbda)
            y = util_search(f, y, delta)

        else:
            if delta[0] > epsilon:
                delta[0] = delta[0] / alpha
            if delta[1] > epsilon:
                delta[1] = delta[1] / alpha
            y = x
            y = util_search(f, y, delta)

    return y
