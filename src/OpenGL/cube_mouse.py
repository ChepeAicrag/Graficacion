import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np # Numpy para manejar los vectores
from math import cos, sin, radians # Math para las operaciones trigonometricas

window = None # Objeto de la ventana
w, h = 500, 500 # Tamaño de la ventana

position = np.array([0.0, 0, 3.0]) # Vector de posición de la cámara
front =  np.array([0.0, 0.0, -1.0]) # Vector de dirección de la cámara
up =  np.array([0.0, 1.0, 0.0]) # Vector up de la cámara
right =  np.array([1.0, 0.0, 0.0]) # Vector rigth de la cámara
worldUp =  np.array([0.0, 1.0, 0.0]) # Vector constante de orientación

mouse = (w / 2, h / 2, None) # Información del mouse (x, y, botón oprimido)
yaw, pitch = -90.0, 0 # Yaw representa la magnitud que estamos mirando hacia la izquierda o hacia la derecha.
# Pitch es el ángulo que representa cuánto miramos hacia arriba o hacia abajo como se ve en la primera imagen.
sx, sy = 0, 0 # Control del desplazamiento en x, y

def square(x, y, z, i, c):
    r, g, b = c
    glBegin(GL_QUADS)
    glColor3f(r, g, b)
    if i == 0:
        glVertex3f(x, y, z)
        glVertex3f(-x, y, z)
        glVertex3f(-x, -y, z)
        glVertex3f(x, -y, z)
    elif i == 1:
        glVertex3f(x, y, z)
        glVertex3f(x, y, -z)
        glVertex3f(x, -y, -z)
        glVertex3f(x, -y, z)
    elif i == 2:
        glVertex3f(x, y, z)
        glVertex3f(-x, y, z)
        glVertex3f(-x, y, -z)
        glVertex3f(x, y, -z)
    glEnd()


def cube(x, y, z):
    square(x, y, z, 0, (1.0, 0.0, 0.0))
    square(x, y, -z, 0, (0.34, 0.14, 0.39))
    square(x, y, z, 1, (0.5, 0.25, 0.0))
    square(-x, y, z, 1, (0.0, 1.0, 0.0))
    square(x, y, z, 2, (1.0, 1.0, 0.0))
    square(x, -y, z, 2, (0.0, 0.0, 1.0))

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
    gluPerspective(120.0, float(w)/float(h), 1, 100) # Se genera la perspectiva
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matrxiz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista

def eje():
    n = 100
    # Eje y-
    glColor3f(0, 1, 0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0, 0, 0)
    glVertex3f(0, n, 0)
    glEnd()
    # Eje x
    glColor3f(1, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0, 0, 0)
    glVertex3f(n, 0, 0)
    glEnd()
    # Eje z
    glColor3f(0, 0, 1)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, n)
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    suma = np.array(position + front) # Calculamos el vector de dirección
    gluLookAt(position[0], position[1], position[2], suma[0], suma[1], suma[2], up[0], up[1], up[2]) # Posicionamiento de la cámara
    cube(-1, 1, 1)
    eje()
    glutSwapBuffers()

def main():
    global window
    glutInit()  # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(w, h)  # Damos el tamaño de la ventana que se mostrará
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Cubo con OpenGL")  # Damos un titulo para la ventana
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(move)
    glutMouseFunc(move_mouse)
    glutMotionFunc(calc_move_mouse)
    glutMainLoop()  # Iniciamos el loop principal

main()

