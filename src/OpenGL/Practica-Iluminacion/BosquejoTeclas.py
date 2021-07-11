import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from threading import Thread
from time import sleep
import numpy as np
from math import *

theta = 45
y1 = 1
z1 = 1
zoomIn = 1
zoomOut = 1
arriba = 1
abajo = 1
izquierda = 1
derecha = 1
mirarDerecha = 1
mirarIzquierda = 1
mirarAbajo = 1
mirarArriba = 1


def cube():
    glBegin(GL_QUADS)

    #Piso
    ab = np.array((-2.31, 0.0, -2.04))  - np.array((-2.31, 0.0, 5.66))
    ac = np.array((5.39, 0.0, 5.66))  - np.array((-2.31, 0.0, 5.66))
    normal = np.cross(ab, ac)

    glNormal3fv(normal)
    glColor3f(1.0, 0.62, 0.47)
    glVertex3f(5.39, 0.0, 5.66)
    glVertex3f(-2.31, 0.0, 5.66)
    glVertex3f(-2.31, 0.0, -2.04)
    glVertex3f(5.39, 0.0, -2.04)

    #SECCION PARED SALA SIN VENTANA
    # Exterior
    ab = np.array((5.39, 2.4, 1.71)) - np.array((5.39, 0.0, 1.71))
    ac = np.array((5.39, 0.0, 5.66)) - np.array((5.39, 0.0, 1.71))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, 5.66)
    glVertex3f(5.39, 0.0, 1.71)
    glVertex3f(5.39, 2.4, 1.71)
    glVertex3f(5.39, 2.4, 5.66)

    # Interior
    ab = np.array((5.27, 2.4, 1.71)) - np.array((5.27, 0.0, 1.71))
    ac = np.array((5.27, 0.0, 5.54)) - np.array((5.27, 0.0, 1.71))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 0.0, 5.54)
    glVertex3f(5.27, 0.0, 1.71)
    glVertex3f(5.27, 2.4, 1.71)
    glVertex3f(5.27, 2.4, 5.54)

    #Union Parte arriba
    ab = np.array((5.27, 2.4, 1.71)) - np.array((5.39, 2.4, 1.71))
    ac = np.array((5.39, 2.4, 5.66)) - np.array((5.39, 2.4, 1.71))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.4, 5.66)
    glVertex3f(5.39, 2.4, 1.71)
    glVertex3f(5.27, 2.4, 1.71)
    glVertex3f(5.27, 2.4, 5.54)
    #FIN SECCION

    #SECCION PARED SIN VENTANA HABITACIÓN MORADA
    # Exterior
    ab = np.array((2.73, 2.4, -2.04)) - np.array((2.73, 0.0, -2.04))
    ac = np.array((5.39, 0.0, -2.04)) - np.array((2.73, 0.0, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, -2.04)
    glVertex3f(2.73, 0.0, -2.04)
    glVertex3f(2.73, 2.4, -2.04)
    glVertex3f(5.39, 2.4, -2.04)

    # Interior
    ab = np.array((2.73, 2.4, -1.92)) - np.array((2.73, 0.0, -1.92))
    ac = np.array((5.27, 0.0, -1.92)) - np.array((2.73, 0.0, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 0.0, -1.92)
    glVertex3f(2.73, 0.0, -1.92)
    glVertex3f(2.73, 2.4, -1.92)
    glVertex3f(5.27, 2.4, -1.92)

    # Union parte arriba
    ab = np.array((2.73, 2.4, -1.92)) - np.array((2.73, 2.4, -2.04))
    ac = np.array((5.39, 2.4, -2.04)) - np.array((2.73, 2.4, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.4, -2.04)
    glVertex3f(2.73, 2.4, -2.04)
    glVertex3f(2.73, 2.4, -1.92)
    glVertex3f(5.27, 2.4, -1.92)
    #FIN SECCION

    #SECCION PARED  EXTERIOR SIN VENTANA HABITACION AMARILLA
    # Lado exterior
    ab = np.array((0.67, 2.4, -2.04)) - np.array((-2.31, 2.4, -2.04))
    ac = np.array((-2.31, 0.0, -2.04)) - np.array((-2.31, 2.4, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, -2.04)
    glVertex3f(-2.31, 2.4, -2.04)
    glVertex3f(0.67, 2.4, -2.04)
    glVertex3f(0.67, 2.4, -2.04)

    # Lado interior
    ab = np.array((0.67, 2.4, -1.92)) - np.array((-2.19, 2.4, -1.92))
    ac = np.array((-2.19, 0.0, -1.92)) - np.array((-2.19, 2.4, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 0.0, -1.92)
    glVertex3f(-2.19, 2.4, -1.92)
    glVertex3f(0.67, 2.4, -1.92)
    glVertex3f(0.67, 0.0, -1.92)

    # Union por encima
    ab = np.array((0.67, 2.4, -1.92)) - np.array((-2.19, 2.4, -1.92))
    ac = np.array((-2.31, 2.4, -2.04)) - np.array((-2.19, 2.4, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 2.4, -2.04)
    glVertex3f(-2.19, 2.4, -1.92)
    glVertex3f(0.67, 2.4, -1.92)
    glVertex3f(0.67, 2.4, -2.04)

    #Pared entrada princial-habitación amarilla
    # Lado de la entrada
    ab = np.array((-0.79, 2.4, 1.71)) - np.array((-2.19, 2.4, 1.71))
    ac = np.array((-2.19, 0.0, 1.71)) - np.array((-2.19, 2.4, 1.71))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 0.0, 1.71)
    glVertex3f(-2.19, 2.4, 1.71)
    glVertex3f(-0.79, 2.4, 1.71)
    glVertex3f(-0.79, 0.0, 1.71)

    # Lado de la habitación
    ab = np.array((-0.67, 2.4, 1.59)) - np.array((-2.19, 2.4, 1.59))
    ac = np.array((-2.19, 0.0, 1.59)) - np.array((-2.19, 2.4, 1.59))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 0.0, 1.59)
    glVertex3f(-2.19, 2.4, 1.59)
    glVertex3f(-0.67, 2.4, 1.59)
    glVertex3f(-0.67, 0.0, 1.59)

    # Union superior
    ab = np.array((-0.67, 2.4, 1.59)) - np.array((-2.19, 2.4, 1.59))
    ac = np.array((-2.19, 2.4, 1.71)) - np.array((-2.19, 2.4, 1.59))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 2.4, 1.71)
    glVertex3f(-2.19, 2.4, 1.59)
    glVertex3f(-0.67, 2.4, 1.59)
    glVertex3f(-0.79, 2.4, 1.71)

    #SECCION PARED SALA-HABIRACION MORADA
    # Lado de la sala
    ab = np.array((2.61, 2.4, 1.71)) - np.array((5.39, 2.4, 1.71))
    ac = np.array((5.39, 0.0, 1.71)) - np.array((5.39, 2.4, 1.71))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, 1.71)
    glVertex3f(5.39, 2.4, 1.71)
    glVertex3f(2.61, 2.4, 1.71)
    glVertex3f(2.61, 0.0, 1.71)

    # Lado de la habiración
    ab = np.array((2.73, 2.4, 1.59)) - np.array((5.39, 2.4, 1.59))
    ac = np.array((5.39, 0.0, 1.59)) - np.array((5.39, 2.4, 1.59))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, 1.59)
    glVertex3f(5.39, 2.4, 1.59)
    glVertex3f(2.73, 2.4, 1.59)
    glVertex3f(2.73, 0.0, 1.59)

    # Union por encima
    ab = np.array((2.73, 2.4, 1.59)) - np.array((5.39, 2.4, 1.59))
    ac = np.array((5.39, 2.4, 1.71)) - np.array((5.39, 2.4, 1.59))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.4, 1.71)
    glVertex3f(5.39, 2.4, 1.59)
    glVertex3f(2.73, 2.4, 1.59)
    glVertex3f(2.61, 2.4, 1.71)

    #Trozo que tapa la parte exterior
    ab = np.array((5.39, 2.4, 1.59)) - np.array((5.39, 2.4, 1.71))
    ac = np.array((5.39, 0.0, 1.71)) - np.array((5.39, 2.4, 1.71))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, 1.71)
    glVertex3f(5.39, 2.4, 1.71)
    glVertex3f(5.39, 2.4, 1.59)
    glVertex3f(5.39, 0.0, 1.59)

    #SECCION PARED EXTERIOR SALA CON VENTANAS
    # Parte exterior
    ab = np.array((4.34, 2.4, 5.66)) - np.array((5.39, 2.4, 5.66))
    ac = np.array((5.39, 0.0, 5.66)) - np.array((5.39, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, 5.66)
    glVertex3f(5.39, 2.4, 5.66)
    glVertex3f(4.34, 2.4, 5.66)
    glVertex3f(4.34, 0.0, 5.66)

    # Parte interior
    ab = np.array((4.34, 2.4, 5.54)) - np.array((5.27, 2.4, 5.54))
    ac = np.array((5.27, 0.0, 5.54)) - np.array((5.27, 2.4, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 0.0, 5.54)
    glVertex3f(5.27, 2.4, 5.54)
    glVertex3f(4.34, 2.4, 5.54)
    glVertex3f(4.34, 0.0, 5.54)

    # Parte de arriba
    ab = np.array((4.34, 2.4, 5.54)) - np.array((5.27, 2.4, 5.54))
    ac = np.array((5.39, 2.4, 5.66)) - np.array((5.27, 2.4, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.4, 5.66)
    glVertex3f(5.27, 2.4, 5.54)
    glVertex3f(4.34, 2.4, 5.54)
    glVertex3f(4.34, 2.4, 5.66)

    # Parte que colinda con ventana
    ab = np.array((4.34, 2.4, 5.54)) - np.array((4.34, 2.4, 5.66))
    ac = np.array((4.34, 0.0, 5.66)) - np.array((4.34, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 0.0, 5.66)
    glVertex3f(4.34, 2.4, 5.66)
    glVertex3f(4.34, 2.4, 5.54)
    glVertex3f(4.34, 0.0, 5.54)

    #SECCION ARRIBA DE LA PRIMERA VENTANA
    # Parte exterior
    ab = np.array((3.34, 2.4, 5.66)) - np.array((4.34, 2.4, 5.66))
    ac = np.array((4.34, 2.0, 5.66)) - np.array((4.34, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 2.0, 5.66)
    glVertex3f(4.34, 2.4, 5.66)
    glVertex3f(3.34, 2.4, 5.66)
    glVertex3f(3.34, 2.0, 5.66)

    # Parte interior
    ab = np.array((3.34, 2.4, 5.66)) - np.array((4.34, 2.4, 5.66))
    ac = np.array((4.34, 2.0, 5.66)) - np.array((4.34, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 2.0, 5.54)
    glVertex3f(4.34, 2.4, 5.54)
    glVertex3f(3.34, 2.4, 5.54)
    glVertex3f(3.34, 2.0, 5.54)

    # Parte de arriba
    ab = np.array((3.34, 2.4, 5.54)) - np.array((3.34, 2.4, 5.66))
    ac = np.array((4.34, 2.4, 5.66)) - np.array((3.34, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 2.4, 5.66)
    glVertex3f(3.34, 2.4, 5.66)
    glVertex3f(3.34, 2.4, 5.54)
    glVertex3f(4.34, 2.4, 5.54)

    # Parte que colinda con la ventana
    ab = np.array((3.34, 2.0, 5.54)) - np.array((3.34, 2.0, 5.66))
    ac = np.array((4.34, 2.0, 5.66)) - np.array((3.34, 2.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 2.0, 5.66)
    glVertex3f(3.34, 2.0, 5.66)
    glVertex3f(3.34, 2.0, 5.54)
    glVertex3f(4.34, 2.0, 5.54)

    # SECCION ABAJO DE LA PRIMERA VENTANA
    # Parte exterior
    ab = np.array((3.34, 1.0, 5.66)) - np.array((4.34, 1.0, 5.66))
    ac = np.array((4.34, 0.0, 5.66)) - np.array((4.34, 1.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 0.0, 5.66)
    glVertex3f(4.34, 1.0, 5.66)
    glVertex3f(3.34, 1.0, 5.66)
    glVertex3f(3.34, 0.0, 5.66)

    # Parte interior
    ab = np.array((3.34, 1.0, 5.54)) - np.array((4.34, 1.0, 5.54))
    ac = np.array((4.34, 0.0, 5.54)) - np.array((4.34, 1.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 0.0, 5.54)
    glVertex3f(4.34, 1.0, 5.54)
    glVertex3f(3.34, 1.0, 5.54)
    glVertex3f(3.34, 0.0, 5.54)

    # Parte que colinda con la ventana
    ab = np.array((3.34, 1.0, 5.54)) - np.array((3.34, 1.0, 5.66))
    ac = np.array((4.34, 1.0, 5.66)) - np.array((3.34, 1.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(4.34, 1.0, 5.66)
    glVertex3f(3.34, 1.0, 5.66)
    glVertex3f(3.34, 1.0, 5.54)
    glVertex3f(4.34, 1.0, 5.54)


    # VENTANA
    # Parte exterior
    ab = np.array((4.34, 2.0, 5.66)) - np.array((4.34, 1.0, 5.66))
    ac = np.array((3.34, 1.0, 5.66)) - np.array((4.34, 1.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(4.34, 1.0, 5.66)
    glVertex3f(4.34, 2.0, 5.66)
    glVertex3f(3.34, 2.0, 5.66)
    glVertex3f(3.34, 1.0, 5.66)

    # Parte interior
    ab = np.array((4.34, 2.0, 5.54)) - np.array((4.34, 1.0, 5.54))
    ac = np.array((3.34, 1.0, 5.54)) - np.array((4.34, 1.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(4.34, 1.0, 5.54)
    glVertex3f(4.34, 2.0, 5.54)
    glVertex3f(3.34, 2.0, 5.54)
    glVertex3f(3.34, 1.0, 5.54)

    #SECCION PARED
    # Parte exterior
    ab = np.array((3.34, 2.4, 5.66)) - np.array((3.34, 0.0, 5.66))
    ac = np.array((2.54, 0.0, 5.66)) - np.array((3.34, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(3.34, 0.0, 5.66)
    glVertex3f(3.34, 2.4, 5.66)
    glVertex3f(2.54, 2.4, 5.66)
    glVertex3f(2.54, 0.0, 5.66)

    # Parte interior
    ab = np.array((3.34, 2.4, 5.54)) - np.array((3.34, 0.0, 5.54))
    ac = np.array((2.54, 0.0, 5.54)) - np.array((3.34, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(3.34, 0.0, 5.54)
    glVertex3f(3.34, 2.4, 5.54)
    glVertex3f(2.54, 2.4, 5.54)
    glVertex3f(2.54, 0.0, 5.54)

    # Parte de arriba
    ab = np.array((3.34, 2.4, 5.54)) - np.array((3.34, 2.4, 5.66))
    ac = np.array((2.54, 2.4, 5.66)) - np.array((3.34, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(3.34, 2.4, 5.66)
    glVertex3f(3.34, 2.4, 5.54)
    glVertex3f(2.54, 2.4, 5.54)
    glVertex3f(2.54, 2.4, 5.66)

    # Parte que colinda con ventana 1
    ab = np.array((3.34, 2.4, 5.66)) - np.array((3.34, 0.0, 5.66))
    ac = np.array((3.34, 0.0, 5.54)) - np.array((3.34, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(3.34, 0.0, 5.66)
    glVertex3f(3.34, 2.4, 5.66)
    glVertex3f(3.34, 2.4, 5.54)
    glVertex3f(3.34, 0.0, 5.54)

    # Parte que colinda con ventana 2
    ab = np.array((2.54, 2.4, 5.66)) - np.array((2.54, 0.0, 5.66))
    ac = np.array((2.54, 0.0, 5.54)) - np.array((2.54, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 0.0, 5.66)
    glVertex3f(2.54, 2.4, 5.66)
    glVertex3f(2.54, 2.4, 5.54)
    glVertex3f(2.54, 0.0, 5.54)

    # SECCION ARRIBA DE LA SEGUNDA VENTANA
    # Parte exterior
    ab = np.array((2.54, 2.4, 5.66)) - np.array((2.54, 2.0, 5.66))
    ac = np.array((0.54, 2.0, 5.66)) - np.array((2.54, 2.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 2.0, 5.66)
    glVertex3f(2.54, 2.4, 5.66)
    glVertex3f(0.54, 2.4, 5.66)
    glVertex3f(0.54, 2.0, 5.66)

    # Parte interior
    ab = np.array((2.54, 2.4, 5.54)) - np.array((2.54, 2.0, 5.54))
    ac = np.array((0.54, 2.0, 5.54)) - np.array((2.54, 2.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 2.0, 5.54)
    glVertex3f(2.54, 2.4, 5.54)
    glVertex3f(0.54, 2.4, 5.54)
    glVertex3f(0.54, 2.0, 5.54)

    # Parte de arriba
    ab = np.array((0.54, 2.4, 5.66)) - np.array((2.54, 2.4, 5.66))
    ac = np.array((2.54, 2.4, 5.54)) - np.array((2.54, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 2.4, 5.66)
    glVertex3f(0.54, 2.4, 5.66)
    glVertex3f(0.54, 2.4, 5.54)
    glVertex3f(2.54, 2.4, 5.54)

    # Parte que colinda con la ventana
    ab = np.array((0.54, 2.0, 5.66)) - np.array((2.54, 2.0, 5.66))
    ac = np.array((2.54, 2.0, 5.54)) - np.array((2.54, 2.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 2.0, 5.66)
    glVertex3f(0.54, 2.0, 5.66)
    glVertex3f(0.54, 2.0, 5.54)
    glVertex3f(2.54, 2.0, 5.54)

    # SECCION ABAJO DE LA SEGUNDA VENTANA
    # Parte exterior
    ab = np.array((2.54, 1.0, 5.66)) - np.array((2.54, 0.0, 5.66))
    ac = np.array((0.54, 0.0, 5.66)) - np.array((2.54, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 0.0, 5.66)
    glVertex3f(2.54, 1.0, 5.66)
    glVertex3f(0.54, 1.0, 5.66)
    glVertex3f(0.54, 0.0, 5.66)

    # Parte interior
    ab = np.array((2.54, 1.0, 5.54)) - np.array((2.54, 0.0, 5.54))
    ac = np.array((0.54, 0.0, 5.54)) - np.array((2.54, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 0.0, 5.54)
    glVertex3f(2.54, 1.0, 5.54)
    glVertex3f(0.54, 1.0, 5.54)
    glVertex3f(0.54, 0.0, 5.54)

    # Parte de arriba que colinda
    ab = np.array((0.54, 1.0, 5.66)) - np.array((2.54, 1.0, 5.66))
    ac = np.array((2.54, 1.0, 5.54)) - np.array((2.54, 1.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.54, 1.0, 5.66)
    glVertex3f(0.54, 1.0, 5.66)
    glVertex3f(0.54, 1.0, 5.54)
    glVertex3f(2.54, 1.0, 5.54)

    # VENTANA
    # Parte exterior
    ab = np.array((2.54, 2.0, 5.66)) - np.array((2.54, 1.0, 5.66))
    ac = np.array((0.54, 1.0, 5.66)) - np.array((2.54, 1.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(2.54, 1.0, 5.66)
    glVertex3f(2.54, 2.0, 5.66)
    glVertex3f(0.54, 2.0, 5.66)
    glVertex3f(0.54, 1.0, 5.66)

    # Parte interior
    ab = np.array((2.54, 2.0, 5.54)) - np.array((2.54, 1.0, 5.54))
    ac = np.array((0.54, 1.0, 5.54)) - np.array((2.54, 1.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(2.54, 1.0, 5.54)
    glVertex3f(2.54, 2.0, 5.54)
    glVertex3f(0.54, 2.0, 5.54)
    glVertex3f(0.54, 1.0, 5.54)

    # SECCION PARED
    # Parte exterior
    ab = np.array((0.54, 2.4, 5.66)) - np.array((0.54, 0.0, 5.66))
    ac = np.array((-0.31, 0.0, 5.66)) - np.array((0.54, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.54, 0.0, 5.66)
    glVertex3f(0.54, 2.4, 5.66)
    glVertex3f(-0.31, 2.4, 5.66)
    glVertex3f(-0.31, 0.0, 5.66)

    # Parte interior
    ab = np.array((0.54, 2.4, 5.54)) - np.array((0.54, 0.0, 5.54))
    ac = np.array((-0.19, 0.0, 5.54)) - np.array((0.54, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.54, 0.0, 5.54)
    glVertex3f(0.54, 2.4, 5.54)
    glVertex3f(-0.19, 2.4, 5.54)
    glVertex3f(-0.19, 0.0, 5.54)

    # Parte de arriba
    ab = np.array((0.54, 2.4, 5.54)) - np.array((0.54, 2.4, 5.66))
    ac = np.array((-0.31, 2.4, 5.66)) - np.array((0.54, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.54, 2.4, 5.66)
    glVertex3f(0.54, 2.4, 5.54)
    glVertex3f(-0.19, 2.4, 5.54)
    glVertex3f(-0.31, 2.4, 5.66)

    # Parte que colinda con ventana 1
    ab = np.array((0.54, 2.4, 5.66)) - np.array((0.54, 0.0, 5.66))
    ac = np.array((0.54, 0.0, 5.54)) - np.array((0.54, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.54, 0.0, 5.66)
    glVertex3f(0.54, 2.4, 5.66)
    glVertex3f(0.54, 2.4, 5.54)
    glVertex3f(0.54, 0.0, 5.54)

    # SECCION PARED COCINA
    # Parte exterior
    ab = np.array((-0.31, 2.4, 5.66)) - np.array((-0.31, 0.0, 5.66))
    ac = np.array((-0.81, 0.0, 5.66)) - np.array((-0.31, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.31, 0.0, 5.66)
    glVertex3f(-0.31, 2.4, 5.66)
    glVertex3f(-0.81, 2.4, 5.66)
    glVertex3f(-0.81, 0.0, 5.66)

    # Parte interior
    ab = np.array((-0.19, 2.4, 5.54)) - np.array((-0.19, 0.0, 5.54))
    ac = np.array((-0.81, 0.0, 5.54)) - np.array((-0.19, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 0.0, 5.54)
    glVertex3f(-0.19, 2.4, 5.54)
    glVertex3f(-0.81, 2.4, 5.54)
    glVertex3f(-0.81, 0.0, 5.54)

    # Parte de arriba
    ab = np.array((-0.19, 2.4, 5.54)) - np.array((-0.31, 2.4, 5.66))
    ac = np.array((-0.81, 2.4, 5.66)) - np.array((-0.31, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.31, 2.4, 5.66)
    glVertex3f(-0.19, 2.4, 5.54)
    glVertex3f(-0.81, 2.4, 5.54)
    glVertex3f(-0.81, 2.4, 5.66)

    # Parte que colinda con ventana
    ab = np.array((-0.81, 2.4, 5.66)) - np.array((-0.81, 0.0, 5.66))
    ac = np.array((-0.81, 0.0, 5.54)) - np.array((-0.81, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 0.0, 5.66)
    glVertex3f(-0.81, 2.4, 5.66)
    glVertex3f(-0.81, 2.4, 5.54)
    glVertex3f(-0.81, 0.0, 5.54)

    # SECCION ARRIBA DE LA VENTANA DE LA COCINA
    # Parte exterior
    ab = np.array((-0.81, 2.4, 5.66)) - np.array((-0.81, 1.7, 5.66))
    ac = np.array((-1.81, 1.7, 5.66)) - np.array((-0.81, 1.7, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 1.7, 5.66)
    glVertex3f(-0.81, 2.4, 5.66)
    glVertex3f(-1.81, 2.4, 5.66)
    glVertex3f(-1.81, 1.7, 5.66)

    # Parte interior
    ab = np.array((-0.81, 2.4, 5.54)) - np.array((-0.81, 1.7, 5.54))
    ac = np.array((-1.81, 1.7, 5.54)) - np.array((-0.81, 1.7, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 1.7, 5.54)
    glVertex3f(-0.81, 2.4, 5.54)
    glVertex3f(-1.81, 2.4, 5.54)
    glVertex3f(-1.81, 1.7, 5.54)

    # Parte de arriba
    ab = np.array((-1.81, 2.4, 5.66)) - np.array((-0.81, 2.4, 5.66))
    ac = np.array((-0.81, 2.4, 5.54)) - np.array((-0.81, 2.4, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 2.4, 5.66)
    glVertex3f(-1.81, 2.4, 5.66)
    glVertex3f(-1.81, 2.4, 5.54)
    glVertex3f(-0.81, 2.4, 5.54)

    # Parte que colinda con la ventana
    ab = np.array((-1.81, 1.7, 5.66)) - np.array((-0.81, 1.7, 5.66))
    ac = np.array((-0.81, 1.7, 5.54)) - np.array((-0.81, 1.7, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 1.7, 5.66)
    glVertex3f(-1.81, 1.7, 5.66)
    glVertex3f(-1.81, 1.7, 5.54)
    glVertex3f(-0.81, 1.7, 5.54)

    # SECCION ABAJO DE LA VENTANA DE LA COCINA
    # Parte exterior
    ab = np.array((-0.81, 1.0, 5.66)) - np.array((-0.81, 0.0, 5.66))
    ac = np.array((-1.81, 0.0, 5.66)) - np.array((-0.81, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 0.0, 5.66)
    glVertex3f(-0.81, 1.0, 5.66)
    glVertex3f(-1.81, 1.0, 5.66)
    glVertex3f(-1.81, 0.0, 5.66)

    # Parte interior
    ab = np.array((-0.81, 1.0, 5.54)) - np.array((-0.81, 0.0, 5.54))
    ac = np.array((-1.81, 0.0, 5.54)) - np.array((-0.81, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 0.0, 5.54)
    glVertex3f(-0.81, 1.0, 5.54)
    glVertex3f(-1.81, 1.0, 5.54)
    glVertex3f(-1.81, 0.0, 5.54)

    # Parte de arriba que colinda
    ab = np.array((-1.81, 1.0, 5.66)) - np.array((-0.81, 1.0, 5.66))
    ac = np.array((-0.81, 1.0, 5.54)) - np.array((-0.81, 1.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.81, 1.0, 5.66)
    glVertex3f(-1.81, 1.0, 5.66)
    glVertex3f(-1.81, 1.0, 5.54)
    glVertex3f(-0.81, 1.0, 5.54)

    #VENTANA COCINA
    ab = np.array((-0.81, 1.7, 5.66)) - np.array((-0.81, 1.0, 5.66))
    ac = np.array((-1.81, 1.0, 5.66)) - np.array((-0.81, 1.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.81, 1.0, 5.66)
    glVertex3f(-0.81, 1.7, 5.66)
    glVertex3f(-1.81, 1.7, 5.66)
    glVertex3f(-1.81, 1.0, 5.66)

    # Parte interior
    ab = np.array((-0.81, 1.7, 5.54)) - np.array((-0.81, 1.0, 5.54))
    ac = np.array((-1.81, 1.0, 5.54)) - np.array((-0.81, 1.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.81, 1.0, 5.54)
    glVertex3f(-0.81, 1.7, 5.54)
    glVertex3f(-1.81, 1.7, 5.54)
    glVertex3f(-1.81, 1.0, 5.54)


    # Parte que colinda con ventana 1
    ab = np.array((-1.81, 2.4, 5.66)) - np.array((-1.81, 0.0, 5.66))
    ac = np.array((-1.81, 0.0, 5.54)) - np.array((-1.81, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.81, 0.0, 5.66)
    glVertex3f(-1.81, 2.4, 5.66)
    glVertex3f(-1.81, 2.4, 5.54)
    glVertex3f(-1.81, 0.0, 5.54)

    # SECCION PARED COCINA DEL LADO DE LA PUERTA POR FUERA (OSEA LA QUE DA A LA CALLE XD)
    # Parte exterior
    ab = np.array((-2.31, 2.4, 5.66)) - np.array((-2.31, 0.0, 5.66))
    ac = np.array((-2.31, 0.0, 3.03)) - np.array((-2.31, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, 5.66)
    glVertex3f(-2.31, 2.4, 5.66)
    glVertex3f(-2.31, 2.4, 3.03)
    glVertex3f(-2.31, 0.0, 3.03)

    # Parte interior
    ab = np.array((-2.19, 2.4, 5.54)) - np.array((-2.19, 0.0, 5.54))
    ac = np.array((-2.19, 0.0, 3.15)) - np.array((-2.19, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 0.0, 5.54)
    glVertex3f(-2.19, 2.4, 5.54)
    glVertex3f(-2.19, 2.4, 3.15)
    glVertex3f(-2.19, 0.0, 3.15)

    # Parte de arriba
    ab = np.array((-2.31, 2.4, 5.66)) - np.array((-2.19, 2.4, 5.54))
    ac = np.array((-2.19, 2.4, 3.15)) - np.array((-2.19, 2.4, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 2.4, 5.54)
    glVertex3f(-2.31, 2.4, 5.66)
    glVertex3f(-2.31, 2.4, 3.03)
    glVertex3f(-2.19, 2.4, 3.15)

    # SECCION PARED COCINA DEL LADO DEL PASILLO
    # Parte exterior (lado del pasillo)
    ab = np.array((-2.31, 2.4, 3.03)) - np.array((-2.31, 0.0, 3.03))
    ac = np.array((-0.19, 0.0, 3.03)) - np.array((-2.31, 0.0, 3.03))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, 3.03)
    glVertex3f(-2.31, 2.4, 3.03)
    glVertex3f(-0.19, 2.4, 3.03)
    glVertex3f(-0.19, 0.0, 3.03)

    # Parte interior (lado de la cocina)
    ab = np.array((-0.31, 2.4, 3.15)) - np.array((-0.31, 0.0, 3.15))
    ac = np.array((-2.19, 0.0, 3.15)) - np.array((-0.31, 0.0, 3.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.31, 0.0, 3.15)
    glVertex3f(-0.31, 2.4, 3.15)
    glVertex3f(-2.19, 2.4, 3.15)
    glVertex3f(-2.19, 0.0, 3.15)

    # Parte de arriba
    ab = np.array((-2.31, 2.4, 3.03)) - np.array((-2.19, 2.4, 3.15))
    ac = np.array((-0.31, 2.4, 3.15)) - np.array((-2.19, 2.4, 3.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 2.4, 3.15)
    glVertex3f(-2.31, 2.4, 3.03)
    glVertex3f(-0.19, 2.4, 3.03)
    glVertex3f(-0.31, 2.4, 3.15)

    # SECCION PARED GRUESA LADO DE LA PUERTA DE LA COCINA
    # Parte exterior (lado del pasillo)
    ab = np.array((-0.19, 2.4, 5.54)) - np.array((-0.19, 0.0, 5.54))
    ac = np.array((-0.19, 0.0, 4.27)) - np.array((-0.19, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 0.0, 5.54)
    glVertex3f(-0.19, 2.4, 5.54)
    glVertex3f(-0.19, 2.4, 4.27)
    glVertex3f(-0.19, 0.0, 4.27)

    # Parte interior (lado de la cocina)
    ab = np.array((-0.31, 2.4, 5.54)) - np.array((-0.31, 0.0, 5.54))
    ac = np.array((-0.31, 0.0, 4.27)) - np.array((-0.31, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.31, 0.0, 5.54)
    glVertex3f(-0.31, 2.4, 5.54)
    glVertex3f(-0.31, 2.4, 4.27)
    glVertex3f(-0.31, 0.0, 4.27)

    # Parte de arriba
    ab = np.array((-0.31, 2.4, 5.54)) - np.array((-0.19, 2.4, 5.54))
    ac = np.array((-0.19, 2.4, 4.27)) - np.array((-0.19, 2.4, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 2.4, 5.54)
    glVertex3f(-0.31, 2.4, 5.54)
    glVertex3f(-0.31, 2.4, 4.27)
    glVertex3f(-0.19, 2.4, 4.27)

    # Parte de lado de la puerta
    ab = np.array((-0.19, 2.4, 4.27)) - np.array((-0.19, 0.0, 4.27))
    ac = np.array((-0.31, 0.0, 4.27)) - np.array((-0.19, 0.0, 4.27))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 0.0, 4.27)
    glVertex3f(-0.19, 2.4, 4.27)
    glVertex3f(-0.31, 2.4, 4.27)
    glVertex3f(-0.31, 0.0, 4.27)

    # SECCION PARED GRUESA DELGADA DE LA PUERTA DE LA COCINA
    # Parte exterior (lado del pasillo)
    ab = np.array((-0.19, 2.4, 3.03)) - np.array((-0.19, 0.0, 3.03))
    ac = np.array((-0.19, 0.0, 3.27)) - np.array((-0.19, 0.0, 3.03))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 0.0, 3.03)
    glVertex3f(-0.19, 2.4, 3.03)
    glVertex3f(-0.19, 2.4, 3.27)
    glVertex3f(-0.19, 0.0, 3.27)

    # Parte interior (lado de la cocina)#Creo que está al reves con la de arriba
    ab = np.array((-0.31, 2.4, 3.15)) - np.array((-0.31, 0.0, 3.15))
    ac = np.array((-0.31, 0.0, 3.27)) - np.array((-0.31, 0.0, 3.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.31, 0.0, 3.15)
    glVertex3f(-0.31, 2.4, 3.15)
    glVertex3f(-0.31, 2.4, 3.27)
    glVertex3f(-0.31, 0.0, 3.27)

    # Parte de arriba
    ab = np.array((-0.31, 2.4, 3.15)) - np.array((-0.19, 2.4, 3.03))
    ac = np.array((-0.19, 2.4, 3.27)) - np.array((-0.19, 2.4, 3.03))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 2.4, 3.03)
    glVertex3f(-0.31, 2.4, 3.15)
    glVertex3f(-0.31, 2.4, 3.27)
    glVertex3f(-0.19, 2.4, 3.27)

    # Parte de lado de la puerta
    ab = np.array((-0.19, 2.4, 3.27)) - np.array((-0.19, 0.0, 3.27))
    ac = np.array((-0.31, 0.0, 3.27)) - np.array((-0.19, 0.0, 3.27))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 0.0, 3.27)
    glVertex3f(-0.19, 2.4, 3.27)
    glVertex3f(-0.31, 2.4, 3.27)
    glVertex3f(-0.31, 0.0, 3.27)

    # SECCION PARED DE ARRIBA DE LA PUERTA
    # Parte exterior (lado del pasillo)
    ab = np.array((-0.19, 2.4, 4.27)) - np.array((-0.19, 2.0, 4.27))
    ac = np.array((-0.19, 2.0, 3.27)) - np.array((-0.19, 2.0, 4.27))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 2.0, 4.27)
    glVertex3f(-0.19, 2.4, 4.27)
    glVertex3f(-0.19, 2.4, 3.27)
    glVertex3f(-0.19, 2.0, 3.27)

    # Parte interior (lado de la cocina)
    ab = np.array((-0.31, 2.4, 4.27)) - np.array((-0.31, 2.0, 4.27))
    ac = np.array((-0.31, 2.0, 3.27)) - np.array((-0.31, 2.0, 4.27))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.31, 2.0, 4.27)
    glVertex3f(-0.31, 2.4, 4.27)
    glVertex3f(-0.31, 2.4, 3.27)
    glVertex3f(-0.31, 2.0, 3.27)

    # Parte de arriba
    ab = np.array((-0.31, 2.4, 4.27)) - np.array((-0.19, 2.4, 4.27))
    ac = np.array((-0.19, 2.4, 3.27)) - np.array((-0.19, 2.4, 4.27))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 2.4, 4.27)
    glVertex3f(-0.31, 2.4, 4.27)
    glVertex3f(-0.31, 2.4, 3.27)
    glVertex3f(-0.19, 2.4, 3.27)

    # Parte de abajo
    ab = np.array((-0.31, 2.0, 4.27)) - np.array((-0.19, 2.0, 4.27))
    ac = np.array((-0.19, 2.0, 3.27)) - np.array((-0.19, 2.0, 4.27))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.19, 2.0, 4.27)
    glVertex3f(-0.31, 2.0, 4.27)
    glVertex3f(-0.31, 2.0, 3.27)
    glVertex3f(-0.19, 2.0, 3.27)

    # SECCION PARED BAÑO-HABITACION MORADA
    # Parte exterior (lado de la habitacion)
    ab = np.array((2.73, 2.4, -2.04)) - np.array((2.73, 0.0, -2.04))
    ac = np.array((2.73, 0.0, 0.46)) - np.array((2.73, 0.0, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.73, 0.0, -2.04)
    glVertex3f(2.73, 2.4, -2.04)
    glVertex3f(2.73, 2.4, 0.46)
    glVertex3f(2.73, 0.0, 0.46)

    # Parte interior (lado del baño)
    ab = np.array((2.61, 2.4, -1.92)) - np.array((2.61, 0.0, -1.92))
    ac = np.array((2.61, 0.0, 0.34)) - np.array((2.61, 0.0, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.61, 0.0, -1.92)
    glVertex3f(2.61, 2.4, -1.92)
    glVertex3f(2.61, 2.4, 0.34)
    glVertex3f(2.61, 0.0, 0.34)

    # Parte de arriba
    ab = np.array((2.73, 2.4, 0.46)) - np.array((2.73, 2.4, -2.04))
    ac = np.array((2.61, 2.4, -1.92)) - np.array((2.73, 2.4, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.73, 2.4, -2.04)
    glVertex3f(2.73, 2.4, 0.46)
    glVertex3f(2.61, 2.4, 0.34)
    glVertex3f(2.61, 2.4, -1.92)

    # SECCION PARED BAÑO-HABITACION AMARILLA
    # Parte exterior (lado de la habitacion)
    ab = np.array((-0.67, 2.4, -2.04)) - np.array((-0.67, 0.0, -2.04))
    ac = np.array((-0.67, 0.0, 0.46)) - np.array((-0.67, 0.0, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.67, 0.0, -2.04)
    glVertex3f(-0.67, 2.4, -2.04)
    glVertex3f(-0.67, 2.4, 0.46)
    glVertex3f(-0.67, 0.0, 0.46)

    # Parte interior (lado del baño)
    ab = np.array((-0.79, 2.4, -1.92)) - np.array((-0.79, 0.0, -1.92))
    ac = np.array((-0.79, 0.0, 0.34)) - np.array((-0.79, 0.0, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.79, 0.0, -1.92)
    glVertex3f(-0.79, 2.4, -1.92)
    glVertex3f(-0.79, 2.4, 0.34)
    glVertex3f(-0.79, 0.0, 0.34)

    # Parte de arriba
    ab = np.array((-0.67, 2.4, 0.46)) - np.array((-0.67, 2.4, -2.04))
    ac = np.array((-0.79, 2.4, -1.92)) - np.array((-0.67, 2.4, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.67, 2.4, -2.04)
    glVertex3f(-0.67, 2.4, 0.46)
    glVertex3f(-0.79, 2.4, 0.34)
    glVertex3f(-0.79, 2.4, -1.92)

    # SECCION PARED EXTERIOR HABIRACIÓN DEL LADO DE LA SALA
    # Parte exterior
    ab = np.array((5.39, 2.4, -2.04)) - np.array((5.39, 0.0, -2.04))
    ac = np.array((5.39, 0.0, -1.23)) - np.array((5.39, 0.0, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, -2.04)
    glVertex3f(5.39, 2.4, -2.04)
    glVertex3f(5.39, 2.4, -1.23)
    glVertex3f(5.39, 0.0, -1.23)

    # Parte interior
    ab = np.array((5.27, 2.4, -1.92)) - np.array((5.27, 0.0, -1.92))
    ac = np.array((5.27, 0.0, -1.23)) - np.array((5.27, 0.0, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 0.0, -1.92)
    glVertex3f(5.27, 2.4, -1.92)
    glVertex3f(5.27, 2.4, -1.23)
    glVertex3f(5.27, 0.0, -1.23)

    # Parte de arriba
    ab = np.array((5.39, 2.4, -1.23)) - np.array((5.39, 2.4, -2.04))
    ac = np.array((5.27, 2.4, -1.92)) - np.array((5.39, 2.4, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.4, -2.04)
    glVertex3f(5.39, 2.4, -1.23)
    glVertex3f(5.27, 2.4, -1.23)
    glVertex3f(5.27, 2.4, -1.92)

    # Parte de la ventana
    ab = np.array((5.39, 2.4, -1.23)) - np.array((5.39, 0.0, -1.23))
    ac = np.array((5.27, 0.0, -1.23)) - np.array((5.39, 0.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, -1.23)
    glVertex3f(5.39, 2.4, -1.23)
    glVertex3f(5.27, 2.4, -1.23)
    glVertex3f(5.27, 0.0, -1.23)

    # Parte exterior arriba de la ventana
    ab = np.array((5.39, 2.4, -1.23)) - np.array((5.39, 2.0, -1.23))
    ac = np.array((5.39, 2.0, -0.77)) - np.array((5.39, 2.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.0, -1.23)
    glVertex3f(5.39, 2.4, -1.23)
    glVertex3f(5.39, 2.4, -0.77)
    glVertex3f(5.39, 2.0, -0.77)

    # Parte interior
    ab = np.array((5.27, 2.4, -1.23)) - np.array((5.27, 2.0, -1.23))
    ac = np.array((5.27, 2.0, -0.77)) - np.array((5.27, 2.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 2.0, -1.23)
    glVertex3f(5.27, 2.4, -1.23)
    glVertex3f(5.27, 2.4, -0.77)
    glVertex3f(5.27, 2.0, -0.77)

    # Parte de arriba
    ab = np.array((5.39, 2.4, -0.77)) - np.array((5.39, 2.4, -1.23))
    ac = np.array((5.27, 2.4, -1.23)) - np.array((5.39, 2.4, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.4, -1.23)
    glVertex3f(5.39, 2.4, -0.77)
    glVertex3f(5.27, 2.4, -0.77)
    glVertex3f(5.27, 2.4, -1.23)

    # Parte colinda con ventana
    ab = np.array((5.39, 2.0, -0.77)) - np.array((5.39, 2.0, -1.23))
    ac = np.array((5.27, 2.0, -1.23)) - np.array((5.39, 2.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.0, -1.23)
    glVertex3f(5.39, 2.0, -0.77)
    glVertex3f(5.27, 2.0, -0.77)
    glVertex3f(5.27, 2.0, -1.23)

    # Parte exterior abajo de la ventana
    ab = np.array((5.39, 1.0, -1.23)) - np.array((5.39, 0.0, -1.23))
    ac = np.array((5.39, 0.0, -0.77)) - np.array((5.39, 0.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, -1.23)
    glVertex3f(5.39, 1.0, -1.23)
    glVertex3f(5.39, 1.0, -0.77)
    glVertex3f(5.39, 0.0, -0.77)

    # Parte interior
    ab = np.array((5.27, 1.0, -1.23)) - np.array((5.27, 0.0, -1.23))
    ac = np.array((5.27, 0.0, -0.77)) - np.array((5.27, 0.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 0.0, -1.23)
    glVertex3f(5.27, 1.0, -1.23)
    glVertex3f(5.27, 1.0, -0.77)
    glVertex3f(5.27, 0.0, -0.77)

    # Parte de arriba
    ab = np.array((5.39, 1.0, -0.77)) - np.array((5.39, 1.0, -1.23))
    ac = np.array((5.27, 1.0, -1.23)) - np.array((5.39, 1.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 1.0, -1.23)
    glVertex3f(5.39, 1.0, -0.77)
    glVertex3f(5.27, 1.0, -0.77)
    glVertex3f(5.27, 1.0, -1.23)

    #VENTANA
    # Parte exterior
    ab = np.array((5.39, 2.0, -1.23)) - np.array((5.39, 1.0, -1.23))
    ac = np.array((5.39, 1.0, -0.77)) - np.array((5.39, 1.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(5.39, 1.0, -1.23)
    glVertex3f(5.39, 2.0, -1.23)
    glVertex3f(5.39, 2.0, -0.77)
    glVertex3f(5.39, 1.0, -0.77)

    # Parte interior
    ab = np.array((5.27, 2.0, -1.23)) - np.array((5.27, 1.0, -1.23))
    ac = np.array((5.27, 1.0, -0.77)) - np.array((5.27, 1.0, -1.23))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(5.27, 1.0, -1.23)
    glVertex3f(5.27, 2.0, -1.23)
    glVertex3f(5.27, 2.0, -0.77)
    glVertex3f(5.27, 1.0, -0.77)

    #PARTE CORTA DE LA PARED
    # Parte exterior
    ab = np.array((5.39, 2.4, -0.77)) - np.array((5.39, 0.0, -0.77))
    ac = np.array((5.39, 0.0, 1.75)) - np.array((5.39, 0.0, -0.77))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, -0.77)
    glVertex3f(5.39, 2.4, -0.77)
    glVertex3f(5.39, 2.4, 1.75)
    glVertex3f(5.39, 0.0, 1.75)

    # Parte interior
    ab = np.array((5.27, 2.4, -0.77)) - np.array((5.27, 0.0, -0.77))
    ac = np.array((5.27, 0.0, 1.59)) - np.array((5.27, 0.0, -0.77))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 0.0, -0.77)
    glVertex3f(5.27, 2.4, -0.77)
    glVertex3f(5.27, 2.4, 1.59)
    glVertex3f(5.27, 0.0, 1.59)

    # Parte de arriba
    ab = np.array((5.39, 2.4, 1.75)) - np.array((5.39, 2.4, -0.77))
    ac = np.array((5.27, 2.4, 0.77)) - np.array((5.39, 2.4, -0.77))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 2.4, -0.77)
    glVertex3f(5.39, 2.4, 1.75)
    glVertex3f(5.27, 2.4, 1.59)
    glVertex3f(5.27, 2.4, 0.77)

    # Parte de la ventana
    ab = np.array((5.39, 2.4, -0.77)) - np.array((5.39, 0.0, -0.77))
    ac = np.array((5.27, 0.0, -0.77)) - np.array((5.39, 0.0, -0.77))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.39, 0.0, -0.77)
    glVertex3f(5.39, 2.4, -0.77)
    glVertex3f(5.27, 2.4, -0.77)
    glVertex3f(5.27, 0.0, -0.77)

    # SECCION PARED EXTERIOR HABIRACIÓN DEL LADO DE LA COCINA
    # Parte exterior
    ab = np.array((-2.31, 2.4, -2.04)) - np.array((-2.31, 0.0, -2.04))
    ac = np.array((-2.31, 0.0, -0.93)) - np.array((-2.31, 0.0, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, -2.04)
    glVertex3f(-2.31, 2.4, -2.04)
    glVertex3f(-2.31, 2.4, -0.93)
    glVertex3f(-2.31, 0.0, -0.93)

    # Parte interior
    ab = np.array((-2.19, 2.4, -1.92)) - np.array((-2.19, 0.0, -1.92))
    ac = np.array((-2.19, 0.0, -0.93)) - np.array((-2.19, 0.0, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 0.0, -1.92)
    glVertex3f(-2.19, 2.4, -1.92)
    glVertex3f(-2.19, 2.4, -0.93)
    glVertex3f(-2.19, 0.0, -0.93)

    # Parte de arriba
    ab = np.array((-2.31, 2.4, -0.93)) - np.array((-2.31, 2.4, -2.04))
    ac = np.array((-2.19, 2.4, -1.92)) - np.array((-2.31, 2.4, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 2.4, -2.04)
    glVertex3f(-2.31, 2.4, -0.93)
    glVertex3f(-2.19, 2.4, -0.93)
    glVertex3f(-2.19, 2.4, -1.92)

    # Parte de la ventana
    ab = np.array((-2.31, 2.4, -0.93)) - np.array((-2.31, 0.0, -0.93))
    ac = np.array((-2.19, 0.0, -0.93)) - np.array((-2.31, 0.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, -0.93)
    glVertex3f(-2.31, 2.4, -0.93)
    glVertex3f(-2.19, 2.4, -0.93)
    glVertex3f(-2.19, 0.0, -0.93)

    # Parte exterior arriba de la ventana
    ab = np.array((-2.31, 2.4, -0.93)) - np.array((-2.31, 2.0, -0.93))
    ac = np.array((-2.31, 2.0, -1.07)) - np.array((-2.31, 2.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 2.0, -0.93)
    glVertex3f(-2.31, 2.4, -0.93)
    glVertex3f(-2.31, 2.4, -1.07)
    glVertex3f(-2.31, 2.0, -1.07)

    # Parte interior
    ab = np.array((5.27, 2.4, -0.93)) - np.array((5.27, 2.0, -0.93))
    ac = np.array((5.27, 2.0, -1.07)) - np.array((5.27, 2.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 2.0, -0.93)
    glVertex3f(5.27, 2.4, -0.93)
    glVertex3f(5.27, 2.4, -1.07)
    glVertex3f(5.27, 2.0, -1.07)

    # Parte de arriba
    ab = np.array((-2.19, 2.4, -1.07)) - np.array((-2.19, 2.4, -0.93))
    ac = np.array((-2.31, 2.4, -0.93)) - np.array((-2.19, 2.4, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 2.4, -0.93)
    glVertex3f(-2.19, 2.4, -1.07)
    glVertex3f(-2.31, 2.4, -1.07)
    glVertex3f(-2.31, 2.4, -0.93)

    # Parte de arriba
    ab = np.array((-2.19, 2.0, -1.07)) - np.array((-2.19, 2.0, -0.93))
    ac = np.array((-2.31, 2.0, -0.93)) - np.array((-2.19, 2.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 2.0, -0.93)
    glVertex3f(-2.19, 2.0, -1.07)
    glVertex3f(-2.31, 2.0, -1.07)
    glVertex3f(-2.31, 2.0, -0.93)

    # Parte exterior bajo de la ventana
    ab = np.array((-2.31, 2.0, -0.93)) - np.array((-2.31, 0.0, -0.93))
    ac = np.array((-2.31, 0.0, -1.07)) - np.array((-2.31, 0.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, -0.93)
    glVertex3f(-2.31, 2.0, -0.93)
    glVertex3f(-2.31, 2.0, -1.07)
    glVertex3f(-2.31, 0.0, -1.07)

    # Parte interior
    ab = np.array((5.27, 2.0, -0.93)) - np.array((5.27, 0.0, -0.93))
    ac = np.array((5.27, 0.0, -1.07)) - np.array((5.27, 0.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.27, 0.0, -0.93)
    glVertex3f(5.27, 2.0, -0.93)
    glVertex3f(5.27, 2.0, -1.07)
    glVertex3f(5.27, 0.0, -1.07)

    # Parte de arriba
    ab = np.array((-2.19, 2.0, -1.07)) - np.array((-2.19, 2.0, -0.93))
    ac = np.array((-2.31, 2.0, -0.93)) - np.array((-2.19, 2.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 2.0, -0.93)
    glVertex3f(-2.19, 2.0, -1.07)
    glVertex3f(-2.31, 2.0, -1.07)
    glVertex3f(-2.31, 2.0, -0.93)

    # VENTANA
    # Parte exterior
    ab = np.array((-2.31, 2.0, -0.93)) - np.array((-2.31, 1.0, -0.93))
    ac = np.array((-2.31, 1.0, -1.07)) - np.array((-2.31, 1.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-2.31, 1.0, -0.93)
    glVertex3f(-2.31, 2.0, -0.93)
    glVertex3f(-2.31, 2.0, -1.07)
    glVertex3f(-2.31, 1.0, -1.07)

    # Parte interior
    ab = np.array((-2.19, 2.0, -0.93)) - np.array((-2.19, 1.0, -0.93))
    ac = np.array((-2.19, 1.0, -0.93)) - np.array((-2.19, 1.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-2.19, 1.0, -0.93)
    glVertex3f(-2.19, 2.0, -0.93)
    glVertex3f(-2.19, 2.0, -0.93)
    glVertex3f(-2.19, 1.0, -0.93)

    # PARTE CORTA DE LA PARED
    # Parte exterior
    ab = np.array((-2.31, 2.4, 1.07)) - np.array((-2.31, 0.0, 1.07))
    ac = np.array((-2.31, 0.0, 1.71)) - np.array((-2.31, 0.0, 1.07))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, 1.07)
    glVertex3f(-2.31, 2.4, 1.07)
    glVertex3f(-2.31, 2.4, 1.71)
    glVertex3f(-2.31, 0.0, 1.71)

    # Parte interior
    ab = np.array((-2.19, 2.4, -0.93)) - np.array((-2.19, 0.0, -0.93))
    ac = np.array((-2.19, 0.0, 1.07)) - np.array((-2.19, 0.0, -0.93))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.19, 0.0, -0.93)
    glVertex3f(-2.19, 2.4, -0.93)
    glVertex3f(-2.19, 2.4, 1.07)
    glVertex3f(-2.19, 0.0, 1.07)

    # Parte de arriba
    ab = np.array((-2.31, 2.4, 1.71)) - np.array((-2.31, 2.4, 1.07))
    ac = np.array((-2.19, 2.4, 1.07)) - np.array((-2.31, 2.4, 1.07))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 2.4, 1.07)
    glVertex3f(-2.31, 2.4, 1.71)
    glVertex3f(-2.19, 2.4, 1.59)
    glVertex3f(-2.19, 2.4, 1.07)

    # Parte de la ventana
    ab = np.array((-2.31, 2.4, 1.07)) - np.array((-2.31, 0.0, 1.07))
    ac = np.array((-2.19, 0.0, 1.07)) - np.array((-2.31, 0.0, 1.07))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2.31, 0.0, 1.07)
    glVertex3f(-2.31, 2.4, 1.07)
    glVertex3f(-2.19, 2.4, 1.07)
    glVertex3f(-2.19, 0.0, 1.07)

    ##SEGUNDA ACTUALIZACIÓN

    # SECCION DE LA PUERTA DEL BAÑO
    # Parte externa del baño
    ab = np.array((2.61, 2.4, 0.46)) - np.array((2.61, 0.0, 0.46))
    ac = np.array((1.79, 0.0, 0.46)) - np.array((2.61, 0.0, 0.46))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.61, 0.0, 0.46)
    glVertex3f(2.61, 2.4, 0.46)
    glVertex3f(1.79, 2.4, 0.46)
    glVertex3f(1.79, 0.0, 0.46)

    # Parte interna del baño
    ab = np.array((2.73, 2.4, 0.34)) - np.array((2.73, 0.0, 0.34))
    ac = np.array((1.79, 0.0, 0.34)) - np.array((2.73, 0.0, 0.34))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.73, 0.0, 0.34)
    glVertex3f(2.73, 2.4, 0.34)
    glVertex3f(1.79, 2.4, 0.34)
    glVertex3f(1.79, 0.0, 0.34)

    # Parte de arriba
    ab = np.array((2.61, 2.4, 0.46)) - np.array((2.73, 2.4, 0.34))
    ac = np.array((1.79, 2.4, 0.34)) - np.array((2.73, 2.4, 0.34))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.73, 2.4, 0.34)
    glVertex3f(2.61, 2.4, 0.46)
    glVertex3f(1.79, 2.4, 0.46)
    glVertex3f(1.79, 2.4, 0.34)

    # Parte colindante con la puerta
    ab = np.array((1.79, 2.4, 0.34)) - np.array((1.79, 0.0, 0.34))
    ac = np.array((1.79, 0.0, 0.46)) - np.array((1.79, 0.0, 0.34))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(1.79, 0.0, 0.34)
    glVertex3f(1.79, 2.4, 0.34)
    glVertex3f(1.79, 2.4, 0.46)
    glVertex3f(1.79, 0.0, 0.46)

    # Seccion parte arriba de la puerta del baño
    # Parte externa del baño
    ab = np.array((0.79, 2.4, 0.46)) - np.array((0.79, 2.0, 0.46))
    ac = np.array((1.79, 2.0, 0.46)) - np.array((0.79, 2.0, 0.46))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 2.0, 0.46)
    glVertex3f(0.79, 2.4, 0.46)
    glVertex3f(1.79, 2.4, 0.46)
    glVertex3f(1.79, 2.0, 0.46)

    # Parte interna del baño
    ab = np.array((0.79, 2.4, 0.34)) - np.array((0.79, 2.0, 0.34))
    ac = np.array((1.79, 2.0, 0.34)) - np.array((0.79, 2.0, 0.34))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 2.0, 0.34)
    glVertex3f(0.79, 2.4, 0.34)
    glVertex3f(1.79, 2.4, 0.34)
    glVertex3f(1.79, 2.0, 0.34)

    # Parte de arriba
    ab = np.array((0.79, 2.4, 0.46)) - np.array((0.79, 2.4, 0.34))
    ac = np.array((1.79, 2.4, 0.34)) - np.array((0.79, 2.4, 0.34))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 2.4, 0.34)
    glVertex3f(0.79, 2.4, 0.46)
    glVertex3f(1.79, 2.4, 0.46)
    glVertex3f(1.79, 2.4, 0.34)

    # Parte de abajo
    ab = np.array((0.79, 2.0, 0.46)) - np.array((0.79, 2.0, 0.34))
    ac = np.array((1.79, 2.0, 0.34)) - np.array((0.79, 2.0, 0.34))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 2.0, 0.34)
    glVertex3f(0.79, 2.0, 0.46)
    glVertex3f(1.79, 2.0, 0.46)
    glVertex3f(1.79, 2.0, 0.34)

    # SECCION DE LA BAÑERA
    # Parte externa de la bañera
    ab = np.array((2.61, 1.9, -1.10)) - np.array((2.61, 0.0, -1.10))
    ac = np.array((1.45, 0.0, -1.10)) - np.array((2.61, 0.0, -1.10))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.61, 0.0, -1.10)
    glVertex3f(2.61, 1.9, -1.10)
    glVertex3f(1.45, 1.9, -1.10)
    glVertex3f(1.45, 0.0, -1.10)

    # Parte interna del baño
    ab = np.array((2.61, 1.9, -1.15)) - np.array((2.61, 0.0, -1.15))
    ac = np.array((1.45, 0.0, -1.15)) - np.array((2.61, 0.0, -1.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.61, 0.0, -1.15)
    glVertex3f(2.61, 1.9, -1.15)
    glVertex3f(1.45, 1.9, -1.15)
    glVertex3f(1.45, 0.0, -1.15)

    # Parte de arriba
    ab = np.array((2.61, 1.9, -1.10)) - np.array((2.61, 1.9, -1.15))
    ac = np.array((1.45, 1.9, -1.15)) - np.array((2.61, 1.9, -1.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.61, 1.9, -1.15)
    glVertex3f(2.61, 1.9, -1.10)
    glVertex3f(1.45, 1.9, -1.10)
    glVertex3f(1.45, 1.9, -1.15)

    # Parte que colinda con la ventana
    ab = np.array((1.45, 1.9, -1.10)) - np.array((1.45, 0.0, -1.10))
    ac = np.array((1.45, 0.0, -1.15)) - np.array((1.45, 0.0, -1.10))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(1.45, 0.0, -1.10)
    glVertex3f(1.45, 1.9, -1.10)
    glVertex3f(1.45, 1.9, -1.15)
    glVertex3f(1.45, 0.0, -1.15)

    # SECCION DE LA VENTANA/PUERTA DE LA BAÑERA
    # Parte externa de la bañera
    ab = np.array((0.79, 1.9, -1.10)) - np.array((0.79, 0.41, -1.10))
    ac = np.array((1.45, 0.41, -1.10)) - np.array((0.79, 0.41, -1.10))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 0.41, -1.10)
    glVertex3f(0.79, 1.9, -1.10)
    glVertex3f(1.45, 1.9, -1.10)
    glVertex3f(1.45, 0.41, -1.10)

    # Parte interna del baño
    ab = np.array((0.79, 1.9, -1.15)) - np.array((0.79, 0.41, -1.15))
    ac = np.array((1.45, 0.41, -1.15)) - np.array((0.79, 0.41, -1.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 0.41, -1.15)
    glVertex3f(0.79, 1.9, -1.15)
    glVertex3f(1.45, 1.9, -1.15)
    glVertex3f(1.45, 0.41, -1.15)

    # Parte de arriba
    ab = np.array((0.79, 1.9, -1.10)) - np.array((0.79, 1.9, -1.15))
    ac = np.array((1.45, 1.9, -1.15)) - np.array((0.79, 1.9, -1.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 1.9, -1.15)
    glVertex3f(0.79, 1.9, -1.10)
    glVertex3f(1.45, 1.9, -1.10)
    glVertex3f(1.45, 1.9, -1.15)

    # seccion de la parte de abajo de la bañera
    # Parte externa de la bañera
    ab = np.array((0.79, 0.41, -1.10)) - np.array((0.79, 0.0, -1.10))
    ac = np.array((1.45, 0.0, -1.10)) - np.array((0.79, 0.0, -1.10))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 0.0, -1.10)
    glVertex3f(0.79, 0.41, -1.10)
    glVertex3f(1.45, 0.41, -1.10)
    glVertex3f(1.45, 0.0, -1.10)

    # Parte interna del baño
    ab = np.array((0.79, 0.41, -1.15)) - np.array((0.79, 0.0, -1.15))
    ac = np.array((1.45, 0.0, -1.15)) - np.array((0.79, 0.0, -1.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 0.0, -1.15)
    glVertex3f(0.79, 0.41, -1.15)
    glVertex3f(1.45, 0.41, -1.15)
    glVertex3f(1.45, 0.0, -1.15)

    # Parte de arriba
    ab = np.array((0.79, 0.41, -1.10)) - np.array((0.79, 0.41, -1.15))
    ac = np.array((1.45, 0.41, -1.15)) - np.array((0.79, 0.41, -1.15))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 0.41, -1.15)
    glVertex3f(0.79, 0.41, -1.10)
    glVertex3f(1.45, 0.41, -1.10)
    glVertex3f(1.45, 0.41, -1.15)

    # ESQUINA DE LA COCINA DEL LADO DE LA VENTANA
    # Parte externa
    ab = np.array((-1.81, 2.4, 5.66)) - np.array((-1.81, 0.0, 5.66))
    ac = np.array((-2.31, 0.0, 5.66)) - np.array((-1.81, 0.0, 5.66))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.81, 0.0, 5.66)
    glVertex3f(-1.81, 2.4, 5.66)
    glVertex3f(-2.31, 2.4, 5.66)
    glVertex3f(-2.31, 0.0, 5.66)

    # Parte interna
    ab = np.array((-1.81, 2.4, 5.54)) - np.array((-1.81, 0.0, 5.54))
    ac = np.array((-2.19, 0.0, 5.54)) - np.array((-1.81, 0.0, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.81, 0.0, 5.54)
    glVertex3f(-1.81, 2.4, 5.54)
    glVertex3f(-2.19, 2.4, 5.54)
    glVertex3f(-2.19, 0.0, 5.54)

    # Parte de arriba
    ab = np.array((-1.81, 2.4, 5.66)) - np.array((-1.81, 2.4, 5.54))
    ac = np.array((-2.19, 2.4, 5.54)) - np.array((-1.81, 2.4, 5.54))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.81, 2.4, 5.54)
    glVertex3f(-1.81, 2.4, 5.66)
    glVertex3f(-2.19, 2.4, 5.66)
    glVertex3f(-2.19, 2.4, 5.54)

    # PARED DE LA HABITACIÓN MORADA CON EL BAÑO
    # Parte de la habitacion
    ab = np.array((2.73, 2.4, -1.92)) - np.array((2.73, 0.0, -1.92))
    ac = np.array((2.73, 0.0, 0.46)) - np.array((2.73, 0.0, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.73, 0.0, -1.92)
    glVertex3f(2.73, 2.4, -1.92)
    glVertex3f(2.73, 2.4, 0.46)
    glVertex3f(2.73, 0.0, 0.46)

    # Parte del baño
    ab = np.array((2.61, 2.4, -2.04)) - np.array((2.61, 0.0, -2.04))
    ac = np.array((2.61, 0.0, 0.34)) - np.array((2.61, 0.0, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.61, 0.0, -2.04)
    glVertex3f(2.61, 2.4, -2.04)
    glVertex3f(2.61, 2.4, 0.34)
    glVertex3f(2.61, 0.0, 0.34)

    # Parte de arriba
    ab = np.array((2.61, 2.4, -2.04)) - np.array((2.73, 2.4, -1.92))
    ac = np.array((2.73, 2.4, 0.46)) - np.array((2.73, 2.4, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2.73, 2.4, -1.92)
    glVertex3f(2.61, 2.4, -2.04)
    glVertex3f(2.61, 2.4, 0.34)
    glVertex3f(2.73, 2.4, 0.46)

    # PARED DE LA HABITACIÓN AMARILLA CON EL BAÑO
    # Parte de la habitacion
    ab = np.array((0.67, 2.4, -1.92)) - np.array((0.67, 0.0, -1.92))
    ac = np.array((0.67, 0.0, 0.46)) - np.array((0.67, 0.0, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.67, 0.0, -1.92)
    glVertex3f(0.67, 2.4, -1.92)
    glVertex3f(0.67, 2.4, 0.46)
    glVertex3f(0.67, 0.0, 0.46)

    # Parte del baño
    ab = np.array((0.79, 2.4, -2.04)) - np.array((0.79, 0.0, -2.04))
    ac = np.array((0.79, 0.0, 0.34)) - np.array((0.79, 0.0, -2.04))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.79, 0.0, -2.04)
    glVertex3f(0.79, 2.4, -2.04)
    glVertex3f(0.79, 2.4, 0.34)
    glVertex3f(0.79, 0.0, 0.34)

    # Parte de arriba
    ab = np.array((0.79, 2.4, -2.04)) - np.array((0.67, 2.4, -1.92))
    ac = np.array((2.67, 2.4, 0.46)) - np.array((0.67, 2.4, -1.92))
    normal = np.cross(ab, ac)
    glNormal3fv(normal)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.67, 2.4, -1.92)
    glVertex3f(0.79, 2.4, -2.04)
    glVertex3f(0.79, 2.4, 0.34)
    glVertex3f(2.67, 2.4, 0.46)
    glEnd()

camaraPos = [10.0,10.0, 10.0]
camaraFront = [-1.0,-1.0, -1.0]
camaraUp = [0.0,1.0, 0.0]
camaraSpeed = 2.5
rotarIzq = 0
rotarDer = 0
rotarArri = 0
rotarAbaj = 0
yaw = -145
pitch = -45
ilum = 0

def teclado(btecla, x, y):
    tecla = btecla.decode("utf-8")
    global camaraPos
    global camaraFront
    global camaraUp
    global camaraSpeed
    global rotarIzq
    global rotarDer
    global rotarArri
    global rotarAbaj
    global yaw
    global pitch
    global ilum

    camaraSpeed = 0.1

    if tecla == 'd':
        print("TECLA d: Desplazamiento a la derecha")
        cruz = np.cross(camaraFront, camaraUp)
        normal = np.linalg.norm(cruz)
        vector = cruz/normal
        camaraPos[0] += vector[0] * camaraSpeed
        camaraPos[1] += vector[1] * camaraSpeed
        camaraPos[2] += vector[2] * camaraSpeed

    if tecla == 'a':
        print("TECLA a: Desplazamiento a la izquierda")
        cruz = np.cross(camaraFront, camaraUp)
        normal = np.linalg.norm(cruz)
        vector = cruz / normal
        camaraPos[0] -= vector[0] * camaraSpeed
        camaraPos[1] -= vector[1] * camaraSpeed
        camaraPos[2] -= vector[2] * camaraSpeed
    if tecla == 'w':
        print("TECLA w: Desplazamiento hacia adelante")
        val = np.array(camaraSpeed) * np.array(camaraFront)
        camaraPos[0] += val[0]
        camaraPos[1] += val[1]
        camaraPos[2] += val[2]
    if tecla == 's':
        print("TECLA s: Desplazamiento hacia atras")
        val = np.array(camaraSpeed) * np.array(camaraFront)
        camaraPos[0] -= val[0]
        camaraPos[1] -= val[1]
        camaraPos[2] -= val[2]
    if tecla == 'u':
        print("TECLA u: Rotación hacia arriba")
        pitch += 2
    if tecla == 'j':
        print("TECLA j: Rotación hacia abajo")
        pitch -= 2
    if tecla == 'h':
        print("TECLA h: Rotación a la izquierda")
        yaw -= 2
    if tecla == 'k':
        print("TECLA k: Rotación a la derecha")
        yaw += 2


def rotarCamara():
    global yaw
    global pitch
    global camaraFront
    direccion = [0,0, 0]

    if (pitch > 89.0):
        pitch = 89.0
    if (pitch < -89.0):
        pitch = -89.0

    direccion[0] = cos(radians(yaw)) * cos(radians(pitch))
    direccion[1] = sin(radians(pitch))
    direccion[2] = sin(radians(yaw)) * cos(radians(pitch))

    normal = np.linalg.norm(direccion)
    camaraFront = direccion/normal

def moverCamara():
    global camaraFront
    global camaraUp
    frontUp = np.array(camaraPos) + np.array(camaraFront)

    posicion = (0, 10, 10)
    target = (0, 0, 0)
    cabeza = (0, 1, 0)
    direccion = np.array(posicion) - np.array(target)
    derecha0 = np.cross(cabeza, posicion)
    derecha = np.linalg.norm(derecha0)
    derecha1 = derecha0/derecha
    arriba = np.cross(direccion, derecha1)


    gluLookAt(camaraPos[0], camaraPos[1], camaraPos[2],
              frontUp[0], frontUp[1], frontUp[2],
            camaraUp[0], camaraUp[1], camaraUp[2])



def ejes():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3d(-500, 0, 0)
    glVertex3d(500, 0, 0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3d(0, -500, 0)
    glVertex3d(0, 500, 0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3d(0, 0, -500)
    glVertex3d(0, 0, 500)
    glEnd()


def setMarerial(ambientR, ambientG, ambientB, diffuseR, diffuseG, diffuseB, specularR, specularG, specularB, shininess):
    ambient = (ambientR, ambientG, ambientB)
    diffuse = (diffuseR, diffuseG, diffuseB)
    specular = (specularR, specularG, specularB)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)

def showScreen():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterar()

    setMarerial(0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.5, 0.5, 0.5, 1)
    glPushMatrix()
    cube()
    ejes()
    glLoadIdentity()
    glPushMatrix()
    iluminacion()
    glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()

def iterar():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60, 1, 1, 200)
    rotarCamara()
    moverCamara()

    glMatrixMode(GL_MODELVIEW)

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

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

def main():
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Modelo 3D")

    glutDisplayFunc(showScreen)

    glutKeyboardFunc(teclado)
    glutIdleFunc(showScreen)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glEnable(GL_BLEND)
    InitGL()

    glutMainLoop()


if __name__ == "__main__":
    main()