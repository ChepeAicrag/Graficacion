
import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

window = None
w, h = 500, 500
theta = 0
rx, px = 3, 0
ry, py = -6, 0
rz, pz = 0, -1

cameraPos = np.array([0.0, 0, 3.0])
cameraFront =  np.array([0.0, 0.0, -1.0])
cameraUp =  np.array([0.0, 1.0, 0.0])
cameraRight =  np.array([1.0, 0.0, 0.0])

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

def move(key, x, y):
    global ry, rx, rz, px, py, pz
    move = 0.5
    key = key.decode('utf-8')
    print(key)
    if (key == 'f'):
        global window, cameraPos, cameraUp, cameraFront
        glutDestroyWindow(window)
        return 0
    if (key == 'j'):
        cameraFront[0] -= move
    elif (key == 'i'):
        cameraFront[1] += move
    elif (key == 'k'):
        cameraFront[1] -= move
    elif (key == 'l'):
        cameraFront[0] += move
    
    elif (key == 'w'):
        cameraPos += (move * cameraFront)
        # rz += move
    elif (key == 's'):
        # rz -= move
        cameraPos -= (move * cameraFront)
    elif (key == 'a'):
        # rx -= move
        v = np.cross(cameraFront, cameraUp)
        cameraPos -= v / np.linalg.norm(v) * move
    elif (key == 'd'):
        # rx += move
        v = np.cross(cameraFront, cameraUp)
        cameraPos += v / np.linalg.norm(v) * move
    
    if cameraPos[1] > 89.9:
        cameraPos[1] = 1
    if cameraPos[1] < -89.9:
        cameraPos[1] = 1

    cameraFront =  cameraFront / np.linalg.norm(cameraFront)

    v = np.cross(cameraFront, np.array([0.0, 1.0, 0.0]))
    cameraRight = v / np.linalg.norm(v)

    glutPostRedisplay()

def iterate():
    k = 5
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
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
    # gluLookAt(rx, ry, rz, px, py, pz, 0, 0, 1)
    suma = np.array(cameraPos + cameraFront)
    print(cameraFront)
    gluLookAt(cameraPos[0], cameraPos[1], cameraPos[2], suma[0], suma[1], suma[2], cameraUp[0], cameraUp[1], cameraUp[2])
    cube(-1, 1, 1)
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
    glutKeyboardFunc(move)
    glutMainLoop()  # Iniciamos el loop principal

main()

