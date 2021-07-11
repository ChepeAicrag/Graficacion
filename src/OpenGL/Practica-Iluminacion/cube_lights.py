import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from PIL import Image
import numpy as np # Numpy para manejar los vectores
from math import cos, sin, radians # Math para las operaciones trigonometricas

window = None # Objeto de la ventana
w, h = 500, 500 # Tamaño de la ventana
theta = 0 # Ángulo de rotación

position = np.array([0.0, 0, 3.0]) # Vector de posición de la cámara
front =  np.array([0.0, 0.0, -1.0]) # Vector de dirección de la cámara
up =  np.array([0.0, 1.0, 0.0]) # Vector up de la cámara
right =  np.array([1.0, 0.0, 0.0]) # Vector rigth de la cámara
worldUp =  np.array([0.0, 1.0, 0.0]) # Vector constante de orientación

lightAmbient = np.array([0.0, 0.0, 1.0])
lightSpecular = np.array([1.0, 1.0, 1.0])
lightDiffuse = np.array([1.0, 1.0, 1.0])
lightPosition = np.array([1.0, 1.0, 1.0])


mouse = (w / 2, h / 2, None) # Información del mouse (x, y, botón oprimido)
yaw, pitch = -90.0, 0 # Yaw representa la magnitud que estamos mirando hacia la izquierda o hacia la derecha.
# Pitch es el ángulo que representa cuánto miramos hacia arriba o hacia abajo como se ve en la primera imagen.
sx, sy = 0, 0 # Control del desplazamiento en x, y


def loadTexture(name):
    texture = Image.open(name)
    textureData = texture.convert('RGBA').tobytes()
    width = texture.width
    height = texture.height
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    return texid

def square(x, y, z, i, c):
    # r, g, b = c
    loadTexture(c)
    glBegin(GL_QUADS)
    # glColor3f(r, g, b)
    if i == 0:
        glTexCoord3f(0.0, 0.0, 0.0)
        glVertex3f(x, y, z)
        glTexCoord3f(1.0, 0.0, 0.0)
        glVertex3f(-x, y, z)
        glTexCoord3f(1.0, 1.0, 0.0)
        glVertex3f(-x, -y, z)
        glTexCoord3f(0.0, 1.0, 0.0)
        glVertex3f(x, -y, z)
        ab = np.array([-x, -y, z]) - np.array([-x, y , z])
        ac = np.array([x, y, z]) - np.array([-x, y, z])
        normal = np.cross(ab, ac)
        glNormal3fv(normal)
    elif i == 1:
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x, y, z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x, y, -z)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x, -y, -z)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x, -y, z)
        ab = np.array([-x, -y, z]) - np.array([-x, y , z])
        ac = np.array([x, y, z]) - np.array([-x, y, z])
        normal = np.cross(ab, ac)
        glNormal3fv(normal)
    elif i == 2:
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x, y, z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-x, y, z)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-x, y, -z)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x, y, -z)
        ab = np.array([-x, -y, z]) - np.array([-x, y , z])
        ac = np.array([x, y, z]) - np.array([-x, y, z])
        normal = np.cross(ab, ac)
        glNormal3fv(normal)
    glEnd()



def cube(x, y, z):
    square(x, y, z, 0, 'wall.jpg')
    square(x, y, -z, 0, '2.jpg')
    square(x, y, z, 1, '3.jpg')
    square(-x, y, z, 1, '4.png')
    square(x, y, z, 2, '5.jpg')
    square(x, -y, z, 2, '6.jpg')

def setMaterial(ambientR, ambientG, ambientB, diffuseR, diffuseG, diffuseB, specularR, specularG, specularB, shininess):
    ambient = (ambientR, ambientG, ambientB)
    diffuse = (diffuseR, diffuseG, diffuseB)
    specular = (specularR, specularG, specularB)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)


def iluminacion():
    light_ambient = (0.1, 0.1, 0.1, 1.0)
    light_diffuse = (1.0, 1.0, 1.0, 1.0)
    light_specular = (1.0, 1.0, 1.0, 1.0)
    light_position = (10.0, 10.0, 0.0, 0.0)

    glEnable(GL_LIGHTING)
    glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, light_ambient)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

def turn():
    global theta
    theta = theta + 0.10
    theta = theta >= 360 if 0 else theta
    glutPostRedisplay()

def move_mouse(button, mode, x, y):
    global mouse
    mouse = (x, y, button) if mode == GLUT_DOWN else (x, y, None)

def calc_move_mouse(x, y):
    global mouse, yaw, pitch, front, right, up, sx, sy
    x_m, y_m, button = mouse
    if button == GLUT_LEFT_BUTTON:
        sx = (x - x_m) * 0.2 # Sensibilidad 
        sy = (y_m - y) * 0.2 # Sesinbilidad
    yaw += sx # 
    pitch += sy # Inclinacion
    # Validaciones
    if pitch > 89.9:
        pitch = 89.9
    if pitch < -89.9:
        pitch = -89.9
    # Calculamos dirección actual
    direction = [
        cos(radians(yaw)) * cos(radians(pitch)),
        sin(radians(pitch)),
        sin(radians(yaw)) * cos(radians(pitch))
    ]
    fv = np.array(direction) # Creas el vector de dirreción actual
    front =  fv / np.linalg.norm(fv) # Usamos numpy para normalizar el vector de dirección
    v = np.cross(front, worldUp) # Calculas el vector de derecha con un producto cruz del vector dirreción y el 
    right = v / np.linalg.norm(v) # Noramlzias el vector calculado anteriormente
    v_up = np.cross(right, front) # Calcular el vector de up
    up = v_up / np.linalg.norm(v_up) # Normalizar el vector de up

    mouse = x, y, None # Guardamos las posiciones del mouse
    glutPostRedisplay() 

def move(key, x, y):
    global window, position, up, front, right
    move = 0.5 # velocidad de movimiento de la cámara
    key = key.decode('utf-8')
    if (key == 'f'):
        glutDestroyWindow(window) # Termina la ejecución
        return 0
    elif (key == 'w'):
        position += (move * front) # Mueves hacia arriba
    elif (key == 's'):
        position -= (move * front) # Mueves hacia abajo
    elif (key == 'a'):
        position -= right * move # Mueves hacia la izquierda
    elif (key == 'd'):
        position += right * move # Mueves hacia la derecha
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)  # Seleccionamos la matriz de proyección
    glLoadIdentity()  # Limpiamos la matriz seleccionada
    gluPerspective(120.0, float(w)/float(h), 1, 100) # Se genera la perspectiva
    glMatrixMode(GL_MODELVIEW)  # Seleccionamos la matriz del modelo
    glLoadIdentity()  # Limpiamos la matrxiz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    suma = np.array(position + front) # Calculamos el vector de dirección
    gluLookAt(position[0], position[1], position[2], suma[0], suma[1], suma[2], up[0], up[1], up[2]) # Posicionamiento de la cámara
    # glRotatef(theta, 1, 1, 1)
    setMaterial(0, 0, 0, 0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 1)
    cube(-1, 1, 1)
    iluminacion()
    glutSwapBuffers()

def main():
    global window
    glutInit()  # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(w, h)  # Damos el tamaño de la ventana que se mostrará
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Cubo con OpenGL")  # Damos un titulo para la ventana
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_BLEND)
    glEnable(GL_LIGHTING)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lightAmbient)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, lightAmbient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightDiffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightSpecular)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(move)
    glutMouseFunc(move_mouse)
    glutMotionFunc(calc_move_mouse)
    glutIdleFunc(turn)
    glutMainLoop()  # Iniciamos el loop principal

main()
