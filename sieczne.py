from funkcje import *

iteracje = 20
epsilon = 0.000000000001

def sieczne(f, a, b, M, epsilon):
    """Metoda siecznych rozwiazywania rownania nieliniowego"""
    f_a = f(a)
    f_b = f(b)
    k = 1
    xn = []

    while abs(f_a) > epsilon and k<= M:
        try:
            S = float(f_b - f_a)/(b - a)
            x = b - float(f_b)/S
            xn.append(x)
        except ZeroDivisionError:
            print("Error, dzielenie przez zero")
        a = b
        b = x
        f_a = f_b
        f_b = f(b)
        k = k + 1

    return x, xn

if __name__ == "__main__":
    x, xn= sieczne(f_2, 3, 4 , iteracje, epsilon)
    print("wynik:", x)
    i=1
    for n in xn[:-1]:
        print("x{} = {}".format(i, n))
        i= i+1
