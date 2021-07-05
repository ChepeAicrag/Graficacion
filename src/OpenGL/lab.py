import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500
rx, px = 3, 0
ry, py = -6, 0
rz, pz = 0, 0

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

def mover(key, x, y):
    global ry
    global rx
    global rz
    global px 
    global py 
    global pz 

    move = 0.10 
    key = key.decode('utf-8')
    print(key)
    if (key == 'f'):
        exit(0)
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
        x -= move
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
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    glFrustum(-1, 1, -1, 1, 2, 10)
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matrxiz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # gluPerspective(120, 1, 1, 40)   
    glPushMatrix()
    gluLookAt(rx, ry, rz, px, py, pz, 0, 0, 1)
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
