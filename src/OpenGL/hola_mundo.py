import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500
theta = 45


def square():
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    # Definimos la proyección a usar como una ortogonal
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matriz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista


def showScreen():
    global theta
    theta = theta + 0.05
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    glRotatef(theta, 0.0, 0.0, 1.0)
    square()
    glutSwapBuffers()


def main():
    glutInit()  # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGBA)  # Asignamos el modelo de color que usaremos
    # Damos el tamaño de la ventana que se mostrará
    glutInitWindowSize(500, 500)
    # Coordenadas en donde aparecerá la venta en la pantalla
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Cubo en OpenGL")  # Damos un titulo para la ventana
    # Designamos la función que contiene los elemntos que serán mostrados en la escena
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()  # Iniciamos el loop principal


if __name__ == "__main__":
    main()
