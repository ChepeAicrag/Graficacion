import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'src', 'Libreria'))
from Functions import line, traslacion
from Utils import  draw_point, combinacion

def generar_traslacion(puntos = [], t = (0, 0)):
    points_direction = combinacion(puntos, 2)
    print (points_direction)
    for i in points_direction:
        for j in line(i[0], i[1]):
            x, y = j
            xr, yr = traslacion(p = j, t = t)
            draw_point(x, y, 'blue')
            draw_point(xr, yr, 'red')

if '__main__' == '__main__':
    p1 = (1, 1) 
    p2 = (2, 3)
    p3 = (3, 1)
    T = (-3, -2)
    generar_traslacion(puntos = [p1, p2, p3], t = T)
