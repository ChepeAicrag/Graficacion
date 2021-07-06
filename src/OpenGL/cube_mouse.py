
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
    glutMouseFunc(move_mouse)
    glutMotionFunc(calc_move_mouse)
    glutMainLoop()  # Iniciamos el loop principal

main()

