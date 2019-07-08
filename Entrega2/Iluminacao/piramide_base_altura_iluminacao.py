from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys

import random

b = int(sys.argv[1]) if len(sys.argv) > 1 else 3
h = int(sys.argv[2]) if len(sys.argv) > 2 else 2

anguloBase = (2*pi)/b

vertices = (
    (0,h,0),
    )

linhas = ()
faces = ()
angulo = 2*pi
for x in range(0, b):
    vertices += (((cos(angulo),0, -sin(angulo))),)
    linhas = ((0,x+1),)
    angulo += anguloBase

    if(x+1 == b):
        linhas += ((b,1),)
        faces += ((0,b,1),)
    else:
        linhas += ((x+1,x+2),)
        faces += ((0,x+1,x+2),)
    
aux = ()
for x in range(1, b+1):
    aux += ((x,))        
    # v -a + f =2
base = ()
base += ((aux),)

def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    V = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def Piramide():
	glBegin(GL_TRIANGLES)
	for face in faces:
		glNormal3fv(calculaNormalFace(face))
		for vertex in face:
			glVertex3fv(vertices[vertex])
	glEnd()

	for face in base:
		glBegin(GL_POLYGON)
		glNormal3fv(calculaNormalFace(face))
		for vertex in face:
	    		glVertex3fv(vertices[vertex])
	glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,5,0,0,0,0,1,0)

def init():
    mat_ambient = (0.0, 0.0, 0.5, 1.0)
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (0.0, 1.0, 0.0, 1.0)
    mat_shininess = (50,)
    light_position = (0.5, 0.5, 0.5)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Piramide")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()


