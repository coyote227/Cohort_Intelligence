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

#ackley
import math

def ackley(x1, x2):
    a = 20
    b = 0.2
    c = 2 * math.pi

    s1 = x1**2 + x2**2
    s2 = math.cos(c * x1) + math.cos(c * x2)

    return -a * math.exp(-b * math.sqrt(s1 / 2)) - math.exp(s2 / 2) + a + math.e


ACKLEY = {
    "name": "Ackley",
    "function": ackley,
    "lower_bounds": [-32.768, -32.768],
    "upper_bounds": [32.768, 32.768],
    "global_minimum": 0,
    "global_argmin": [0, 0]
}

#G6 kyoto

def g6(x1, x2):

    return (x1 - 10)**3 + (x2 - 20)**3


def g6_constrained(x1, x2):

    obj = g6(x1, x2)

    g1 = (x1 - 5)**2 + (x2 - 5)**2 - 100
    g2 = 82.81 - ((x1 - 5)**2 + (x2 - 5)**2)

    penalty = max(0, g1)**2 + max(0, g2)**2

    return obj + 1e4 * penalty
    


G6 = {
    "name": "G6",
    "function": g6_constrained,
    "lower_bounds": [13, 0],
    "upper_bounds": [100, 100],
    "global_minimum": -6961.81388,
    "global_argmin": [14.095, 0.84296]
}

def g11(x1, x2):
    return x1**2 + (x2 - 1)**2


def g11_constrained(x1, x2):

    obj = g11(x1, x2)

    g1 = abs(x2 - x1**2) - 1e-4

    g2 = -x1 - 1
    g3 = -x2 - 1

    g4 = x1 - 1
    g5 = x2 - 1

    penalty = (
        max(0, g1)**2 +
        max(0, g2)**2 +
        max(0, g3)**2 +
        max(0, g4)**2 +
        max(0, g5)**2
    )

    return obj + 1e5 * penalty


G11 = {
    "name": "G11",
    "function": g11_constrained,
    "lower_bounds": [-1, -1],
    "upper_bounds": [1, 1],
    "global_minimum": 0.75,
    "global_argmin": [-(0.5**0.5), 0.5]
}

def g12_constrained(x1, x2, x3):
    objective = -(1 - 0.01 * (
        (x1 - 5)**2 +
        (x2 - 5)**2 +
        (x3 - 5)**2
    ))

    min_constraint = float('inf')

    for p in range(1, 10):
        for q in range(1, 10):
            for r in range(1, 10):
                g = (
                    (x1 - p)**2 +
                    (x2 - q)**2 +
                    (x3 - r)**2 -
                    0.0625
                )
                min_constraint = min(min_constraint, g)

    penalty = 1e4 * max(0, min_constraint)**2

    return objective + penalty


G12 = {
    "name": "G12",
    "function": g12_constrained,
    "lower_bounds": [0, 0, 0],
    "upper_bounds": [10, 10, 10],
    "global_minimum": -1.0,
    "global_argmin": [5.0, 5.0, 5.0]
}