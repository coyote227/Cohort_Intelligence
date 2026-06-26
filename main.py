import matplotlib.pyplot as plt

from algorithm import CohortIntelligence
from benchmark import (
    sphere,
    rosenbrock, 
    ackley,
    g1,
    g4,
    g6,
    welded_beam,
    pressure_vessel,
    tension_compression_spring
)


PROBLEMS = {
    "SPHERE": sphere,
    "ROSENBROCK": rosenbrock,
    "ACKLEY": ackley,
    "G1": g1,
    "G4": g4,
    "G6": g6,
    "WB" :welded_beam,
    "PV" : pressure_vessel,
    "TCS" : tension_compression_spring
}



print("\nProblems:")
for name in PROBLEMS:
    print(f"  {name}")

problem_name = input("\nSelect: ").strip().upper()

if problem_name not in PROBLEMS:
    raise ValueError(f"Unknown problem: {problem_name}")


if problem_name == "SPHERE" or problem_name == "ROSENBROCK" or problem_name == "ACKLEY":

    n, lb, ub, objFun = sphere()

    ci = CohortIntelligence(
        obj_fun=objFun,
        lb=lb,
        ub=ub,
        n=n,
        population=200,
        reduction=0.97,
        max_iter=1000
    )

    best_x, best_f, history = ci.optimize()

    print("Best Solution:")
    print(best_x)
    print(f"\nBest Function Value: {best_f:.10e}")

else:

    n, lb, ub, objFun, conFun, f_opt = PROBLEMS[problem_name]()

    ci = CohortIntelligence(
        obj_fun=objFun,
        con_fun=conFun,
        lb=lb,
        ub=ub,
        n=n,
        population=7,
        reduction=0.995,
        max_iter=4500,
        penalty_coeff=1e7
    )

    best_x, best_f, history = ci.optimize()

    print("Solution:")
    print(best_x)

    print(f"Objective Value   : {objFun(best_x):.10e}")
    print(f"Known Optimum     : {f_opt:.10e}")

    print("\nConstraint Check")

    gx = conFun(best_x)

    feasible = True

    for i, g in enumerate(gx):

        satisfied = g <= 1e-5

        if not satisfied:
            feasible = False

        status = "SATISFIED" if satisfied else "VIOLATED"

        print(
            f"g{i+1}(x) = {g:+.6e}  -->  {status}"
        )

    print(
        "\nFeasible Solution"
        if feasible
        else "\nInfeasible Solution"
    )
        



plt.figure(figsize=(9, 5))

plt.plot(
    history,
    color="steelblue",
    linewidth=1.5
)

plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.title(f"Convergence Plot - {problem_name}")

plt.grid(True)

plt.tight_layout()
# plt.show()