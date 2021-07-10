import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

w, h = 500, 500

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
texturas = []

def loadTexture(name):
    texture = Image.open(name)
    textureData = texture.convert('RGB').tobytes()
    width = texture.width
    height = texture.height
    texturas.append((textureData, width, height))

def loadTextures(textureData, width, height):
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    return texid

def square(x, y, z, n, i, c):
    # r, g, b = c
    loadTextures(c[0], c[1], c[2])
    glBegin(GL_QUADS)
    # glColor3f(r, g, b)
    if i == 0:
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x, y, z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x + n, y, z)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x + n, y + n, z)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x, y + n, z)
    elif i == 1:
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x, y, z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x, y, z + n)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x, y + n, z + n)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(x, y + n, z)
    elif i == 2:
        glTexCoord2f(0.0, 0.0)
        glVertex3f(x, y, z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(x + n, y, z)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(x + n, y, z + n)
        glTexCoord2f(0.0, 1.0)
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
            color = texturas[1]#(0, 0, 0)
            if matriz[x][y] == 0:
                color = texturas[0] #(1, 1, 1)
            cube(y * n - 1, 1 - x * n, 1 - x * n, n, color)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glPushMatrix()
    
    make_lab(laberinto)
    glPopMatrix()
    glutSwapBuffers()

def main():
    glutInit()  # Iniciamos la instancia de glut
    # glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH) # Asignamos el modelo de color que usaremos
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH) # Asignamos el modelo de color que usaremos
    glutInitWindowSize(600, 600) # Damos el tamaño de la ventana que se mostrará
    glutInitWindowPosition(0, 0) # Coordenadas en donde aparecerá la ventana en la pantalla
    glutCreateWindow("Laberinto en 3D")  # Damos un titulo para la ventana
    glEnable(GL_DEPTH_TEST) # Permite ver sin transparentar las figuras
    glutDisplayFunc(showScreen) # Designamos la función que contiene los elementos que serán mostrados en la escena
    loadTexture('wall.jpg')
    loadTexture('5.jpg')
    glutMainLoop()  # Iniciamos el loop principal

main()
