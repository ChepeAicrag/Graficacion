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

cameraPos = np.array([0.0, 0, 3.0])
cameraFront =  np.array([0.0, 0.0, -1.0])
cameraUp =  np.array([0.0, 1.0, 0.0])
cameraRight =  np.array([1.0, 0.0, 0.0])
worldUp =  np.array([0.0, 1.0, 0.0])

mouse = (w / 2, h / 2, None)
yaw, pitch = -90.0, 0
sx, sy = 0, 0

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
    global mouse, yaw, pitch, cameraFront, cameraRight, cameraUp, sx, sy
    x_m, y_m, button = mouse
    if button == GLUT_LEFT_BUTTON:
        sx = (x - x_m) * 0.2
        sy = (y_m - y) * 0.2
    yaw += sx
    pitch += sy
    if pitch >= 90:
        pitch = 89.9
    if pitch <= -90:
        pitch = -89.9
    direction = [
        cos(radians(yaw)) * cos(radians(pitch)),
        sin(radians(pitch)),
        sin(radians(yaw)) * cos(radians(pitch))
    ]
    fv = np.array(direction) 
    cameraFront =  fv / np.linalg.norm(fv)
    v = np.cross(cameraFront, worldUp)
    cameraRight = v / np.linalg.norm(v)
    v_up = np.cross(cameraRight, cameraFront)
    cameraUp = v_up / np.linalg.norm(v_up)

    mouse = x, y, None
    glutPostRedisplay( )
    print(x, y)
    print(mouse)

def move(key, x, y):
    global window, cameraPos, cameraUp, cameraFront, cameraRight
    move = 0.5
    key = key.decode('utf-8')
    print(key)
    if (key == 'f'):
        glutDestroyWindow(window)
        return 0

    elif (key == 'w'):
        cameraPos += (move * cameraFront)
    elif (key == 's'):
        cameraPos -= (move * cameraFront)
    elif (key == 'a'):
        cameraPos -= cameraRight * move
    elif (key == 'd'):
        cameraPos += cameraRight * move
    glutPostRedisplay()


def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    # glFrustum(-1, 1, -1, 1, 2, 10)
    gluPerspective(70.0, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matrxiz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glPushMatrix()
    suma = np.array(cameraPos + cameraFront)
    gluLookAt(cameraPos[0], cameraPos[1], cameraPos[2], suma[0], suma[1], suma[2], cameraUp[0], cameraUp[1], cameraUp[2])
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
