import matplotlib.pyplot as plt
import matplotlib as mpl

def draw_point(x, y, c):
    print(f'({x}, {y}) -> {c}')
    plt.scatter(x, y, c = c)

def conjunto_potencia(c):
    if len(c) == 0:
        return [[]]
    r = conjunto_potencia(c[:-1])
    # print(r)
    #print('c --> ', c)
    return r + [s + [c[-1]] for s in r]

def combinacion(c, n):
    return [i for i in conjunto_potencia(c) if len(i) == n]
    #return [j for i in conjunto_potencia(c) if len(i) == n for j in i]

#print(combinacion([1, 2, 3, 4, 5, 6, 7], 4))
#print(conjunto_potencia(['a', 'b', 'c']))
