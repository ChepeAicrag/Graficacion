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

w, h = 500, 500
theta = 0

rotate_x = 3
rotate_y = -6
rotate_z = 0

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
    theta = theta + 0.05
    theta = theta >= 360 if 0 else theta
    glutPostRedisplay()

def mover(key, x, y):
    global rotate_y
    global rotate_x
    global rotate_z
    move = 0.10 
    key = key.decode('utf-8')
    print(key)
    if (key == 'f'):
        return 0
    elif (key == 'Y'):
        rotate_y = rotate_y + move
    elif (key == 'y'):
        rotate_y = rotate_y - move
    elif (key == 'X'):
        rotate_x = rotate_x + move
    elif (key == 'x'):
        rotate_x = rotate_x - move
    elif (key == 'Z'):
        rotate_z = rotate_z + move
    elif (key == 'z'):
        rotate_z = rotate_z - move

    glutPostRedisplay()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    # Definimos la proyección a usar como una ortogonal
    # glOrtho(-5, 5, -5, 5, 5, -5)
    # glLoadIdentity()  # Limpiamos la matriz seleccionada
    # glFrustum(-1, 1, -1, 1, 2, 10)
    gluPerspective(120, 1, 1, 400)
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matrxiz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glPushMatrix()
    print(rotate_x, rotate_y, rotate_z)
    gluLookAt(rotate_x, rotate_y, rotate_z, 0, 0, 0, 0, 0, 1)
    glRotatef(theta, 1, 1, 1)
    cube(-1, 1, 1)
    glPopMatrix()
    glutSwapBuffers()

def main():
    glutInit()  # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(w, h)  # Damos el tamaño de la ventana que se mostrará
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Cubo con OpenGL")  # Damos un titulo para la ventana
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(mover)
    glutIdleFunc(turn)
    glutMainLoop()  # Iniciamos el loop principal

main()
