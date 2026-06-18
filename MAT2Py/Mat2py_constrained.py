import numpy as np


valid_problems = ['G1', 'G4', 'G6', 'G7', 'G9', 'G10', 'G12']

while True:
    problem = input(f"Select problem {valid_problems}: ").strip().upper()
    if problem in valid_problems:
        break
    print(f"  Invalid choice. Please enter one of {valid_problems}.")

runs = 1


if problem == 'G1':
    n = 13
    lb = np.array([0]*9 + [0, 0, 0, 0], dtype=float)
    ub = np.array([1]*9 + [100, 100, 100, 1], dtype=float)

    def objFun(x):
        return 5*np.sum(x[:4]) - 5*np.sum(x[:4]**2) - np.sum(x[4:13])

    def conFun(x):
        return np.array([
            2*x[0]+2*x[1]+x[9]+x[10]-10,
            2*x[0]+2*x[2]+x[9]+x[11]-10,
            2*x[1]+2*x[2]+x[10]+x[11]-10,
            -8*x[0]+x[9],
            -8*x[1]+x[10],
            -8*x[2]+x[11],
            -2*x[3]-x[4]+x[9],
            -2*x[5]-x[6]+x[10],
            -2*x[7]-x[8]+x[11]
        ])

    f_opt = -15.0

elif problem == 'G4':
    n = 5
    lb = np.array([78, 33, 27, 27, 27], dtype=float)
    ub = np.array([102, 45, 45, 45, 45], dtype=float)

    def objFun(x):
        return (5.3578547*x[2]**2
                + 0.8356891*x[0]*x[4]
                + 37.293239*x[0]
                - 40792.141)

    def conFun(x):
        u = 85.334407 + 0.0056858*x[1]*x[4] + 0.0006262*x[0]*x[3] - 0.0022053*x[2]*x[4]
        v = 80.51249  + 0.0071317*x[1]*x[4] + 0.0029955*x[0]*x[1] + 0.0021813*x[2]**2
        w = 9.300961  + 0.0047026*x[2]*x[4] + 0.0012547*x[0]*x[2] + 0.0019085*x[2]*x[3]
        return np.array([-u, u-92, -v+90, v-110, -w+20, w-25])

    f_opt = -30665.539

elif problem == 'G6':
    n = 2
    lb = np.array([13, 0], dtype=float)
    ub = np.array([100, 100], dtype=float)

    def objFun(x):
        return (x[0]-10)**3 + (x[1]-20)**3

    def conFun(x):
        return np.array([
            -(x[0]-5)**2 - (x[1]-5)**2 + 100,
            (x[0]-6)**2 + (x[1]-5)**2 - 82.81
        ])

    f_opt = -6961.81388

elif problem == 'G7':
    n = 10
    lb = -10 * np.ones(n)
    ub =  10 * np.ones(n)

    def objFun(x):
        return (x[0]**2 + x[1]**2 + x[0]*x[1]
                - 14*x[0] - 16*x[1]
                + (x[2]-10)**2
                + 4*(x[3]-5)**2
                + (x[4]-3)**2
                + 2*(x[5]-1)**2
                + 5*x[6]**2
                + 7*(x[7]-11)**2
                + 2*(x[8]-10)**2
                + (x[9]-7)**2
                + 45)

    def conFun(x):
        return np.array([
            4*x[0]+5*x[1]-3*x[6]+9*x[7]-105,
            10*x[0]-8*x[1]-17*x[6]+2*x[7],
            -8*x[0]+2*x[1]+5*x[8]-2*x[9]-12,
            3*(x[0]-2)**2+4*(x[1]-3)**2+2*x[2]**2-7*x[3]-120,
            5*x[0]**2+8*x[1]+(x[2]-6)**2-2*x[3]-40,
            x[0]**2+2*(x[1]-2)**2-2*x[0]*x[1]+14*x[4]-6*x[5],
            0.5*(x[0]-8)**2+2*(x[1]-4)**2+3*x[4]**2-x[5]-30,
            -3*x[0]+6*x[1]+12*(x[8]-8)**2-7*x[9]
        ])

    f_opt = 24.3062091

elif problem == 'G9':
    n = 7
    lb = -10 * np.ones(n)
    ub =  10 * np.ones(n)

    def objFun(x):
        return ((x[0]-10)**2
                + 5*(x[1]-12)**2
                + x[2]**4
                + 3*(x[3]-11)**2
                + 10*x[4]**6
                + 7*x[5]**2
                + x[6]**4
                - 4*x[5]*x[6]
                - 10*x[5]
                - 8*x[6])

    def conFun(x):
        return np.array([
            2*x[0]**2+3*x[1]**4+x[2]+4*x[3]**2+5*x[4]-127,
            7*x[0]+3*x[1]+10*x[2]**2+x[3]-x[4]-282,
            23*x[0]+x[1]**2+6*x[5]**2-8*x[6]-196,
            4*x[0]**2+x[1]**2-3*x[0]*x[1]+2*x[2]**2+5*x[5]-11*x[6]
        ])

    f_opt = 680.6300573

