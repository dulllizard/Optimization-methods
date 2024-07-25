import time


def target_function_1(x1: float, x2: float) -> float:
    """
    Функция из предложенного варианта задания
    :param x1: Значение соответствующее горизонтальной оси
    :param x2: Значение соответствующее вертикальной оси
    :return: Значение функции
    """
    return (x1 - 1) ** 2 + (x2 + x1) ** 2


def target_function_2(x1, x2):
    return 4 * (x1 - 5) ** 2 + (x2 - 6) ** 2


def target_function_3(x1, x2):
    return 2 * x1 ** 2 + x1 * x2 + x2 ** 2


def util_search(f: callable, y: list, delta: list) -> list:
    """
    Исследующий поиск
    :param f: Функция
    :param y: Базис
    :param delta: Приращение
    :return: Новый базис
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
    Поиск по образцу
    :param x: Прошлый базис
    :param y: Нынешний базис
    :param lmbda: Ускоряющий множитель
    :return: Новый базис
    """
    y = [y[0] + lmbda * (y[0] - x[0]), y[1] + lmbda * (y[1] - x[1])]
    return y


def hook_jeeves_method(f: callable, x0: list, delta: list, epsilon: float, lmbda: float, alpha: int) -> list:
    """
    Метод конфигураций (метод Хука — Дживса [R. Hooke, T. A. Jeeves])
    :param f: Функция
    :param x0: Начальная точка
    :param delta: Приращение
    :param epsilon: число > 0 для остановки алгоритма
    :param lmbda: Ускоряющий множитель
    :param alpha: Коэффициент уменьшения шага
    :return: Координаты минимума функции
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


# print(hook_jeeves_method(target_function_2, [8, 9], [1, 2], 0.3, 1, 2))
start = time.time()
print(hook_jeeves_method(target_function_1, [9, 8], [1, 2], 0.1, 1, 2))
end = time.time()
print(end - start)
# print(hook_jeeves_method(target_function_3, [0.5, 1], [0.2, 0.4], 0.1, 1.5, 4))

# print(target_function_2(3, 3))
# print(target_function_2(4, 3))
# print(target_function_2(4, 5))
# print(target_function_2(4, 3))
