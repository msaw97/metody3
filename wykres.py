import matplotlib.pyplot as plt
import numpy as np

def wykres(funkcja, metoda1,metoda2,metoda3):
    y = [ i+1 for i in range(0, len(metoda1))]

    plt.scatter(x= [ i+1 for i in range(0, len(metoda1))] , y = metoda1, c='r')
    plt_b = plt.plot([ i+1 for i in range(0, len(metoda1))] , metoda1, 'r--')
    plt.scatter(x= [ i+1 for i in range(0, len(metoda2))] , y = metoda2, c='g')
    plt_n = plt.plot([ i+1 for i in range(0, len(metoda2))] , metoda2, 'g--')
    plt.scatter(x= [ i+1 for i in range(0, len(metoda3))] , y = metoda3, c='b')
    plt_b = plt.plot([ i+1 for i in range(0, len(metoda3))] , metoda3, 'b--')
    plt.grid()
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    plt.tick_params(
        axis='x',
        which='minor',
        bottom=False,
        top=False,
        labelbottom=False)
    plt.xticks(np.arange(min(y), max(y)+1, 1.0))

    plt.title("Znajdowanie miejsca zerowego dla funkcji: {}".format(funkcja.__doc__))
    plt.xlabel("Iteracje")
    plt.ylabel("X")
    plt.legend(["metoda {}".format(m) for m in ("bisekcji", "newtona", "siecznych")])
    plt.show()
