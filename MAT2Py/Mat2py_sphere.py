import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Cohort Intelligence (Minimization) – Roulette Wheel
# Optimized Convergence for 3 Variables
# ============================================================

runs = 1
n = 3          # Number of variables
C = 200        # Number of candidates
R = 0.99       # Reduction factor
MAX_ITER = 1000

# Objective function: Sphere function
def f(x):
    return np.sum(x ** 2)

# Storage across runs
bestValues    = np.zeros(runs)
bestSolutions = np.zeros((runs, n))

for run in range(runs):

    # Initial bounds
    lb = -5.12
    ub =  5.12
    range_ = ub - lb

    # Initialise candidates
    x = lb + (ub - lb) * np.random.rand(C, n)

    currentFitness = np.zeros((MAX_ITER, C))
    fx = np.zeros(C)

    for iteration in range(MAX_ITER):

        # Evaluate fitness for every candidate
        for i in range(C):
            fx[i] = f(x[i])

        currentFitness[iteration] = fx

        # Roulette-wheel selection (minimisation → invert fitness)
        fitness     = 1.0 / (fx + np.finfo(float).eps)
        probability = fitness / np.sum(fitness)
        cumulativeP = np.cumsum(probability)

        selectedCandidate = np.zeros((C, n))
        for i in range(C):
            r = np.random.rand()
            idx = np.searchsorted(cumulativeP, r)
            idx = min(idx, C - 1)          # guard against floating-point edge
            selectedCandidate[i] = x[idx]

        # Shrink search range
        range_ *= R

        # Build new bounds centred on selected candidates
        newLB = np.clip(selectedCandidate - range_ / 2, lb, ub)
        newUB = np.clip(selectedCandidate + range_ / 2, lb, ub)

        # Sample new candidates inside their personal bounds
        x = newLB + np.random.rand(C, n) * (newUB - newLB)

    # Best result for this run
    bestHistory = np.min(currentFitness, axis=1)   # best-so-far each iteration

    finalBestIdx       = np.argmin(fx)
    finalBestFx        = fx[finalBestIdx]
    finalBestCandidate = x[finalBestIdx]

    bestValues[run]      = finalBestFx
    bestSolutions[run]   = finalBestCandidate

    print(f"\nRun {run + 1}")
    print(f"  Best Function Value : {finalBestFx:.6e}")
    print(f"  Best Candidate      : {finalBestCandidate}")

print("\nbest Values across all runs:")
print(bestValues)

# ── Convergence plot ─────────────────────────────────────────
plt.figure(figsize=(9, 5))
plt.plot(bestHistory, color="steelblue", linewidth=1.5, label="Best Function Value")
plt.xlabel("Iteration")
plt.ylabel("Best Function Value")
plt.title("Convergence Plot of Sphere Function")
plt.grid(True)
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
