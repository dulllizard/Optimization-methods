"""
Метод Фибоначчи
"""

def task_function(x: float) -> float:
    """
    Функция из предложенного варианта задания
    :param x: Значение соответствующее оси абсцисс
    :return: Значение y
    """
    return (x + 1) ** 2 - 7 * x + 6


def get_fibonacci_sequence(sequence: list, n: int) -> None:
    """
    Пополнение последовательности Фибоначчи
    :param sequence: Последовательность Фибонначи
    :param n: Значение n-индекса последовательности
    """
    sequence.append(sequence[n - 1] + sequence[n - 2])


def fibonacci_search(a: int, b: int, l: float, epsilon: float, target_function: callable) -> float:
    """
    Метод Фибоначчи для поиска безусловного экстремума
    :param a: Начало интервала неопределенности
    :param b: Конец интервала неопределенности
    :param l: Шаг в интервале неопределенности
    :param epsilon: Параметр эпсилон
    :param target_function Целевая функция
    :return: Безусловный экстремум
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
