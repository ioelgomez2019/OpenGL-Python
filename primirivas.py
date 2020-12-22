# -*- coding: utf-8 -*-
"""
Created 14/12/2020 horas15:00

@author: joel santos
"""

# pip install pygame
# pip install PyOpenGL

# Lo que debemos conocer de la LibrerÃ­a OpenGL
# GL: La libreria GL basica, trae los comando primitivos
# GLU: Utilities, comandos mas complejos, Cilindro 3D
# GLX: X-Window comando parea dibujar las formas en Windows
# GLUT: Toolkit: trae caracteristicas mucho mas sofisticadas
import pygame # as pyg
from pygame.locals import *



from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from random import*
from math import*
#colores para el pygame

# Esta seccion serÃ¡ para dibujar las primitivas
def Punto():
    glBegin(GL_POINTS)
    pos_x = 0.50
    pos_y = 0.50
    """r = random()
    g = random()
    b = random()"""
    glColor3fv([1,0,0])
    
    """para la parabola
    #x = randrange(-750,750)/750
    for x in range(-50,50):
        #y = randrange(-600,600)/600
        x = x/50
        glVertex2f(x, x*x-0.9)
      """


    for x in range(-50,50):
        #y = randrange(-600,600)/600
        x = x/50
        glVertex2f(x, x*x-0.9)
    
    glColor3fv([1,0,0])
    glVertex2f(pos_x, pos_y)
    glEnd()
def figura():
    glBegin(GL_LINE_LOOP)

    r = random()
    g = random()
    b = random()
    glColor3fv([r,g,b])
    glVertex2f(0.5,0.5)
    glVertex2f(0.5,-0.5)
    glVertex2f(-0.5,-0.5)
    glVertex2f(-0.5,0.5)
    glVertex2f(0.0,0.8)
    glVertex2f(0.5,0.5)
    glEnd();
def Curva():
    glBegin(GL_LINE_LOOP)

    X,Y,R,L = 0.9,0.9,0,0
    r = random()
    g = random()
    b = random()
    glColor3fv([r,g,b])
    #contruccion grafica
    for x in range( L):
        p1 = R * cos(x*2*pi/L) + X
        p2 = R * sin(x*2*pi/L) + Y
        glVertex2f(p1,p2)
    glEnd()
def Reloj():
    L,R = 360,0.4
    X,Y = 0,0
    rm = 0.35
    glBegin(GL_LINE_LOOP)
    r = random()
    g = random()
    b = random()
    glColor3fv([1,0,0])
    for i in range(L):
        x = R * cos(i*2*pi/L) + X
        y = R * sin(i*2*pi/L) + Y
        glVertex2f(x,y)
        
    glEnd()

    glBegin(GL_LINES)
    #LINES
    for h in range(12):
        x1=X + R*cos(h*2*pi/12)
        x2=X + rm*cos(h*2*pi/12)
        y1=Y + R*sin(h*2*pi/12)
        y2=Y +rm*sin(h*2*pi/12)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
    glEnd()
    #manecilla
    
    
    
    
def Main():
    #INICIALIZAMOS
    pygame.init()
    ANCHO = 800
    ALTO = 600
    BLANCO = (255,255,255)
    NEGRO = (0,0,0)
    ROJO = (255,0 ,0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)
    pantalla = [ANCHO, ALTO]
    #PANTALLA
    """, pygame.FULLSCREEN"""
    pygame.display.set_mode(pantalla, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Primitivas en Computacicion Grafica')
    
    coords =[]
    for x in range(50):
        cxy = []
        cxy.append(randrange(-750,750)/750)
        cxy.append(randrange(-600,600)/600)

        coords.append(cxy)
    print(coords)
    #BUCLE PRINCIPAL
    Close = False
    while not Close:
        #Eventos
        for event in pygame.event.get():
            #Eventoq eu con la X se cierra
            if event.type == pygame.QUIT:
                Close = True
            #evento par que con la Qse cierre
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                     Close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                     Close = True
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #logica
        #pos_x = pos_x+0.001
        #pos_y = pos_y+0.001
        
        # Llama a las funciones de las primitivas DIBUJOS
        #for x in range(50):
        #Punto()
        #figura()
        Curva()
        Reloj()
            
            
        #pygame.draw.rect(pantalla, (255,255,255),(10,10,100,100))
        #actualizar
        pygame.display.flip()
        pygame.time.wait(10)
        pygame.time.delay(60)
        #pygame.display.update()

    #salir
    pygame.quit()

Main()    
    
