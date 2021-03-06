import numpy as np
import matplotlib.pyplot as plt
from Libreria.Functions import line, traslacion, rotacion, escalado
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

def draw_point(p = (0, 0)):
  x, y = p
  if x > 0 and y > 0: 
    linea.append([y, x])

"""
  Función que dada una lista de tuplas, donde cada tupla es un punto, entonces se pinta el pixel con respectiva
  coordenada
"""
def paint_lines(points):
  for i in points: # [(), (), (), ()]
    draw_point(i)

# [[(x0, y0), (x1, y1)]]
"""
  Función que dada una lista de listas que contienen cada una el punto inicial y final se genera cada una de 
  las lineas, y sus respectivos puntos de todas las lineas formadas se almacenan en una lista 
  points = [[(x0, y0), (x1, y1)], [(xn-1, yn-1), (xn, yn)]]
  return [(x0, y0) ... (x1, y1), (xn-1, y0) ... (xn, yn)] # Lista de tuplas
"""
def get_points_lines(points):
  return [ j for i in points for j in line(i[0], i[1]) ] 
  
""" 
  Es una función que dada una lista de puntos [(x, y), (x1, y1) ... (xn, yn)] retorna
  una lista de listas que tienen el punto inicial y final de la linea que forma el contorno 
  [[(x, y), (x1, y1)], [(x1, y1), (x2, y2)] ... [(xn-1, yn-1), (xn, yn)], [(xn, yn), (x, y)]]
"""
def get_vertices(points):
  l = len(points)
  return [ [ points[i], points[i + 1 if i < l - 1 else 0] ] for i in range(l) ]

"""
  Rellena a partir de una lista de tuplas (puntos) y un valor de y máximo para iterar de forma decremental
  Trazando de izquierda a derecha de forma horizontal los pixeles de adentro del contorno
"""
def rellenar(points_outline, ymax):
  values_x = []
  print('puntos_contorno', points_outline)
  for vy in range(ymax):
    values_x = [ x for (x, y) in points_outline if y == vy ]
    if len(values_x) == 0: continue
    for xp in range(min(values_x), max(values_x)):
      draw_point((xp, vy))
    values_x = []

def generar_poligono(n = 0):
  if n < 3: return
  teta, t_aux = (360 / n) * pi / 180, (45) * pi / 180
  puntos, dx, dy, d = [], 15, 15, 10 # Desplazamiento en x , y   
  for _ in range(n):
      x, y = round(d * cos(t_aux) + dx), round(d * sin(t_aux) + dy)
      t_aux += teta
      puntos.append((x, y))
  return puntos 

def draw_poligono(puntos):
  points_direction = get_vertices(puntos) # La combinación entre esos vertices para marcar los puntos de las líneas
  ymax = max( [ y for x, y in puntos ] ) # La y maxima para hacer el pintado de forma horizontal
  print ('points_direction', points_direction)  
  points_lines = get_points_lines(points_direction) # Lista con todas los puntos de todas las lineas para el contorno
  paint_lines(points_lines) # Pinta las lineas de alrededor del poligono 
  rellenar(points_lines, ymax) # Pinta los pixeles interiores del poligono (relleno)
  imprimir_linea()

def rotate_poligono(puntos = [], pf = (0, 0), teta = 0):
  return [ rotacion(p, pf, teta) for p in puntos ]
  
def translate_poligono(puntos = [], t = (0, 0)):
  return [ traslacion(p, t) for p in puntos ]

def escalado_poligono(puntos = [], pf = (0, 0), e = (0, 0)):
  return [ escalado(p, pf, e) for p in puntos ]

def crear_poligono():
  puntos = []
  n = int(input('Introduce el el número de lados: '))
  if n < 3: 
    print('El número de lados debe ser mayor a 3')
  else: 
    return generar_poligono(n)
  return puntos

def limpiar_pantalla():
  matriz_linea = np.zeros((N, N))
  linea = []

def validar_poligono(poligono):
  if len(poligono) == 0: 
    print('Debe crear un poligono primeramnete')
    return False
  return True

def draw_poligono_msj(poligono,  msj):
  print(msj)
  draw_poligono(poligono)
  limpiar_pantalla()

def menu():
    poligono = []
    while True:
        op = int(input('Seleccione una opción:\n1. Crear poligono\n2. Aplicar traslación\n3. Aplicar Escalado\n4. Aplicar Rotación\n5. Salir'))
        if op == 5: return
        elif op == 1:
          poligono = crear_poligono()
          if len(poligono) == 0: break
          draw_poligono_msj(poligono, 'El poligono creado es: ')
        elif op == 2:
          draw_poligono_msj(poligono, 'El poligono creado es: ')
          
          poligono_trasladado = translate_poligono(poligono, t = )
          draw_poligono_msj(poligono_trasladado, 'El poligono trasladado creado es: ')
        elif op == 3:

        elif op == 4:

        else: 
          print('Seleccione correctamente')
          break
          
if '__main__' == '__main__':
  #poligono = generar_poligono(6)
  #print(poligono)
  #teta = 45
  #draw_poligono(poligono)

  #poligono_rotado = rotate_poligono(puntos = poligono, teta = teta)
  #draw_poligono(poligono_rotado)

  #poligono_trasladado = translate_poligono(poligono, t = (25, 25))
  #draw_poligono(poligono_trasladado)

  #poligono_escalado = escalado_poligono(poligono, pf = (0, 0), e = (2, 2))
  #draw_poligono(poligono_escalado)
  menu()