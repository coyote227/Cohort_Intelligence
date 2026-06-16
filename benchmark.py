#sphere function 
def sphere(x1, x2, x3):
    return x1**2 + x2**2 + x3**2


SPHERE = {
    "name": "Sphere",
    "function": sphere,
    "lower_bounds": [-5.12, -5.12,-5.12],
    "upper_bounds": [5.12, 5.12,5,12],
    "global_minimum": 0.0,
    "global_argmin": [0, 0, 0]
}

#rosenbrock 

def rosenbrock(x1, x2):
    return (1 - x1)**2 + 100 * (x2 - x1**2)**2

ROSENBROCK = {
    "name": "Rosenbrock",
    "function": rosenbrock,
    "lower_bounds": [-5, -5],
    "upper_bounds": [10, 10],
    "global_minimum": 0,
    "global_argmin": [1, 1]
}

#G6 kyoto

def g6(x1, x2):

    return (x1 - 10)**3 + (x2 - 20)**3


def g6_constrained(x1, x2):

    obj = g6(x1, x2)

    g1 = (x1 - 5)**2 + (x2 - 5)**2 - 100
    g2 = 82.81 - ((x1 - 5)**2 + (x2 - 5)**2)

    penalty = max(0, g1)**2 + max(0, g2)**2

    return obj + 1e6 * penalty


G6 = {
    "name": "G6",
    "function": g6_constrained,
    "lower_bounds": [13, 0],
    "upper_bounds": [100, 100],
    "global_minimum": -6961.81388,
    "global_argmin": [14.095, 0.84296]
}