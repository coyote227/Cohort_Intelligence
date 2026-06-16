import random
import math

def generate_values(given_ranges):
    matrix = []

    for candidate_range in given_ranges:

        row = []

        for low, high in candidate_range:
            row.append(random.uniform(low, high))

        matrix.append(row)

    return matrix


def reduce_range(reduction_factor, current_range):
    return reduction_factor * current_range


def evaluate_population(values, objective):
    return [objective(*v) for v in values]

# *v in Python is called the unpacking operator (or “splat operator”).
# It means:
# “Take the elements inside v and pass them as separate arguments.”
   

def roulette_selection(
        values,
        fitness,
        given_ranges,
        range_width,
        lower_bounds,
        upper_bounds):

    eps = 1e-6  #to avoid division by 0

    fmin = min(fitness)
    
    spread = max(fitness) - min(fitness)

    if spread > 0:
        alpha = 10 / spread
    else:
        alpha = 1

    weights = [
        1 / (1 + alpha * (f - fmin))
        for f in fitness
    ]
    
    # fmin = min(fitness)

    # shifted = [f - fmin for f in fitness]
    # weights = [1 / (1 + f) for f in shifted]
    
    # shifted = [f - fmin + 1e-6 for f in fitness]
    # weights = [1 / f for f in shifted]

    
    total_weight = sum(weights)

    cumulative = []

    s = 0

    for w in weights:
        s += w / total_weight
        cumulative.append(s)

    new_values = [None] * len(values)

    for i in range(len(values)):

        r = random.uniform(0, 1)

        for j in range(len(values)):
            if r < cumulative[j]:
                new_values[i] = values[j][:]
                break

    # shrink ranges
    for i in range(len(values)):

        for j in range(len(range_width)):

            lo = new_values[i][j] - range_width[j] / 2
            hi = new_values[i][j] + range_width[j] / 2

            lo = max(lo, lower_bounds[j])
            hi = min(hi, upper_bounds[j])

            lo = max(lo, given_ranges[i][j][0])
            hi = min(hi, given_ranges[i][j][1])

            if lo < hi:
                given_ranges[i][j][0] = lo
                given_ranges[i][j][1] = hi

    return new_values


def CI(
        objective,
        candidates,
        iterations,
        reduction_factor,
        lower_bounds,
        upper_bounds,
        initial_ranges):

    #initialisation of ranges 
    given_ranges = [
        [[r[0], r[1]] for r in initial_ranges]
        for _ in range(candidates)
    ]

    #initalisation of range width for reduction 
    range_width = [
        r[1] - r[0]
        for r in initial_ranges
    ]

    #saves function and candidate values respectively
    history = []
    population_history = []

    
    for _ in range(iterations):

        # randomly generate values from given_ranges and save them
        values = generate_values(given_ranges)
        population_history.append([v[:] for v in values])

        # evaluate function values and save them
        fitness = evaluate_population(values, objective)
        history.append(fitness[:])

        # roulette wheel and candidate selection
        values = roulette_selection(
            values,
            fitness,
            given_ranges,
            range_width,
            lower_bounds,
            upper_bounds
        )

        # reduce range width for the next iteration
        for j in range(len(range_width)):
            range_width[j] *= reduction_factor


    return history, population_history
    
    
def check_constraints(population_history, lower_bounds, upper_bounds):
    violations = 0

    for iteration in population_history:
        for candidate in iteration:
            for j, x in enumerate(candidate):

                if x < lower_bounds[j] or x > upper_bounds[j]:
                    violations += 1
                    print(f"Violation: x{j+1} = {x}")

    if violations == 0:
        print("\nAll constraints satisfied!")
    else:
        print(f"\nTotal violations: {violations}")

