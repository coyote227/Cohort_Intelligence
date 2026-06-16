import matplotlib.pyplot as plt
from algorithm import CI,check_constraints
from benchmark import SPHERE,ROSENBROCK,G6,ACKLEY,G11,G12

# selection of the benchmarking function 

benchmarks = [SPHERE,ROSENBROCK,ACKLEY,G6,G11,G12]

print("Select benchmark:")
for i, b in enumerate(benchmarks, 1):
    print(f"{i}. {b['name']}")

choice = int(input("benchmarking function: "))
benchmark = benchmarks[choice - 1]


def main():

    candidates = int(input("Enter number of candidates: "))
    reduction_factor = float(input("Enter reduction factor: "))

    history, population_history = CI(
        objective=benchmark["function"],
        candidates=candidates,
        iterations= 3500,
        reduction_factor=reduction_factor,
        lower_bounds=benchmark["lower_bounds"],
        upper_bounds=benchmark["upper_bounds"],
        initial_ranges=list(zip(
            benchmark["lower_bounds"],
            benchmark["upper_bounds"])
        )
    )

    
    check_constraints(
        population_history,
        benchmark["lower_bounds"],
        benchmark["upper_bounds"]
    )
    

# printing the candidate table with function value at each iteration

#headers
    for c in range(candidates):

        candidate_fitness = [
            history[i][c]
            for i in range(len(history))
        ]

        plt.plot(
            range(1, len(history) + 1),
            candidate_fitness,
            label=f"C{c+1}"
        )
        

    dimensions = len(benchmark["lower_bounds"])

    header = f"{'Iter':<6}{'Cand':<6}"

    for dim in range(dimensions):
        header += f"{f'x{dim+1}':<20}"

    header += f"{'Fitness':<25}"

    print(header)
    print("-" * len(header))


#values
    dimensions = len(population_history[0][0])

    for iteration in range(len(history)):

        for cand in range(candidates):

            position = population_history[iteration][cand]
            fitness = history[iteration][cand]

            row = (
                f"{iteration+1:<6}"
                f"{cand+1:<6}"
            )

            for dim in range(dimensions):
                row += f"{position[dim]:<25.10e}"

            row += f"{fitness:<20.10e}"

            print(row)

        print("\n")

    
    

    # plot graph
    plt.title("CI Fitness per Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.show()


if __name__ == "__main__":
    main()