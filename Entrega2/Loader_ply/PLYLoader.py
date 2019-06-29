from OpenGL.GL import *
 
import random


class PLY:
    def __init__(self, filename, swapyz=False):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.lenVertices = 0
        self.lenFaces = 0

        self.iVertices = 0
        self.iFaces = 0

        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue

            if line.startswith('ply'): continue
            
            if line.startswith('format'): continue
            
            if line.startswith('comment'): continue

            if line.startswith('property'): continue
            
            values = line.split()
            if not values: continue

            if line.startswith('element'):
                if values[1] == 'vertex':
                    self.lenVertices = int(values[2])
                    continue
                if values[1] == 'face':
                    self.lenFaces = int(values[2])
                    continue


            if line.startswith('end_header'): continue
                
            if(self.lenVertices > self.iVertices):
                v = map(float, values[0:3])
                self.vertices.append(v)
                self.iVertices +=1
                continue
            

            if(self.lenFaces > self.iFaces):
                vf = map(int, values[1:4])
                self.faces.append([self.vertices[vf[0]],self.vertices[vf[1]],self.vertices[vf[2]]])
                self.iFaces += 1
                continue

        self.gl_list = glGenLists(1) 
        glNewList(self.gl_list, GL_COMPILE)
        glBegin(GL_TRIANGLES)

        for face in self.faces:
            #print(face)
            for i in range(3):
                glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
                #print(face[i][0])
                glVertex3fv(face[i])    
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()
            
            

            
        """ self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glFrontFace(GL_CCW)
        for face in self.faces:
            vertices, normals, texture_coords, material = face
 
            mtl = self.mtl[material]
            if 'texture_Kd' in mtl:
                # use diffuse texmap
                glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
            else:
                # just use diffuse colour
                glColor(*mtl['Kd'])
 
            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList() """

#arq = PLY("bun_zipper_res4.ply")