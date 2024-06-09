"""
метод Пауэлла
"""

def target_function(x: float) -> float:
    """
    Функция из предложенного варианта задания
    :param x: Значение соответствующее оси абсцисс
    :return: Значение y
    """
    return (x + 1) ** 2 - 7 * x + 6


def get_function_values(x1: float, delta: float) -> tuple:
    """
    Получение значений функций f1, f2, f3 и их координаты x
    :param x1: Начальная точка
    :param delta: Величина шага
    :return: Значения функций f1, f2, f3 и их координаты x
    """
    x2 = x1 + delta

    f1 = target_function(x1)
    f2 = target_function(x2)

    if f1 > f2:
        x3 = x1 + 2 * delta
    else:
        x3 = x1 - delta

    f3 = target_function(x3)

    return [f1, f2, f3], [x1, x2, x3]


def get_minimum(function_values: tuple) -> tuple:
    """
    Получение минимальных значений
    :param function_values: Значения функций f1, f2, f3 и их координаты x
    :return: Минимальные значения
    """
    x1, x2, x3 = function_values[1]
    f1, f2, f3 = function_values[0]
    function_min = min(function_values[0])
    x_min = function_values[1][function_values[0].index(function_min)]

    polinom_min_x = ((x2 ** 2 - x3 ** 2) * f1 + (x3 ** 2 - x1 ** 2) * f2 +
                     (x1 ** 2 - x2 ** 2) * f3) / (2 * ((x2 - x3) * f1 +
                                                       (x3 - x1) * f2 + (
                                                               x1 - x2) * f3))

    polinom_min_f = target_function(polinom_min_x)

    return function_min, polinom_min_f, polinom_min_x, x_min


def powell_method(x1: float, delta: float, epsilon_1: float, epsilon_2: float) -> float:
    """
    Метод квадратичной интерполяции
    :param x1: Начальная точка
    :param delta: Величина шага
    :param epsilon_1: Малое положительное число, характеризующее точность
    :param epsilon_2: Малое положительное число, характеризующее точность
    :return: Глобальный минимум
    """
    function_values = get_function_values(x1, delta)
    x1, x2, x3 = function_values[1]
    function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(function_values)

    while not (abs((function_min - polinom_min_f) / polinom_min_f) < epsilon_1 and abs(
            (x_min - polinom_min_x) / polinom_min_x) < epsilon_2):
        if polinom_min_x == 0:
            x1 = x_min
            function_values = get_function_values(x1, delta)
            function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(function_values)

        elif x1 <= polinom_min_x <= x3:
            if polinom_min_f < target_function(x_min):
                x1, x2, x3 = sorted([x1, x2, x3, polinom_min_x])[0:3]
            else:
                x1, x2, x3 = sorted([x1, x2, x3, x_min])[0:3]
            f1 = target_function(x1)
            f2 = target_function(x2)
            f3 = target_function(x3)
            function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(([f1, f2, f3], [x1, x2, x3]))
        else:
            x1 = polinom_min_x
            function_values = get_function_values(x1, delta)
            function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(function_values)

    return polinom_min_x


def get_amount_operations_powell_method(x1: float, delta: float, epsilon_1: float, epsilon_2: float) -> int:
    """
    Метод квадратичной интерполяции
    :param x1: Начальная точка
    :param delta: Величина шага
    :param epsilon_1: Малое положительное число, характеризующее точность
    :param epsilon_2: Малое положительное число, характеризующее точность
    :return: Глобальный минимум
    """
    counter = 6
    function_values = get_function_values(x1, delta)
    x1, x2, x3 = function_values[1]
    function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(function_values)

    while not (abs((function_min - polinom_min_f) / polinom_min_f) < epsilon_1 and abs(
            (x_min - polinom_min_x) / polinom_min_x) < epsilon_2):
        if polinom_min_x == 0:
            x1 = x_min
            function_values = get_function_values(x1, delta)
            function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(function_values)
            counter += 6

        elif x1 <= polinom_min_x <= x3:
            if polinom_min_f < target_function(x_min):
                x1, x2, x3 = sorted([x1, x2, x3, polinom_min_x])[0:3]
            else:
                x1, x2, x3 = sorted([x1, x2, x3, x_min])[0:3]
            f1 = target_function(x1)
            f2 = target_function(x2)
            f3 = target_function(x3)
            function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(([f1, f2, f3], [x1, x2, x3]))
            counter += 2
        else:
            x1 = polinom_min_x
            function_values = get_function_values(x1, delta)
            function_min, polinom_min_f, polinom_min_x, x_min = get_minimum(function_values)
            counter += 2

    return counter


print(get_amount_operations_powell_method(-60, 1000, 1000, 1000))
print(powell_method(-6, 10, 10, 10))