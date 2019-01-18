import sys
import pygame as pg
from OpenGL import GL

pg.init()
pg.display.set_mode((320,240), pg.OPENGL|pg.DOUBLEBUF)

GL.glClearColor(0.1, 0.2, 0.3, 1.0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    pg.display.flip()

