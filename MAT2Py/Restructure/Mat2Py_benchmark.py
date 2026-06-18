import numpy as np


def sphere():

    n = 3
    lb = -5.12 * np.ones(n)
    ub =  5.12 * np.ones(n)

    def objFun(x):
        return np.sum(x**2)

    return n, lb, ub, objFun



def g1():

    n = 13

    lb = np.array([0]*9 + [0,0,0,0], dtype=float)
    ub = np.array([1]*9 + [100,100,100,1], dtype=float)

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

    return n, lb, ub, objFun, conFun, f_opt



def g2():
    pass



def g3():
    pass


def g4():

    n = 5

    lb = np.array([78,33,27,27,27], dtype=float)
    ub = np.array([102,45,45,45,45], dtype=float)

    def objFun(x):
        return (
            5.3578547*x[2]**2
            + 0.8356891*x[0]*x[4]
            + 37.293239*x[0]
            - 40792.141
        )

    def conFun(x):

        u = (
            85.334407
            + 0.0056858*x[1]*x[4]
            + 0.0006262*x[0]*x[3]
            - 0.0022053*x[2]*x[4]
        )

        v = (
            80.51249
            + 0.0071317*x[1]*x[4]
            + 0.0029955*x[0]*x[1]
            + 0.0021813*x[2]**2
        )

        w = (
            9.300961
            + 0.0047026*x[2]*x[4]
            + 0.0012547*x[0]*x[2]
            + 0.0019085*x[2]*x[3]
        )

        return np.array([
            -u, u-92,
            -v+90, v-110,
            -w+20, w-25
        ])

    f_opt = -30665.539

    return n, lb, ub, objFun, conFun, f_opt



def g5():
    pass



def g6():

    n = 2

    lb = np.array([13,0], dtype=float)
    ub = np.array([100,100], dtype=float)

    def objFun(x):
        return (x[0]-10)**3 + (x[1]-20)**3

    def conFun(x):
        return np.array([
            -(x[0]-5)**2 - (x[1]-5)**2 + 100,
            (x[0]-6)**2 + (x[1]-5)**2 - 82.81
        ])

    f_opt = -6961.81388

    return n, lb, ub, objFun, conFun, f_opt



def g7():
    ...
    return n, lb, ub, objFun, conFun, f_opt


def g8():
    pass


def g9():
    ...
    return n, lb, ub, objFun, conFun, f_opt



def g10():
    ...
    return n, lb, ub, objFun, conFun, f_opt


def g11():
    pass



def g12():
    ...
    return n, lb, ub, objFun, conFun, f_opt