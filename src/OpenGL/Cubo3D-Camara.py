import OpenGL
import OpenGL.GL  
import OpenGL.GLUT  
import OpenGL.GLU  
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import pyrr
import glfw
import math

 
cameraPos = pyrr.Vector3([0.0, 0, 3.0])
cameraFront = pyrr.Vector3([0.0, 0.0, -1.0])
cameraUp = pyrr.Vector3([0.0, 1.0, 0.0])
cameraRight = pyrr.Vector3([1.0, 0.0, 0.0])

yaw = 0
pitch =0
cameraSpeed = 0.1
sesibilMouse=.15
mouseButtonPressed= None
oldMousePos = [ 0, 0 ]

window = 0


#Variables para la rotacion
ejeX = 0.0
ejeY = 0.0
ejeZ = 0.0

contador = 0
 
  
def InitGL(Width, Height): 
 
        glClearColor(0.0, 0.0, 0.0, 0.0) #Limpiar el buffer de color
        glClearDepth(1.0)  #Limpiar el bufer profundidad
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST) #Activa el buffer de profundidad
        #glEnable(GL_CULL_FACE)
        glShadeModel(GL_SMOOTH)  #Cambia el estilo del sombreado
        glMatrixMode(GL_PROJECTION) #Seleccionamos la matriz de proyeccion
        glLoadIdentity() #Cargamos la matriz identidad
        gluPerspective(90.0, float(Width)/float(Height), 1, 100)#Utilizamos una proyeccion en perspectiva
        #glOrtho(-3.3, 3.33,-2.5, 2.5 , -10.0, 100.0) #Hacemos una proyeccion ortogonal
        glMatrixMode(GL_MODELVIEW)#Cambiamos a la matriz para modelar el cubo

def cube():     
    glBegin(GL_QUADS)
 
    glColor3f(1,.07,.07)#Color Rojo
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0) 
 
    glColor3f(0.301, 0.058, 0.058)#Color cafe
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0) 
 
    glColor3f(0.219, 0.698, 0.388)#Color verde
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
 
    glColor3f(0.866, 0.890, 0.109) #Color amarilo
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)
 
    glColor3f(0.654, 0.184, 0.509)  #Color morado
    glVertex3f(-1.0, 1.0, 1.0) 
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0) 
    glVertex3f(-1.0,-1.0, 1.0) 
 
    glColor3f(0.247, 0.243, 0.658) #Color Azul
    glVertex3f( 1.0, 1.0,-1.0) 
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glEnd()

def keyPressed ( key, x, y) :
    global cameraPos,cameraFront,cameraUp,yaw,pitch

    if (key == GLUT_KEY_UP):
        cameraPos = cameraPos + (cameraSpeed * cameraFront)
    if (key == GLUT_KEY_DOWN):
        cameraPos = cameraPos - (cameraSpeed * cameraFront)
    if (key == GLUT_KEY_LEFT):
        cameraPos = cameraPos - pyrr.vector.normalise(pyrr.vector3.cross(cameraFront,cameraUp)) * cameraSpeed
    if (key == GLUT_KEY_RIGHT):
        #cameraPos += glm::normalize(glm::cross(cameraFront, cameraUp)) * cameraSpeed
        cameraPos = cameraPos + pyrr.vector.normalise(pyrr.vector3.cross(cameraFront,cameraUp))* cameraSpeed
    

    glutPostRedisplay( )

def mouseButton( button, mode, x, y ):
	
        global oldMousePos
        global mouseButtonPressed
        
        if mode == GLUT_DOWN:
             mouseButtonPressed = button
        else:
	        mouseButtonPressed = None
        oldMousePos[0], oldMousePos[1] = x, y
        glutPostRedisplay( )


def mouseMotion( x, y ):
    global  oldMousePos
    global translationScale
    global rY,rX,tY,tX , yaw, pitch , sesibilMouse
    global cameraPos,cameraFront,cameraUp,cameraRight

    deltaX = x - oldMousePos[ 0 ]
    deltaY = y - oldMousePos[ 1 ]

    print("x: " + str(x))
    print("y: " + str(y))

    if mouseButtonPressed == GLUT_LEFT_BUTTON:
        tX = deltaX * sesibilMouse
        tY = deltaY * sesibilMouse

    yaw += tX
    pitch += tY

    if pitch > 89.9:
        pitch = 89.9
    if pitch < -89.9:
        pitch = -89.9


    front = pyrr.Vector3([0.0, 0.0, 0.0])
    front.x = math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))
    front.y = math.sin(math.radians(pitch))
    front.z = math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))

    cameraFront = pyrr.vector.normalise(front)
    cameraRight = pyrr.vector.normalise(pyrr.vector3.cross(cameraFront, pyrr.Vector3([0.0, 1.0, 0.0])))
    

    oldMousePos[0], oldMousePos[1] = x, y

    glutPostRedisplay( )
def showScreen():

        global ejeX,ejeY,ejeZ,contador

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #limpiamos los buffers 
        glLoadIdentity() #Cargamos la matriz identitad 

        sum= pyrr.Vector3(cameraPos + cameraFront)
        gluLookAt(cameraPos.x,cameraPos.y,cameraPos.z, sum.x,sum.y,sum.z,cameraUp.x,cameraUp.y,cameraUp.z)
        
        
        cube() # Dibujar el cubo 

        '''ejeX = ejeX - 0.90 # disminuimos el Angulo de rotacion para cada eje
        ejeZ = ejeZ - 0.90 # cada vez que se hace una iteración
        ejeY = ejeY - 0.90 '''
        
        
        glutSwapBuffers() # dibuja el contenido actual de los buffers 
        #time.sleep(.05)  # Delay para rotar lento
 
 
 
def main():
 
        global window
 
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640,480)  #Definir el tamaño de la ventana
        glutInitWindowPosition(200,200)  #Definir la posicion de la ventana

        window = glutCreateWindow('Cubo 3D con rotacion- Graficacion')
 
        glutDisplayFunc(showScreen) # Definimos la funcion que pintara la matriz
        glutIdleFunc(showScreen) # Definimos que funcion repintara la matriz
        glutSpecialFunc( keyPressed )
        glutMouseFunc( mouseButton )
        glutMotionFunc(mouseMotion)
        InitGL(640, 480) # Metodo que inicializa parametros
        glutMainLoop()
 
if __name__ == "__main__":
        main() 
