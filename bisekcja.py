from funkcje import *

iteracje = 20
epsilon = 0.000000000001

def bisekcja(f, a, b, M, epsilon):
    """Metoda bisekcji rozwiazywania rownania nieliniowego"""
    k=1
    xn = []

    while abs(a - b) > epsilon and k< M:
        try:
            x1 = a  + (b - a)/ 2    #znajdowanie srodkowego punktu przedzialu
            xn.append(x1)
        except:
            print("Error, blad w wyborze przedzialu [a, b]")
            
        if abs(f(x1)) <= epsilon:
            break

        elif f(x1) * f(a) < 0:
            b = x1
        else:
            a = x1
        k=k+1

    wynik = a + (b - a)/ 2
    xn.append(wynik)
    return (wynik, xn)

if __name__ == "__main__":
    wynik, xn = bisekcja(f_2, 3, 4, iteracje, epsilon)
    print("wynik:", wynik)
    i=1
    for n in xn:
        print("x{} = {}".format(i, n))
        i= i+1
