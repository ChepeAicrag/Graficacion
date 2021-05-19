from math import sin, cos, pi

__author__ = "Jose Angel Garcia Garcia"
__email__ = "chepeaicrag12@gmail.com"

def line(p1, p2):
    '''
        Algoritmo para trazar una linea mediante dos puntos
        :param p1: tupla como primer punto
        :param p2: tupla como segundo punto
        :return: list con los puntos intermedios entre p1 y p2
    '''
    puntos = []
    x0, y0 = p1
    x1, y1 = p2
    dif_x, dif_y = x1 - x0, y1 - y0
    dx, dy = abs(dif_x), abs(dif_y)
    if dy >= dx:
        dx, dy = dy, dx
    inc_E = 2 * dy  # 2dy
    inc_NE = inc_E - 2 * dx  # 2dy - 2dx
    d = inc_E - dx  # 2dy - dx
    x, y = x0, y0
    puntos.append((x, y))
    x_inc = 1 if dif_x > 0 else - 1
    y_inc = 1 if dif_y > 0 else - 1
    x_inc = x_inc if dif_x != 0 else 0
    y_inc = y_inc if dif_y != 0 else 0
    flag = (abs(dif_y/dif_x) if dif_x != 0 else 0) > 1
    for _ in range(dx):
        x = x + x_inc if not flag else x
        y = y + y_inc if flag else y
        if (d < 0 and flag) or (d < 0 and x_inc != 0 and not flag):
            d = d + inc_E
        else:
            x = x + x_inc if flag else x
            y = y + y_inc if not flag else y
            d = d + inc_NE
        puntos.append((x, y))
    return puntos

def __add_point(x, y, puntos):
    '''
        Función para agregar x, y con sus variaciones a una lista
    '''
    puntos.append([x, y])
    puntos.append([y, x])
    puntos.append([y, -x])
    puntos.append([x, -y])
    puntos.append([-x, -y])
    puntos.append([-y, -x])
    puntos.append([-x, y])
    puntos.append([-y, x])

def circunferencia(r):
    '''
        Algoritmo para trazar una circunferencia a partir de un radio r
        :params r: radio de la circunferencia
    '''
    puntos = []
    x, y = 0, r
    p = 5/4 - r
    __add_point(x, y, puntos)
    while y > x:
        x = x + 1
        aux = p + 2 * x  
        if p < 0:
            p = aux + 1  
        else:
            p = aux - 2 * y + 3  
            y = y - 1
        __add_point(y, x, puntos)
    return puntos



def rotacion(p = (0, 0), pf = (0, 0), teta = 0):
    '''
        Rotación de una coordenada respecto a un punto arbitrario y un ángulo 
        :params p: coordenada como tupla (x, y)
        :params pf: coordenada de punto sobre el que se rota como tupla (xp, yp)
        :params teta: ángulo de rotación en grados
        :return: coordenada rotada con respecto a un punto arbitrario como tupla (x', y')        
    '''
    teta = teta * pi / 180
    xp, yp = pf
    x, y = p
    dif_x, dif_y, s, c = x - xp, y - yp, round(sin(teta)), round(cos(teta))
    return xp + dif_x * c - dif_y * s, yp + dif_x * s + dif_y * c

def escalado(p = (0, 0), pf = (0, 0), s = (0, 0)):
    '''
        Escalado de una coordenada respecto a un punto arbitrario y un vector de escalamiento
        :params p: coordenada como tupla (x, y)
        :params pf: coordenada de punto fijo como tupla (xp, yp)
        :params s: vector de escalamiento como tupla (xs, ys)
        :return: coordenada escalada con respecto a un punto arbitrario como tupla (x', y')
    '''
    x, y, = p
    xp, yp = pf 
    xs, ys = s
    return xp + xs * (x - xp), yp + ys * (y - yp)

def traslacion(p = (0, 0), t = (0, 0)):
    '''
        Traslación de una coordenada mediante un vector de traslación
        :params p: coordenada como tupla (x, y)
        :params t: vector de traslación como tupla (xt, yt)
        :return: coordenada trasladada como tupla (x', y')
    '''
    x, y = p
    xt, yt = t
    return x + xt, y + yt