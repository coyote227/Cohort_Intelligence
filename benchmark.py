import numpy as np


def sphere():

    n = 3
    lb = -5.12 * np.ones(n)
    ub =  5.12 * np.ones(n)

    def objFun(x):
        return np.sum(x**2)

    return n, lb, ub, objFun

import numpy as np

def rosenbrock():

    n = 2
    lb = np.full(n, -30.0)
    ub = np.full(n, 30.0)

    def objFun(x):
        return np.sum(
            100.0 * (x[1:] - x[:-1]**2)**2 +
            (x[:-1] - 1.0)**2
        )

    def conFun(x):
        return np.array([])  # unconstrained

    f_opt = 0.0

    return n, lb, ub, objFun, conFun, f_opt
    
import numpy as np

def ackley():

    n = 2
    lb = np.full(n, -32.768)
    ub = np.full(n, 32.768)

    def objFun(x):
        a = 20.0
        b = 0.2
        c = 2.0 * np.pi

        term1 = -a * np.exp(-b * np.sqrt(np.mean(x**2)))
        term2 = -np.exp(np.mean(np.cos(c * x)))

        return term1 + term2 + a + np.e

    def conFun(x):
        return np.array([])  # unconstrained

    f_opt = 0.0

    return n, lb, ub, objFun, conFun, f_opt

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
    pass


def g8():
    pass


def g9():
    pass



def g10():
    pass


def g11():
    pass



def g12():
    pass
    

import numpy as np

def welded_beam():
    n = 4
    lb = np.array([0.1, 0.1, 0.1, 0.1], dtype=float)
    ub = np.array([10.0, 10.0, 10.0, 10.0], dtype=float)

    def objFun(x):
        return 1.10471*x[0]**2*x[1] + 0.04811*x[2]*x[3]*(14.0 + x[1])

    def conFun(x):
        P = 6000.0
        L = 14.0
        E = 30e+6
        G = 12e+6
        t_max = 13600.0
        s_max = 30000.0
        d_max = 0.25

        M = P*(L + x[1]/2)
        R = np.sqrt(0.25*(x[1]**2 + (x[0]+x[2])**2))
        J = 2/np.sqrt(2)*x[0]*x[1]*(x[1]**2/12 + 0.25*(x[0]+x[2])**2)
        P_c = (4.013*E/(6*L**2))*x[2]*x[3]**3*(1 - 0.25*x[2]*np.sqrt(E/G)/L)

        t1 = P/(np.sqrt(2)*x[0]*x[1])
        t2 = M*R/J
        t = np.sqrt(t1**2 + t1*t2*x[1]/R + t2**2)

        s = 6*P*L/(x[3]*x[2]**2)
        d = 4*P*L**3/(E*x[3]*x[2]**3)

        return np.array([
            t - t_max,
            s - s_max,
            x[0] - x[3],
            0.10471*x[0]**2 + 0.04811*x[2]*x[3]*(14.0 + x[1]) - 5.0,
            d - d_max,
            P - P_c
        ])

    f_opt = 1.724852
    return n, lb, ub, objFun, conFun, f_opt
    
def pressure_vessel():
    n = 4
    lb = np.array([0.0, 0.0, 0.0, 0.0], dtype=float)
    ub = np.array([99.0, 99.0, 200.0, 200.0], dtype=float)

    def objFun(x):
        return (
            0.6224*x[0]*x[2]*x[3]
            + 1.7781*x[1]*x[2]**2
            + 3.1661*x[0]**2*x[3]
            + 19.84*x[0]**2*x[2]
        )

    def conFun(x):
        return np.array([
            -x[0] + 0.0193*x[2],
            -x[1] + 0.00954*x[2],
            -np.pi*x[2]**2*x[3] - (4/3)*np.pi*x[2]**3 + 1296000,
            x[3] - 240
        ])

    f_opt = 6059.7143
    return n, lb, ub, objFun, conFun, f_opt


def tension_compression_spring():
    n = 3
    lb = np.array([0.0, 0.0, 0.0], dtype=float)
    ub = np.array([100.0, 100.0, 100.0], dtype=float)

    def objFun(x):
        return x[0]**2*x[1]*(x[2] + 2)

    def conFun(x):
        return np.array([
            1 - (x[1]**3*x[2])/(71785*x[0]**4),
            (4*x[1]**2 - x[0]*x[1])/(12566*x[0]**3*(x[1]-x[0])) + 1/(5108*x[0]**2) - 1,
            1 - 140.45*x[0]/(x[2]*x[1]**2),
            (x[0]+x[1])/1.5 - 1
        ])

    f_opt = 0.012665
    return n, lb, ub, objFun, conFun, f_opt