elif problem == 'G10':
    n = 8
    lb = np.array([100, 1000, 1000, 10, 10, 10, 10, 10], dtype=float)
    ub = np.array([10000, 10000, 10000, 1000, 1000, 1000, 1000, 1000], dtype=float)

    def objFun(x):
        return x[0] + x[1] + x[2]

    def conFun(x):
        return np.array([
            -1 + 0.0025*(x[3]+x[5]),
            -1 + 0.0025*(x[4]+x[6]-x[3]),
            -1 + 0.01*(x[7]-x[4]),
            -x[0]*x[5] + 833.33252*x[3] + 100*x[0] - 83333.333,
            -x[1]*x[6] + 1250*x[4] + x[1]*x[3] - 1250*x[3],
            -x[2]*x[7] + 1250000 + x[2]*x[4] - 2500*x[4]
        ])

    f_opt = 7049.3307

elif problem == 'G12':
    n = 3
    lb = -10 * np.ones(n)
    ub =  10 * np.ones(n)

    def objFun(x):
        return 1 - 0.01*((x[0]-5)**2 + (x[1]-5)**2 + (x[2]-5)**2)

    def conFun(x):
        return np.array([np.sum((x - np.round(x))**2) - 0.0625])

    f_opt = 1.0

else:
    raise ValueError(f"Invalid problem selection: {problem}")


penaltyCoeff = 1e8
C       = 200
R       = 0.995
MaxIter = 5000

def penalized(x):
    return objFun(x) + penaltyCoeff * np.sum(np.maximum(0, conFun(x))**2)

bestValues    = np.zeros(runs)
bestSolutions = np.zeros((runs, n))
errorHistory  = np.zeros(MaxIter)


for run in range(runs):

    range_ = (ub - lb).copy()

    # Initial random population (per-variable bounds)
    x = np.array([[lb[j] + np.random.rand() * (ub[j] - lb[j])
                   for j in range(n)]
                  for _ in range(C)])

    currentFitness = np.zeros((MaxIter, C))
    fx = np.zeros(C)

    for iteration in range(MaxIter):

        # Evaluate penalized objective
        for i in range(C):
            fx[i] = penalized(x[i])

        currentFitness[iteration] = fx

        # Roulette-wheel selection (shift so minimum > 0)
        fx_shifted  = fx - fx.min() + np.finfo(float).eps
        fitness     = 1.0 / fx_shifted
        probability = fitness / fitness.sum()
        cumulativeP = np.cumsum(probability)

        selectedCandidate = np.zeros((C, n))
        for i in range(C):
            r   = np.random.rand()
            idx = np.searchsorted(cumulativeP, r)
            idx = min(idx, C - 1)
            selectedCandidate[i] = x[idx]

        # Shrink search range
        range_ *= R

        # New bounds centred on selected candidates
        newLB = np.clip(selectedCandidate - range_ / 2, lb, ub)
        newUB = np.clip(selectedCandidate + range_ / 2, lb, ub)

        # Record error before updating population
        bestIdx_iter       = np.argmin(fx)
        bestCandidate_iter = x[bestIdx_iter]
        errorHistory[iteration] = abs(objFun(bestCandidate_iter) - f_opt)

        # Generate new population
        x = newLB + np.random.rand(C, n) * (newUB - newLB)

    
    finalBestIdx       = np.argmin(fx)
    finalBestCandidate = x[finalBestIdx]
    trueObj            = objFun(finalBestCandidate)

    bestValues[run]    = trueObj
    bestSolutions[run] = finalBestCandidate


print("\nBest Values across all runs:")
for v in bestValues:
    print(f"  {v:.10e}")

bestRunIdx = np.argmin(bestValues)
bestX      = bestSolutions[bestRunIdx]

print(f"\n=== Constraint Check for Best Solution (Run {bestRunIdx + 1}) ===")
print(f"Objective Value : {bestValues[bestRunIdx]:.6f}")
print(f"Known Optimum   : {f_opt:.6f}\n")

gx           = conFun(bestX)
allSatisfied = True

for k, g in enumerate(gx):
    satisfied = g <= 1e-5
    status    = "SATISFIED" if satisfied else "VIOLATED"
    print(f"  g{k+1}(x) = {g:+.6f}  --> {status}")
    if not satisfied:
        allSatisfied = False

print()
if allSatisfied:
    print("All constraints satisfied.")
else:
    print("One or more constraints VIOLATED.")