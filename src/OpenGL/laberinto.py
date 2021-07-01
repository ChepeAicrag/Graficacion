import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

theta = 0

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
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    if i == 0:
        glVertex3f(x, y, z)
        glVertex3f(x+n, y, z)
        glVertex3f(x+n, y+n, z)
        glVertex3f(x, y+n, z)
    elif i == 1:
        glVertex3f(x, y, z)
        glVertex3f(x, y, z+n)
        glVertex3f(x, y+n, z+n)
        glVertex3f(x, y+n, z)
    elif i == 2:
        glVertex3f(x, y, z)
        glVertex3f(x+n, y, z)
        glVertex3f(x+n, y, z+n)
        glVertex3f(x, y, z+n)
    glEnd()


def cubo(x, y, z, c):
    n = 1/11
    squad(x, y, z, n, 0, c)
    squad(x, y, z+n, n, 0, c)
    squad(x+n, y, z, n, 1, c)
    squad(x, y, z, n, 1, c)
    squad(x, y+n, z, n, 2, c)
    squad(x, y, z, n, 2, c)
    global theta
    theta = theta + 0.005
    if(theta > 360):
        theta = 0

def make_lab(matriz):
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            color = (0, 0, 0)
            if matriz[x][y] == 0:
                color = (1, 1, 1)
            cubo(y/11 - 1, 1 - x/11, 1 - x/11, color)

def rotar():
    glutPostRedisplay()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glPushMatrix()
    glRotatef(theta, 0.5, 0.5, 0.5)
    make_lab(laberinto)
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
    # glEnable(GL_DEPTH_TEST)
    # Designamos la función que contiene los elemntos que serán mostrados en la escena
    glutDisplayFunc(showScreen)
    glutIdleFunc(rotar)
    glutMainLoop()  # Iniciamos el loop principal
    return 0

main()
