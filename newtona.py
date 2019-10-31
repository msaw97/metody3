import math
from funkcje import *

iteracje = 20
epsilon = 0.000000000001

def newtona(f, Df, x_0, M, epsilon):
    """Metoda newtona rozwiazywania rownania nieliniowego"""
    xn = []
    v = f(x_0)
    k = 1

    while k<M:
        xn.append(x_0)
        if abs(v) < epsilon:    #warunek pierwszy
            break

        x_1 = x_0 - v/Df(x_0)  #wzor metody iteracyjnej newtona
        v = f(x_1)

        if abs(x_1 - x_0) < epsilon:    #warunek drugi
            break
        x_0 = x_1
        k=k+1

    return(x_0, xn)

if __name__ == "__main__":
    x, xn= newtona(f_2, Df_2, 3, iteracje, epsilon)
    print("wynik:", x)
    i=1
    for n in xn:
        print("x{} = {}".format(i, n))
        i= i+1
