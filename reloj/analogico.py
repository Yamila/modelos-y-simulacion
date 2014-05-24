# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from math import *
from color import *
from reloj import *

#velocidad Normal
#sincronizar = 100099
#sincronizar_2= 40
#velocidad Radida
sincronizar = 1
sincronizar_2 = 1
ancho = 400
alto = 400
radio = 100
centrox= ancho/2
centroy= alto/2
#funciones trigonometricas
def seny(grados):
    return sin(radians(grados))
def cosx(grados):
    return cos(radians(grados))

#Retorna la posicion de la aguja x,y
def posicion_aguja(angulo):
	angulo = angulo - 90 # para que comienze en las 12
	x = cosx(angulo)
	y = seny(angulo)
	x = centrox + (x*radio)
	y = centroy + (y*radio)
	return (x,y)

def main():
	#crear ventana 
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('SIMULACION RELOJ')
	clock = pygame.time.Clock()

	def dibujar_reloj(gs,gm,gh):
		#fondo
		fondo = pygame.display.get_surface()
		fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
		fondo.fill(negro)
		#reloj digital
		font = pygame.font.Font(None, 30)
		text = font.render(r.get_hora(), 1,blanco)
		fondo.blit(text, (0, 0))
		#definir el circulo del reloj
		circulo = pygame.draw.circle(fondo, blanco, (centrox,centroy), radio, 1)
		# definir las agujas (fondo,color_aguja,posicion_comienzo(x,y),posicion_final(x,y), grosor)
		aguja_segundo = pygame.draw.line(fondo, azul, (centrox,centroy), posicion_aguja(gs) , 2)
		aguja_minuto = pygame.draw.line(fondo, verde, (centrox,centroy), posicion_aguja(gm) , 4)
		aguja_hora = pygame.draw.line(fondo, rojo, (centrox,centroy), posicion_aguja(gh), 5)
		#PONER FONDO EN PANTALLA	
		pantalla.blit(fondo,(0,0)) 

	#Loop principal del juego	
	while True: 
		clock.tick(0)
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		for i in range(1, sincronizar):
			for z in range(1,sincronizar_2):
				a = 1
		r.avanzar()
		#determinar los grados en relacion a la hora,minuto,segundo
		grados_seg = (r.segundo*360)/60
		grados_min = ((r.minuto*360)/60) + grados_seg/60
		grados_hora = ((r.hora*360)/12) + grados_min/12
		dibujar_reloj(grados_seg, grados_min, grados_hora)
		pygame.display.flip()
		pygame.display.update()


#PRINCIPAl
if __name__ == '__main__':
	#Ingreso de la hora 
	x = inicializar()
	# crear el reloj
	r = Reloj(x[0],x[1],x[2])
  	pygame.init()
  	main()