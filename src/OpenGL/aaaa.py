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
 