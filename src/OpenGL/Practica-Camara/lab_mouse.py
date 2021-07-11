import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np
from math import cos, sin, radians

window = None
w, h = 500, 500

position = np.array([0.0, 0, 3.0]) # Vector de posición de la cámara
front =  np.array([0.0, 0.0, -1.0]) # Vector de dirección de la cámara
up =  np.array([0.0, 1.0, 0.0]) # Vector up de la cámara
right =  np.array([1.0, 0.0, 0.0]) # Vector rigth de la cámara
worldUp =  np.array([0.0, 1.0, 0.0]) # Vector constante de orientación

mouse = (w / 2, h / 2, None) # Información del mouse (x, y, botón oprimido)
yaw, pitch = -90.0, 0 # Yaw representa la magnitud que estamos mirando hacia la izquierda o hacia la derecha.
# Pitch es el ángulo que representa cuánto miramos hacia arriba o hacia abajo como se ve en la primera imagen.
sx, sy = 0, 0 # Control del desplazamiento en x, y

laberinto = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
             [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
             [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
             [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def squad(x, y, z, n, i, c):
    r, g, b = c
    glBegin(GL_QUADS)
    glColor3f(r, g, b)
    if i == 0:
        glVertex3f(x, y, z)
        glVertex3f(x + n, y, z)
        glVertex3f(x + n, y - n, z)
        glVertex3f(x, y - n, z)
    elif i == 1:
        glVertex3f(x, y, z)
        glVertex3f(x, y, z - n)
        glVertex3f(x, y - n, z - n)
        glVertex3f(x, y - n, z)
    elif i == 2:
        glVertex3f(x, y, z)
        glVertex3f(x + n, y, z)
        glVertex3f(x + n, y, z - n)
        glVertex3f(x, y, z - n)
    glEnd()

def cubo(x, y, z, c):
    n = 1 / 11
    squad(x, y, z, n, 0, c)
    squad(x, y, z-n, n, 0, c)
    squad(x + n, y, z, n, 1, c)
    squad(x, y, z, n, 1, c)
    squad(x, y - n, z, n, 2, c)
    squad(x, y, z, n, 2, c)

def make_lab(matriz):
    n = 1 / 11
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            color = (0, 0, 0)
            if matriz[x][y] == 0:
                color = (1, 1, 1)
            cubo(y * n - 1, 1 - x * n, 1, color)

def move_mouse(button, mode, x, y):
    global mouse
    mouse = (x, y, button) if mode == GLUT_DOWN else (x, y, None)

def calc_move_mouse(x, y):
    global mouse, yaw, pitch, front, right, up, sx, sy
    x_m, y_m, button = mouse
    if button == GLUT_LEFT_BUTTON:
        sx = (x - x_m) * 0.2 # Sensibilidad 
        sy = (y_m - y) * 0.2 # Sesinbilidad
    yaw += sx # 
    pitch += sy # Inclinacion
    # Validaciones
    if pitch > 89.9:
        pitch = 89.9
    if pitch < -89.9:
        pitch = -89.9
    # Calculamos dirección actual
    direction = [
        cos(radians(yaw)) * cos(radians(pitch)),
        sin(radians(pitch)),
        sin(radians(yaw)) * cos(radians(pitch))
    ]
    fv = np.array(direction) # Creas el vector de dirreción actual
    front =  fv / np.linalg.norm(fv) # Usamos numpy para normalizar el vector de dirección
    v = np.cross(front, worldUp) # Calculas el vector de derecha con un producto cruz del vector dirreción y el 
    right = v / np.linalg.norm(v) # Noramlzias el vector calculado anteriormente
    v_up = np.cross(right, front) # Calcular el vector de up
    up = v_up / np.linalg.norm(v_up) # Normalizar el vector de up

    mouse = x, y, None # Guardamos las posiciones del mouse
    glutPostRedisplay() 

def move(key, x, y):
    global window, position, up, front, right
    move = 0.5 # velocidad de movimiento de la cámara
    key = key.decode('utf-8')
    if (key == 'f'):
        glutDestroyWindow(window) # Termina la ejecución
        return 0
    elif (key == 'w'):
        position += (move * front) # Mueves hacia arriba
    elif (key == 's'):
        position -= (move * front) # Mueves hacia abajo
    elif (key == 'a'):
        position -= right * move # Mueves hacia la izquierda
    elif (key == 'd'):
        position += right * move # Mueves hacia la derecha
    glutPostRedisplay()


def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    gluPerspective(120.0, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matrxiz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glPushMatrix()
    suma = np.array(position + front) # Calculamos el vector de dirección
    gluLookAt(position[0], position[1], position[2], suma[0], suma[1], suma[2], up[0], up[1], up[2]) # Posicionamiento de la cámara
    make_lab(laberinto)
    glPopMatrix()
    glutSwapBuffers()

def main():
    glutInit()  # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH) # Asignamos el modelo de color que usaremos
    glutInitWindowSize(600, 600) # Damos el tamaño de la ventana que se mostrará
    glutInitWindowPosition(0, 0) # Coordenadas en donde aparecerá la ventana en la pantalla
    glutCreateWindow("Laberinto en 3D")  # Damos un titulo para la ventana
    glEnable(GL_DEPTH_TEST) # Permite ver sin transparentar las figuras
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(move)
    glutMouseFunc(move_mouse)
    glutMotionFunc(calc_move_mouse)
    glutMainLoop()  # Iniciamos el loop principal

main()
