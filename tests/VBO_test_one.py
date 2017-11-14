from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGLContext.arrays import *
from OpenGL.arrays import vbo

import numpy as np
import pygame

def generateCircle(radius):
	circ_list = []

	for theta in range(0,360):
		x=np.cos(np.radians(theta))*radius
		y=np.sin(np.radians(theta))*radius
		circ_list.append([x,y,0.0])

	return circ_list

class GLContext():
	def __init__(self, screen):
		self.screen = screen
		self.aspect = screen.get_width()/screen.get_height()
		gluPerspective(30.0, self.aspect, 0.1, 200.0)


		self.vbos=[]
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(4)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(3)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(2)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(1)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(4.5)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(3.5)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(2.5)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(1.5)))))
		self.vbos.append(vbo.VBO(array(np.float32(generateCircle(.5)))))


		return

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
				exit()
		return

	def display(self):
		glClearColor(0.2,0.2,1.0,1.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		glPushMatrix()

		glTranslatef(0.0,0.0,-15.0)

		for cur_vbo in self.vbos:
			cur_vbo.bind()
			glEnableClientState(GL_VERTEX_ARRAY)
			glVertexPointerf(cur_vbo)

			glDrawArrays(GL_LINE_LOOP, 0, len(cur_vbo))

			cur_vbo.unbind()
			glDisableClientState(GL_VERTEX_ARRAY)

		glPopMatrix()

		return


def main():
	pygame.init()
	glutInit()
	screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)
	context = GLContext(screen)  

	while True:
		context.check_events()  
		context.display()  
		pygame.display.flip() 


if __name__ == '__main__':
	try:
		main()
	finally:
		pygame.quit()