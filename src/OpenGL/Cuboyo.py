import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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


def rotar():
    glutPostRedisplay()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glPushMatrix()
    glRotatef(theta, 1.0, 1.0, 1.0)
    cubo(-0.5, 0.5, 0.5)
    glPopMatrix()
    glutSwapBuffers()


def main():
    print('hola mundo')
    glutInit()  # Iniciamos la instancia de glut
    # Asignamos el modelo de color que usaremos
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    # Damos el tamaño de la ventana que se mostrará
    glutInitWindowSize(600, 600)
    # Coordenadas en donde aparecerá la venta en la pantalla
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Cubo")  # Damos un titulo para la ventana
    glClearColor(0, 0, 0, 1)
    glColor3f(1, 1, 1)
    glEnable(GL_DEPTH_TEST)
    # Designamos la función que contiene los elemntos que serán mostrados en la escena
    glutDisplayFunc(showScreen)
    glutIdleFunc(rotar)
    glutMainLoop()  # Iniciamos el loop principal
    return 0

main()
