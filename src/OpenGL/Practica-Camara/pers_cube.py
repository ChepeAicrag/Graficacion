"""
Solución de la actividad 1 T4
"""

import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = None
w, h = 500, 500
theta = 0
rx, px = 3, 0
ry, py = -6, 0
rz, pz = 0, 0


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


def turn():
    global theta
    theta = theta + 0.10
    theta = theta >= 360 if 0 else theta
    glutPostRedisplay()


def move(key, x, y):
    global ry, rx, rz, px, py, pz
    move = 0.20
    key = key.decode('utf-8')
    print(key)
    if (key == 'f'):
        global window
        glutDestroyWindow(window)
        return 0
    elif (key == 'j'):
        px -= move
    elif (key == 'i'):
        pz += move
    elif (key == 'k'):
        pz -= move
    elif (key == 'l'):
        px += move
    elif (key == 'w'):
        rz += move
        pz += move
    elif (key == 's'):
        rz -= move
        pz -= move
    elif (key == 'a'):
        rx -= move
        px -= move
    elif (key == 'd'):
        rx += move
        px += move
    elif (key == 'q'):
        ry -= move
        py -= move
    elif (key == 'e'):
        ry += move
        py += move
    glutPostRedisplay()


def iterate():
    k = 5
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    # glFrustum(-3, 3, -3, 3, 3, 10)
    gluPerspective(90.0, float(w)/float(h), 1, 100)
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
    print(rx, ry, rz)
    gluLookAt(rx, ry, rz, px, py, pz, 0, 0, 1)
    # gluLookAt(rx, ry, rz, px, py, pz, 0, 0, 1)
    # glRotatef(theta, 1, 1, 1)
    # glRotatef(theta, 0, 1, 0)
    # glRotatef(theta, 0, 0, 1)
    cube(-3, 3, 3)
    eje()
    glutSwapBuffers()

def main():
    glutInit()  # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(w, h)  # Damos el tamaño de la ventana que se mostrará
    glutInitWindowPosition(0, 0)
    global window
    window = glutCreateWindow("Cubo con OpenGL")  # Damos un titulo para la ventana
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showScreen)
    glutIdleFunc(turn)
    glutKeyboardFunc(move)
    glutMainLoop()  # Iniciamos el loop principal

main()

