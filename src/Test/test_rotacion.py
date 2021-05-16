import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'src', 'Libreria'))
from Functions import line, rotacion
from Utils import  draw_point, combinacion

def generar_rotacion(puntos = [], pf = (0, 0), teta = 0):
    points_direction = combinacion(puntos, 2)
    print (points_direction)
    for i in points_direction:
        for j in line(i[0], i[1]):
            x, y = j
            xr, yr = rotacion(p = j, pf = pf, teta = teta)
            draw_point(x, y)
            draw_point(xr, yr)

if '__main__' == '__main__':
    p1 = (1, 2)
    p2 = (3, 5)
    p3 = (12, 15)
    pf = (0, 0)
    teta = 45
    generar_rotacion(puntos = [p1, p2, p3], pf = pf, teta = teta)
