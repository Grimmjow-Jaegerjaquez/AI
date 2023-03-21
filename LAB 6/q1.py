import random
import math

def f(x):
    return -1 * (x) ** 2 + 5 * x + 10

def hill_climbing(f, x_min, x_max, max_iterations=1000, step_size=0.1):
   
    current_state = random.uniform(x_min, x_max)

    
    for i in range(max_iterations):
        
        current_value = f(current_state)

        neighbor_state = current_state + random.uniform(-step_size, step_size)

        neighbor_state = max(min(neighbor_state, x_max), x_min)

        neighbor_value = f(neighbor_state)

        if neighbor_value > current_value:
            current_state = neighbor_state

    return current_state


x_max = 10
x_min = -10
max_x = hill_climbing(f, x_min, x_max)

print("Maximum value of f(x) is:", f(max_x), "at x =", max_x)
