import numpy

def plus(a: float, b: float):
    return a + b

def minus(a: float, b: float):
    return a - b

def multi(a: float, b: float):
    return a * b

def division(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError
    return a / b

all_funcs = [plus, division, minus, multi]
calcs_data = [(1, 2, 3), (1, 2, 0.5), (3, 4, -1), (5, 2, 10)]

for method, data in zip(all_funcs, calcs_data):
    a, b, result = data
    print(method.__name__, a, b, result)