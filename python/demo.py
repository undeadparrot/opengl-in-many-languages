import sys
import ctypes
import pygame as pg
import numpy
from OpenGL import GL
from OpenGL.arrays import ArrayDatatype

DATA = numpy.array([
    # x     y    z     r    g    b     
     0.5,  0.9, 0.0,  #1.0, 0.0, 0.0,
     0.9, -0.9, 0.0,  #0.0, 1.0, 0.0,
    -0.9, -0.9, 0.0,  #0.0, 0.0, 1.0,
    ], dtype="float32")

VERTEX_SHADER_SOURCE = \
    """#version 120
    attribute vec3 aPos;
    //attribute vec3 aColor;
    varying vec3 oColor;
    void main(){
        gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
        oColor = vec3(0.7, 0.8, 0.9);//aColor;
    }
    """

FRAGMENT_SHADER_SOURCE = \
    """#version 120
    varying vec3 oColor;
    void main(){
        gl_FragColor= vec4(oColor, 1.0);
    } 
    """

def compile_shader(source: str, type_: int) -> int:
    id_ = GL.glCreateShader(type_)
    GL.glShaderSource(id_, source)
    GL.glCompileShader(id_)
    error_msg = GL.glGetShaderInfoLog(id_)
    if error_msg:
        raise Exception(error_msg)
    return id_

def compile_shader_program(vertex_source: str, fragment_source: str) -> int:
    vs = compile_shader(vertex_source, GL.GL_VERTEX_SHADER)
    fs = compile_shader(fragment_source, GL.GL_FRAGMENT_SHADER)
    prog = GL.glCreateProgram()
    GL.glAttachShader(prog, vs)
    GL.glAttachShader(prog, fs)
    GL.glLinkProgram(prog)
    return prog


def init():
    pg.init()
    pg.display.set_mode((320,240), pg.OPENGL|pg.DOUBLEBUF)
    GL.glClearColor(0.1, 0.2, 0.3, 1.0)

    prog = compile_shader_program(VERTEX_SHADER_SOURCE, FRAGMENT_SHADER_SOURCE)
    GL.glUseProgram(prog)

    vbuf = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbuf)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(DATA), DATA,  GL.GL_STATIC_DRAW)

    a_pos = GL.glGetAttribLocation(prog, 'aPos')
    a_color = GL.glGetAttribLocation(prog, 'aColor')
    GL.glEnableVertexAttribArray(a_pos)
    #GL.glEnableVertexAttribArray(a_color)
    GL.glVertexAttribPointer(
            index=a_pos,
            size=3,
            type=GL.GL_FLOAT,
            normalized=GL.GL_FALSE,
            stride=0,
            pointer=None#)ctypes.c_voidp(0)
    )
    #GL.glVertexAttribPointer(
    #        index=a_color,
    #        size=3,
    #        type=GL.GL_FLOAT,
    #        normalized=False,
    #        stride=6*4,
    #        pointer=ctypes.c_voidp(3*4)
    #)


init()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glDrawArrays(GL.GL_LINE_STRIP, len(DATA)//3, 0)
    pg.display.flip()

