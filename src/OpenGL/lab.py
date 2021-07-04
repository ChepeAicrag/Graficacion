import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500
rotate_x = 3
rotate_y = -6
rotate_z = 0

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

def square(x, y, z, n, i, c):
    r, g, b = c
    glBegin(GL_QUADS)
    glColor3f(r, g, b)
    if i == 0:
        glVertex3f(x, y, z)
        glVertex3f(x + n, y, z)
        glVertex3f(x + n, y + n, z)
        glVertex3f(x, y + n, z)
    elif i == 1:
        glVertex3f(x, y, z)
        glVertex3f(x, y, z + n)
        glVertex3f(x, y + n, z + n)
        glVertex3f(x, y + n, z)
    elif i == 2:
        glVertex3f(x, y, z)
        glVertex3f(x + n, y, z)
        glVertex3f(x + n, y, z + n)
        glVertex3f(x, y, z + n)
    glEnd()

def cube(x, y, z, n, c):
    square(x, y, z, n, 0, c)
    square(x, y, z + n, n, 0, c)
    square(x + n, y, z, n, 1, c)
    square(x, y, z, n, 1, c)
    square(x, y, z, n, 2, c)
    square(x, y + n, z, n, 2, c)

def make_lab(matriz):
    n = 1 / 11
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            color = (0, 0, 0)
            if matriz[x][y] == 0:
                color = (1, 1, 1)
            cube(y * n - 1, 1 - x * n, 1 - x * n, n, color)

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


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    # gluPerspective(120, 1, 1, 40)   
    glFrustum(-1, 1, -1, 1, 2, 10)
    glPushMatrix()
    gluLookAt(rotate_x, rotate_y, rotate_z, 0, 0, 0, 1, 0, 0)
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
    glutDisplayFunc(showScreen) # Designamos la función que contiene los elementos que serán mostrados en la escena
    glutKeyboardFunc(mover)
    glutMainLoop()  # Iniciamos el loop principal

main()
