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

def generar_poligono(n = 0):
  if n < 3: return
  teta, t_aux = (360 / n) * pi / 180, (45) * pi / 180
  puntos, dx, dy, d = [], 50, 50, 15 # Desplazamiento en x , y   
  for i in range(n):
      x, y = round(d * cos(t_aux) + dx), round(d * sin(t_aux) + dy)
      t_aux += teta
      print(x, y)
      puntos.append((x, y))
  points_direction = get_vertices(puntos)
  #pf, teta = (dx, dy), -45
  #points_rotated = [ [rotacion(p = i[0], pf = pf, teta = teta), rotacion(p = i[1], pf = pf, teta = teta)] for i in points_direction ]
  print(puntos)
  print (points_direction)
  #print(points_rotated)
  paint_lines(points_direction, 'blue')
  #paint_lines(points_rotated, 'red')
  imprimir_linea()


if '__main__' == '__main__':

  generar_poligono(12)
  