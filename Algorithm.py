import random
import matplotlib.pyplot as plt


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
   
def solveRosenbrock(values):

    funcValues.clear()

    for i in range(candidates):

        x = values[i][0]
        y = values[i][1]

        value = 100 * (x**2 - y)**2 + (x - 1)**2

        funcValues.append(value)

    funcValues_all.append(funcValues[:])
    

def calcProb(values):
    probsum = (1/funcValues[0]) + (1/funcValues[1]) + (1/funcValues[2])
    p1 = (1/funcValues[0]) / probsum
    p2 = (1/funcValues[1]) / probsum + p1
    p3 = (1/funcValues[2]) / probsum + p2
    
    new_values = [None] * candidates
    
    for i in range(candidates):
        c = random.uniform(0, 1)
        if c < p1:
            new_values[i] = values[0]
        elif c < p2:
            new_values[i] = values[1]
        else:
            new_values[i] = values[2]
    
    for i in range(candidates):
        for j in range(2):
            lo = new_values[i][j] - ranges / 2
            hi = new_values[i][j] + ranges / 2
            
            lo = max(lo, given_ranges[i][j][0])  
            hi = min(hi, given_ranges[i][j][1]) 
            
            if lo < hi:  
                given_ranges[i][j][0] = lo
                given_ranges[i][j][1] = hi
            new_values[i][j] = max(given_ranges[i][j][0],
                                   min(new_values[i][j], given_ranges[i][j][1]))

# main       
candidates = int(input("enter number of candidates : "))
reductionFactor = float(input("enter reduction factor : "))

given_ranges = []
ranges = 10.24

funcValues = []
funcValues_all = []

for i in range(candidates):
    given_ranges.append([[-5, 10], [-5, 10]])

for i in range(100):
    values = generate_values(given_ranges)
    print("candidate x1 x2")
    print(values,"\n\n")
    #display(values)
    #print("\n\n")
    solveRosenbrock(values)
    calcProb(values)
    ranges = redRange(reductionFactor, ranges)

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