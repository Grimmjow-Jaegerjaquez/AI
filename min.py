import random

def f(x):
    x ** 3 + (-1) * 4 * x ** 2 + 3 * x + 1

def hcs():
    x = random.uniform(-10, 10)
    dx = 0.01
    max_iterations = 1000
    iteration = 0

    while iteration < max_iterations:
        iteration += 1
        fx = f(x)
        fx_dx_minus = f(x - dx)
        fx_dx_plus = f(x + dx)
        if fx_dx_minus < fx:
            x -= dx
        elif fx_dx_plus < fx:
            x += dx
        else:
            break
    return x

fx_min = hcs()
print(f'The minimum value of f(x) is {f(x_min)} at x = {x_min}')