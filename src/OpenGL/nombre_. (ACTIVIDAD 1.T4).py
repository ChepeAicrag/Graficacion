
import OpenGL
import OpenGL.GL  
import OpenGL.GLUT  
import OpenGL.GLU  
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
rotate_y=0
rotate_x=0
rotate_z=0
angulo=0
w= 600
h=600
rx=0
ry=0
rz=0
px=0
py=0
pz=0

def Face(A,B,C,D):
    glBegin(GL_POLYGON)
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glVertex3fv(D)
    glEnd()
def Cube(V0,V1,V2,V3,V4,V5,V6,V7):
    #cafe
    glColor3f(.52,.42,.27)
    Face(V0,V1,V2,V3) #Enfrente
    #morado
    glColor3f(.81,.45,.97)
    Face(V4,V5,V6,V7) #atras
    #rojo
    glColor3f(0.8,0.02,.01)
    Face(V0,V4,V7,V3) #izquierda
    #verde
    glColor3f(.26,.77,.27)
    Face(V1,V5,V6,V2) #derecha
    #azul
    glColor3f(.05,0.08,.32)
    Face(V2,V3,V7,V6) #abajo
    #amarillo
    glColor3f(0.94,.9,.28)
    Face(V0,V1,V5,V4) #arriba

def Draw():
    V=   (
            (-5.5, 5.5, 5.5),
            ( 5.5, 5.5, 5.5),
            ( 5.5,-5.5, 5.5),
            (-5.5,-5.5, 5.5),
            (-5.5, 5.5,-5.5),
            ( 5.5, 5.5,-5.5),
            ( 5.5,-5.5,-5.5),
            (-5.5,-5.5,-5.5)
        )
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) """
    #glLoadIdentity()
    #glRotated(d,f,p,1) """
    """ glRotatef(rotate_x,1.0,0.0,0.0)
    glRotatef(rotate_y,0.0,1.0,0.0)
    glRotatef(rotate_z,0.0,0.0,1.0) """
    Cube(V[0],V[1],V[2],V[3],V[4],V[5],V[6],V[7])


def reshape(w,h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,h/w,1,300)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    glClearColor(0,0,0,0)
    glShadeModel(GL_FLAT)
    glEnable(GL_DEPTH_TEST)

def display():
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(-10+rx,9+ry,-10+rz,px,py,pz,0,1,0)
    #glPushMatrix()
    #i=-100
    """ for i in range(-100,100,1):
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_LINE_STRIP)
        glVertex3f(i,0,-100)
        glVertex3f(i,0,100)
        glEnd()
    for i in range(-100,100,1):
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_LINE_STRIP)
        glVertex3f(-100,0,i)
        glVertex3f(100,0,i)
        glEnd() """
    Draw()
    glFlush()
    glutSwapBuffers()
    

def mover(bkey, x, y):
    key = bkey.decode("utf-8")
    global rx,px,rz,pz,ry,rz,py
    global rotate_x
    global rotate_y
    global rotate_z
    #esc
    if (key==chr(58)):
        print('a')
    elif (key=='d'):
        rx=rx+0.2
    elif (key=='a'):
        rx=rx-0.2
    elif (key=='l'):
        px=px+0.8   
    elif (key=='j'):
        px=px-0.2
    elif (key=='q'):
        ry=ry+0.2
    elif (key=='e'):
        ry=ry-0.2        
    elif (key=='u'):
        py=py+0.2
    elif (key=='o'):
        py=py-0.2
    #1
    elif (key==chr(32)):
        ry=ry+0.2
        py=py+0.2
    #2    
    elif (key==chr(13)):
        ry=ry-0.2
        py=py-0.2
    elif (key=='w'):
        rz=rz+0.2
    elif (key=='s'):
        rz=rz-0.2
    elif (key=='i'):
        pz=pz+0.8
    elif (key=='k'):
        pz=pz-0.8

    glutPostRedisplay()

''' def keypressed(*args):
    key_esc=b'47'
    key_d=b'd'
    key_d=b'd'
    key_d=b'd'
    key_d=b'd' '''




def flechas(key,x,y):
    global rx,px,rz,pz,ry,rz,py
    if (key==GLUT_KEY_LEFT):
        rx=rx+0.2
        px=px+0.2  
    elif (key==GLUT_KEY_RIGHT):
        rx=rx-0.2
        px=px-0.2
    elif (key==GLUT_KEY_UP):
        rz=rz+0.2
        pz=pz+0.2
    elif (key==GLUT_KEY_DOWN):
        rz=rz-0.2
        pz=pz-0.2
    glutPostRedisplay()
def main():
    glutInit()
    glutInit(sys.argv)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(100,50)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("Cubo")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(mover)
    glutSpecialFunc(flechas)
    glutReshapeFunc(reshape)
    glutMainLoop()
    return 0    
main()      

    


    