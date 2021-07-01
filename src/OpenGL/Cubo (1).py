import OpenGL
import OpenGL.GL  
import OpenGL.GLUT  
import OpenGL.GLU  
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

theta=45
rx=0
ry=0
rz=0
def square1():     
    glBegin(GL_QUADS)
    glColor3f(0.1,0.0,0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glEnd()

def square2():     
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,1.0)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(0.5, 0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glEnd()

def square3():     
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glEnd()

def square4():     
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)
    glVertex3f(0.5,-0.5, 0.5)
    glEnd()

def square5():     
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)
    glEnd()

def square6():     
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glEnd()        

def cubo():
    square1()
    square2()
    square3()
    square4()
    square5()
    square6()
    global theta
    theta = theta + 0.20
    if(theta > 360):
        theta = 0

def rotar():
    glutPostRedisplay()

def showScreen():   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity() 
    glRotatef(theta,1.0,1.0,1.0)
    cubo()
    glutSwapBuffers()

def main():
    print('hola mundo')
    glutInit() # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB| GLUT_DOUBLE| GLUT_DEPTH) # Asignamos el modelo de color que usaremos   
    glutInitWindowSize(600, 600)   # Damos el tamaño de la ventana que se mostrará  
    glutInitWindowPosition(0, 0)   # Coordenadas en donde aparecerá la venta en la pantalla   
    glutCreateWindow("Cubo") # Damos un titulo para la ventana
    glClearColor(0,0,0,1)
    glColor3f(1,0,0)
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showScreen)  # Designamos la función que contiene los elemntos que serán mostrados en la escena 
    glutIdleFunc(rotar)     
    glutMainLoop()  # Iniciamos el loop principal
    return 0

main()