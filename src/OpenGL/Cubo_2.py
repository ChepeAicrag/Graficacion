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

# from pynput import keyboard as kb

# def pulsa(tecla):
# 	print('Se ha pulsado la tecla ' + str(tecla))

# with kb.Listener(pulsa) as escuchador:
# 	escuchador.join()

w, h = 500, 500
theta = 45

def squad(x, y, z, i, c):
    r, g, b = c
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
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

def cubo(x, y, z):

    # Cara de A, B, C, D (x, y, z), (x-y, z), (x-y-z), (x, y-z)
    squad(x, y, z, 0, (0.1, 0.0, 0.0)) # Cafe

    # Cara de E, F, G, H (x, y, z-n), (x-y, z-n), (x-y-z-n), (x, y-z-n)
    squad(x, y, -z, 0, (1.0, 0.0, 1.0))

    # Cara de B, F, G, C (x-y, z), (x-y, z-n), (x-y-z-n), (x-y-z)
    squad(-x, y, z, 1, (1.0, 0.0, 0.0))

    # Cara de A, E, H, D (x, y, z), (x, y, z-n), (x, y-z-n), (x, y-z)
    squad(x, y, z, 1, (0.0, 1.0, 0.0))

    # Cara de D, C, G, H (x, y-z), (x-y-z), (x-y-z-n), (x, y-z-n)
    squad(x, -y, z, 2, (0.0, 0.0, 1.0))

    # Cara de A, B, F, E (x, y, z), (x-y, z), (x-y, z-n), (x, y, z-n)
    squad(x, y, z, 2, (1.0, 1.0, 0.0))

    global theta
    theta = theta + 0.20
    if(theta > 360):
        theta = 0

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    # Definimos la proyección a usar como una ortogonal
    #glOrtho(-5, 5, -5, 5, -5, 10)
    #glOrtho(-0.5, 0.5, -0.5, 0.5, -0.05, 10)
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matriz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glPushMatrix()
    #glRotatef(theta, 0.5, 0.5, 0.5)
    glRotatef(theta, 1, 1, 1)
    cubo(1, 1, 1)
    glPopMatrix()
    glutSwapBuffers()

def main():
    glutInit()  # Iniciamos la instancia de glut
    # Asignamos el modelo de color que usaremos
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    # Damos el tamaño de la ventana que se mostrará
    glutInitWindowSize(w, h)
    # Coordenadas en donde aparecerá la venta en la pantalla
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Cubo")  # Damos un titulo para la ventana
    glClearColor(0, 0, 0, 1)
    glColor3f(0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    # Designamos la función que contiene los elemntos que serán mostrados en la escena
    glutDisplayFunc(showScreen)
    glutIdleFunc(glutPostRedisplay)
    glutMainLoop()  # Iniciamos el loop principal
    return 0

main()
