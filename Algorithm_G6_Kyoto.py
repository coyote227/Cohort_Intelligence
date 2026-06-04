import random
import matplotlib.pyplot as plt

LOWER_BOUNDS = [13, 0]
UPPER_BOUNDS = [100, 100]

def generate_values(given_ranges): 
    matrix = [] 
    for i in range(len(given_ranges)):
        row = []
        for j in range(2):
            low = given_ranges[i][j][0]
            high = given_ranges[i][j][1]
            value = random.uniform(low, high)
            value = max(low, min(value, high))
            row.append(value)
        matrix.append(row)
    return matrix
    
def display(values):
    for i, row in enumerate(values):
        print(f"{i+1}: {row}")
        
def redRange(reductionFactor, ranges):
    return reductionFactor * ranges
   
def solveG6(values):
    
    funcValues.clear()
    for i in range(candidates):
        funcValues.append(constrained(values[i][0],values[i][1],10**3))
    funcValues_all.append(funcValues[:])
    
    
def constrained(x1,x2,pcoeff):
        
        funcg1 = (x1 - 10)**3 + (x2 - 20)**3
        
        g1 = (x1-5)**2 + (x2-5)**2 - 100
        g2 = 82.81 - ((x1-5)**2 + (x2-5)**2)
        
        penalty = max(0, g1)**2 + max(0, g2)**2
        
        penalised = funcg1 + pcoeff * penalty
        
        return penalised

def calcProb(values):

    eps = 1e-6

    # Shift fitness values so all are positive
    fmin = min(funcValues)
    shiftedFitness = []

    for f in funcValues:
        shiftedFitness.append(f - fmin + eps)

    # Since this is a minimization problem,
    # smaller fitness -> larger selection weight
    weights = []

    for f in shiftedFitness:
        weights.append(1 / f)

    probsum = sum(weights)

    probs = []
    cumulative = 0

    for w in weights:
        cumulative += w / probsum
        probs.append(cumulative)

    # Roulette-wheel selection
    new_values = [None] * candidates

    for i in range(candidates):

        c = random.uniform(0, 1)

        for j in range(candidates):
            if c < probs[j]:
                new_values[i] = values[j][:]
                break

    # Shrink search ranges around selected candidates
    for i in range(candidates):
        for j in range(2):

            lo = new_values[i][j] - variable_ranges[j] / 2
            hi = new_values[i][j] + variable_ranges[j] / 2

            lo = max(lo, LOWER_BOUNDS[j])
            hi = min(hi, UPPER_BOUNDS[j])

            lo = max(lo, given_ranges[i][j][0])
            hi = min(hi, given_ranges[i][j][1])

            if lo < hi:
                given_ranges[i][j][0] = lo
                given_ranges[i][j][1] = hi

            new_values[i][j] = max(
                given_ranges[i][j][0],
                min(new_values[i][j], given_ranges[i][j][1])
            )

    return new_values

    for i in range(candidates):
        for j in range(2):
            lo = new_values[i][j] - variable_ranges[j] / 2
            hi = new_values[i][j] + variable_ranges[j] / 2
            
            lo = max(lo, LOWER_BOUNDS[j])
            hi = min(hi, UPPER_BOUNDS[j])

            lo = max(lo, given_ranges[i][j][0])
            hi = min(hi, given_ranges[i][j][1])   
            
            if lo < hi:  
                given_ranges[i][j][0] = lo
                given_ranges[i][j][1] = hi
            new_values[i][j] = max(given_ranges[i][j][0],
                                   min(new_values[i][j], given_ranges[i][j][1]))
    return new_values
    
    
# main       
candidates = int(input("enter number of candidates : "))
reductionFactor = float(input("enter reduction factor : "))

given_ranges = [[[13,100],[0,100]] for _ in range(candidates)]

variable_ranges = [
    given_ranges[0][0][1] - given_ranges[0][0][0],  
    given_ranges[0][1][1] - given_ranges[0][1][0]   
]

funcValues = []
funcValues_all = []

for i in range(500):
    values = generate_values(given_ranges)
    print(f"Iteration {i+1} - candidate x1 x2")
    print(values,"\n\n")
    #display(values)
    #print("\n\n")
    solveG6(values)
    values = calcProb(values)
    for j in range(len(variable_ranges)):
        variable_ranges[j] = max(1e-6,redRange(reductionFactor, variable_ranges[j])
    )

for i in range(len(funcValues_all)):
    print(funcValues_all[i])
    
for c in range(candidates):
    candidate_fitness = [funcValues_all[i][c] for i in range(len(funcValues_all))]
    plt.plot(range(1, len(funcValues_all) + 1), candidate_fitness)

plt.title("CI — Fitness of Each Candidate per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Fitness f(x, y)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()