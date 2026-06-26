import numpy as np


class CohortIntelligence:

    def __init__(
        self,
        obj_fun,
        lb,
        ub,
        n,
        population=200,
        reduction=0.975,
        max_iter=5000,
        penalty_coeff=1e8,
        con_fun=None
    ):

        self.obj_fun = obj_fun
        self.con_fun = con_fun

        self.lb = np.asarray(lb)
        self.ub = np.asarray(ub)

        self.n = n
        self.C = population
        self.R = reduction
        self.max_iter = max_iter
        self.penalty_coeff = penalty_coeff

    def evaluate(self, x):

        if self.con_fun is None:
            return self.obj_fun(x)

        penalty = np.sum(
            np.maximum(0, self.con_fun(x))**2
        )

        return self.obj_fun(x) + self.penalty_coeff * penalty

    def optimize(self):

        range_ = (self.ub - self.lb).copy()

        x = self.lb + np.random.rand(self.C, self.n) * (
            self.ub - self.lb
        )

        history = []

        for _ in range(self.max_iter):

            fx = np.array(
                [self.evaluate(candidate) for candidate in x]
            )

            history.append(np.min(fx))

            fx_shifted = fx - fx.min() + np.finfo(float).eps

            fitness = 1.0 / fx_shifted
            probability = fitness / fitness.sum()

            cumulativeP = np.cumsum(probability)

            selected = np.zeros_like(x)

            for i in range(self.C):

                r = np.random.rand()

                idx = np.searchsorted(
                    cumulativeP,
                    r
                )

                idx = min(idx, self.C - 1)

                selected[i] = x[idx]

            range_ *= self.R

            newLB = np.clip(
                selected - range_/2,
                self.lb,
                self.ub
            )

            newUB = np.clip(
                selected + range_/2,
                self.lb,
                self.ub
            )

            x = newLB + np.random.rand(
                self.C,
                self.n
            ) * (newUB - newLB)

        fx = np.array(
            [self.evaluate(candidate) for candidate in x]
        )

        best_idx = np.argmin(fx)

        return (
            x[best_idx],
            fx[best_idx],
            np.array(history)
        )