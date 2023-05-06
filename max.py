import math
import random

def f(x):
    return -1 * x ** 2 + 5 * x + 10

def hcs(f, x_min, x_max, max_iteration = 1000, step_size = 0.1):
    curr_state = random.uniform(x_min, x_max)
    for i in range(max_iteration):
        curr_value = f(curr_state)
        neighbor_state = curr_state + random.uniform(-step_size, step_size)
        neighbor_state = max(min(neighbor_state, x_max), x_min)
        neighbor_value = f(neighbor_state)
        if neighbor_value > curr_value:
            curr_state = neighbor_state
    return curr_state

x_max = 10
x_min = -10
max_x = hcs(f, x_min, x_max)
print("Maximum value of f(x) : ", f(max_x), " at x = ", max_x)