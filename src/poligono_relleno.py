import numpy as np
import matplotlib.pyplot as plt
from Libreria.Functions import line, traslacion, rotacion, escalado
from Libreria.Utils import combinacion
import matplotlib
from math import  pi, cos, sin

matplotlib.use('TKAgg')

N = 100
matriz_linea = np.zeros((N, N))
linea = []


def imprimir_linea():
  for c in linea:
      matriz_linea[c[0], c[1]] = 1

  plt.imshow(matriz_linea)
  plt.colorbar()
  plt.show()

def draw_point(x, y, c):
  linea.append([y, x])

def paint_lines(points, color):
  for i in points:
      for j in line(i[0], i[1]):
          x, y = j
          draw_point(x, y, color)

def get_vertices(puntos):
  l = len(puntos) - 1
  points = []
  for i in range(l):
    points.append([puntos[i], puntos[i + 1]])
  points.append([puntos[0], puntos[-1]])
  return points

def rellenar(vertices, xmax, ymax):
  vertices_act = []
  for i in vertices:
    points = line(i[0], i[1])
    for p in points:
        vertices_act.append(p)
  l = len(vertices_act)
  print(vertices_act)
  pixels = {}
  values_x = []
  for vy in range(ymax):
    for p  in vertices_act:
        x, y = p
        if y == vy:
            values_x.append(x)
    if len(values_x) > 0:
        xma, xmi = max(values_x), min(values_x) 
        pixels[vy] = [xmi, xma]
    values_x = []
  for y, x in pixels.items():
      for j in line((x[0], y), (x[1], y)):
          x, y = j
          draw_point(x, y, 'red')

def maximo(points):
    xmax, ymax = 0, 0
    for p in points:
        x, y = p
        xmax = x if x > xmax else xmax
        ymax = y if y > ymax else ymax
    return xmax, ymax

def generar_poligono(n = 0):
  if n < 3: return
  teta, t_aux = (360 / n) * pi / 180, (45) * pi / 180
  puntos, dx, dy, d = [], 10, 10, 5 # Desplazamiento en x , y   
  for i in range(n):
      x, y = round(d * cos(t_aux) + dx), round(d * sin(t_aux) + dy)
      t_aux += teta
      print(x, y)
      puntos.append((x, y))
  points_direction = get_vertices(puntos)
  print(puntos)
  xmax, ymax = maximo(puntos)
  print (points_direction)
  paint_lines(points_direction, 'blue')
  rellenar(points_direction, xmax, ymax)
  imprimir_linea()


if '__main__' == '__main__':
  generar_poligono(5)
  