import numpy as np
import matplotlib.pyplot as plt
from Libreria.Functions import line, traslacion, rotacion, escalado
from Libreria.Utils import combinacion
import matplotlib
matplotlib.use('TKAgg')

N = 50
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

# points = [[(), ()]]
def paint_lines(points, color):
  for i in points:
      for j in line(i[0], i[1]):
          x, y = j
          draw_point(x, y, color)

def generar_traslacion(puntos = [], t = (0, 0)):
  points_direction = combinacion(puntos, 2)
  print(points_direction)
  points_transferred = [ [traslacion(p = i[0], t = t), traslacion(p = i[1], t = t)] for i in points_direction ]
  print(points_transferred)
  paint_lines(points_direction, 'blue')
  paint_lines(points_transferred, 'red')
  imprimir_linea()
  
def generar_rotacion(puntos = [], pf = (0, 0), teta = 0):
  points_direction = combinacion(puntos, 2)
  print (points_direction)
  # points_rotated = [ [rotacion(p = i[0], pf = pf, teta = teta), rotacion(p = i[1], pf = pf, teta = teta)] for i in points_direction ]
  # print(points_rotated)
  # paint_lines(points_direction, 'blue')
  # paint_lines(points_rotated, 'red')
  for i in points_direction:
        for j in line(i[0], i[1]):
            x, y = j
            xr, yr = rotacion(p = j, pf = pf, teta = teta)
            draw_point(x, y, 'blue')
            draw_point(xr, yr, 'red')

  imprimir_linea()

def generar_escalado(puntos = [], s = (0, 0)):
  if len(puntos) < 2: return
  points_direction = combinacion(puntos, 2)
  print (points_direction)
  pf = puntos[0]
  points_escalados = [ [escalado(p = i[0], pf = pf, s = s), escalado(p = i[1], pf = pf, s = s)] for i in points_direction]
  print (points_escalados)
  paint_lines(points_direction, 'blue')
  paint_lines(points_escalados, 'red')
  imprimir_linea()

if '__main__' == '__main__':
  # p1 = (1, 1)
  # p2 = (2, 3)
  # p3 = (3, 1)
  # T = (4, 4)
  # generar_traslacion(puntos = [p1, p2, p3], t = T)

  # p1 = (1, 2)
  # p2 = (3, 5)
  # p3 = (12, 15)
  # pf = (1, 2)
  # teta = 45
  p1 = (1, 1)
  p2 = (10, 1)
  p3 = (5, 10)
  pf = (5, 10)
  teta = 90
  generar_rotacion(puntos = [p1, p2, p3], pf = pf, teta = teta)
  
  # p1 = (1, 4)
  # p2 = (4, 2)
  # p3 = (3, 10)
  # T = (2, 2)

  # p1 = (1, 1)
  # p2 = (3, 1)
  # p3 = (2, 3)
  # S = (2, 3)
  # generar_escalado(puntos = [p1, p2, p3], s = S)