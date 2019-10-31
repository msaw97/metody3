from bisekcja import bisekcja
from newtona import newtona
from sieczne import sieczne
from wykres import wykres
from funkcje import *

epsilon = 0.000000000001
funkcja = f_2
funkcja_pochodna = Df_2
iteracje = 20

wynik, xn_bisekcja = bisekcja(funkcja, 3, 4, iteracje, epsilon)
print("Wynik z metody bisekcji: ", wynik)

wynik, xn_newtona= newtona(funkcja, funkcja_pochodna, 3, iteracje, epsilon)
print("Wynik z metody newtona: ", wynik)

wynik, xn_sieczne = sieczne(funkcja, 3, 4, iteracje, epsilon)
print("Wynik z metody siecznych: ", wynik)

wykres(funkcja, xn_bisekcja, xn_newtona, xn_sieczne)
