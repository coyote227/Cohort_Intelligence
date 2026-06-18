import matplotlib.pyplot as plt

from Mat2Py_algorithm import CohortIntelligence
from Mat2Py_benchmark import (
    sphere,
    g1,
    g4,
    g6,
    g7,
    g9,
    g10,
    g12
)


PROBLEMS = {
    "SPHERE": sphere,
    "G1": g1,
    "G4": g4,
    "G6": g6,
    "G7": g7,
    "G9": g9,
    "G10": g10,
    "G12": g12
}



print("\nAvailable Problems:")
for name in PROBLEMS:
    print(f"  {name}")

problem_name = input("\nSelect Problem: ").strip().upper()

if problem_name not in PROBLEMS:
    raise ValueError(f"Unknown problem: {problem_name}")


if problem_name == "SPHERE":

    n, lb, ub, objFun = sphere()

    ci = CohortIntelligence(
        obj_fun=objFun,
        lb=lb,
        ub=ub,
        n=n,
        population=200,
        reduction=0.99,
        max_iter=1000
    )

    best_x, best_f, history = ci.optimize()

    print("\n===== RESULTS =====")
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
        max_iter=5000,
        penalty_coeff=1e8
    )

    best_x, best_f, history = ci.optimize()

    print("\n===== RESULTS =====")
    print("Best Solution:")
    print(best_x)

    print(f"\nPenalized Fitness : {best_f:.10e}")
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
plt.show()