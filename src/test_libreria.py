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
def paint_line(points, color):
  for i in points:
      for j in line(i[0], i[1]):
          x, y = j
          draw_point(x, y, color)

def generar_traslacion(puntos=[], t=(0, 0)):
  points_direction = combinacion(puntos, 2)
  print(points_direction)
  for i in points_direction:
      for j in line(i[0], i[1]):
          x, y = j
          xr, yr = traslacion(p=j, t=t)
          draw_point(x, y, 'blue')
          draw_point(xr, yr, 'red')
  imprimir_linea()
  
def generar_rotacion(puntos = [], pf = (0, 0), teta = 0):
  points_direction = combinacion(puntos, 2)
  print (points_direction)
  for i in points_direction:
      for j in line(i[0], i[1]):
          x, y = j
          xr, yr = rotacion(p = j, pf = pf, teta = teta)
          draw_point(x, y, 'c')
          draw_point(xr, yr, 'c')
  imprimir_linea()

def generar_escalado(puntos = [], t = (0, 0)):
  if len(puntos) < 2: return
  points_direction = combinacion(puntos, 2)
  print (points_direction)
  pf = puntos[0]
  points_escalados = [ [escalado(p = i[0], pf = pf, t = t), escalado(p = i[1], pf = pf, t = t)] for i in points_direction]
  print (points_escalados)
  paint_line(points_direction, 'blue')
  paint_line(points_escalados, 'red')
  
  
  #for i in points_direction:
  #    for j in line(i[0], i[1]):
  #        x, y = j
          #xr, yr = escalado(p = j, pf = puntos[0], t = t)
  #        draw_point(x, y, 'blue')
          #draw_point(xr, yr, 'red')
      
      #xe, ye = escalado(p = i[0], pf = pf, t = t)
      #xe2, ye2 = escalado(p = i[1], pf = pf, t = t)
      #for k in line((xe, ye), (xe2, ye2)):
      #  xk, yk = k
      #  draw_point(xk, yk, 'red')
      
  imprimir_linea()

if '__main__' == '__main__':
  # p1 = (1, 1)
  # p2 = (2, 3)
  # p3 = (3, 1)
  # T = (2, 2)
  # generar_traslacion(puntos=[p1, p2, p3], t=T)

  # p1 = (1, 2)
  # p2 = (3, 5)
  # p3 = (12, 15)
  # pf = (1, 2)
  # teta = 45
  # generar_rotacion(puntos = [p1, p2, p3], pf = pf, teta = teta)
  
  # p1 = (1, 4)
  # p2 = (4, 2)
  # p3 = (3, 10)
  # T = (2, 2)
  p1 = (1, 1)
  p2 = (3, 1)
  p3 = (2, 3)
  T = (2, 3)
  generar_escalado(puntos = [p1, p2, p3], t = T)