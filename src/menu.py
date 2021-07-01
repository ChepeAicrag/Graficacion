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

def paint_lines(line):
  for i in line: 
    draw_point(i)

def generar_poligono(n = 0, r = 0):
  if n < 3: return
  teta, t_aux = (360 / n) * pi / 180, (45) * pi / 180
  puntos, dx, dy = [], 10, 10
  for _ in range(n):
      x, y = round(r * cos(t_aux) + dx), round(r * sin(t_aux) + dy)
      t_aux += teta
      puntos.append((x, y))
  return puntos 

def draw_poligono(puntos):
  l = len(puntos)
  points_direction = [ [ puntos[i], puntos[i + 1 if i < l - 1 else 0] ] for i in range(l) ]
  ymax = max( [ y for x, y in puntos ] ) 
  points_lines = [ j for i in points_direction for j in line(i[0], i[1]) ]  
  paint_lines(points_lines) 
  values_x = []
  for vy in range(ymax):
    values_x = [ x for (x, y) in points_lines if y == vy ]
    if len(values_x) == 0: continue
    for xp in range(min(values_x), max(values_x)):
      draw_point((xp, vy))
    values_x = []
  imprimir_linea()

def validar_poligono(poligono):
  if len(poligono) == 0: 
    print('Debe crear un poligono primeramente')
    return False
  return True

def draw_poligono_msj(poligono,  msj):
  print(poligono)
  print(msj)
  draw_poligono(poligono)

def menu():
    poligono = []
    while True:
        op = int(input('\nSeleccione una opción:\n1. Crear poligono\n2. Aplicar traslación\n3. Aplicar Escalado\n4. Aplicar Rotación\n5. Salir\n'))
        if op == 5: return
        elif op == 1:
          n = int(input('Introduce el número de lados: '))
          if n < 3: 
            print('El número de lados debe ser mayor a 3')
            break
          else:
            r = int(input('Introduce el valor del radio: '))
            if r > 0: poligono = generar_poligono(n, r)
            else: 
              print('El valor del radio debe ser positivo')
              break
          draw_poligono_msj(poligono, 'El poligono creado es:\n')
        elif op == 2:
          if validar_poligono(poligono):
            t = tuple(list(map(int, input('Introduce el vector de traslación: ').split())))
            poligono_trasladado = [ traslacion(p, t) for p in poligono ]
            draw_poligono_msj(poligono_trasladado, 'El poligono trasladado creado es: ')
        elif op == 3:
          if validar_poligono(poligono):
            e = tuple(list(map(int, input('Introduce el vector de escalado: ').split())))
            pf = poligono[0]
            poligono_escalado = [ escalado(p, pf, e) for p in poligono ]
            draw_poligono_msj(poligono_escalado, 'El poligono escalado es: ')
        elif op == 4:
          if validar_poligono(poligono):
            pf = tuple(list(map(int, input('Introduce la coordenada del punto de referencia: ').split())))
            teta = int(input('Introduce el ángulo: '))
            poligono_rotado = [ rotacion(p, pf, teta) for p in poligono ] 
            draw_poligono_msj(poligono_rotado, 'El poligono rotado es: ')
        else: 
          print('Seleccione correctamente')
          
if '__main__' == '__main__':
  menu()