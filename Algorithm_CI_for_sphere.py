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
   
def solveSphere(values):
    funcValues.clear()
    for i in range(candidates):
        funcValues.append(values[i][0]**2 + values[i][1]**2)
    funcValues_all.append(funcValues[:])
    

def calcProb(values):
    probsum = sum(1 / (f + 1e-12) for f in funcValues)
    probs = []
    cumulative = 0

    for f in funcValues:
        cumulative += (1 / (f + 1e-12)) / probsum
        probs.append(cumulative)
    
    new_values = [None] * candidates
    
    for i in range(candidates):

        c = random.uniform(0, 1)

        for j in range(candidates):
            if c < probs[j]:
                new_values[i] = values[j]
                break
    
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
    return new_values
    
    
# main       
candidates = int(input("enter number of candidates : "))
reductionFactor = float(input("enter reduction factor : "))

given_ranges = []
ranges = 10.24

funcValues = []
funcValues_all = []

for i in range(candidates):
    given_ranges.append([[-5.12, 5.12], [-5.12, 5.12]])

for i in range(500):
    values = generate_values(given_ranges)
    print("candidate x1 x2")
    print(values,"\n\n")
    #display(values)
    #print("\n\n")
    solveSphere(values)
    values = calcProb(values)
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