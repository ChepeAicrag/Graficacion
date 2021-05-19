import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'src', 'Libreria'))
from Functions import line, escalado
from Utils import  draw_point, combinacion


def generar_escalado(puntos = [], t = (0, 0)):
    points_direction = combinacion(puntos, 2)
    print (points_direction)
    for i in points_direction:
        for j in line(i[0], i[1]):
            x, y = j
            xr, yr = escalado(p = j, pf = puntos[0], s = t)
            draw_point(x, y, 'blue')
            draw_point(xr, yr, 'red')

if '__main__' == '__main__':
    p1 = (1, 4)
    p2 = (4, 2)
    p3 = (3, 10)
    T = (1, 1)
    generar_escalado(puntos = [p1, p2, p3], t = T)