# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from math import *
from color import *
from random import *
from gusano import *
# Constantes
ancho = 400
alto = 400
#sincronizar = 100000
radio = 7
grosor = 2
tam = 5 # Tamaño del gusano
angulo = 0
# Distancia entre una parte del cuerpo y la siguiente
distancia = 14  

def main():
	
	def borrar(posicion):
		pygame.draw.circle(fondo,negro,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))
	
	def dibujar(posicion):
		pygame.draw.circle(fondo,blanco,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))

	#crear ventana 
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('SNAKE')
	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
	fondo.fill(negro)
	# Crear Gusano
	gusano = Gusano(ancho,alto,angulo,distancia,radio)
	dibujar(gusano.cuerpo[gusano.cabeza])
	
	while  gusano.tam <= tam:
		gusano.add()
		dibujar(gusano.cuerpo[gusano.cabeza])
	sincronizar = 600000 	
	comida = Comida(ancho,alto,radio)
	comida.add()
	dibujar(comida.posicion)
	#Bloque principal
	while True: 	
		clock.tick(60)
		#Tomamos la entrada del teclado
		teclado = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		if teclado[K_ESCAPE]:
			pygame.quit()
			sys.exit()
		if teclado[K_UP]:
			if (gusano.direccion != 90):
				gusano.direccion = 270
		if teclado[K_DOWN]:
			if (gusano.direccion != 270):
				gusano.direccion = 90
		if teclado[K_RIGHT]:
			if (gusano.direccion != 180):
				gusano.direccion = 0
		if teclado[K_LEFT]:
			if (gusano.direccion != 0):
				gusano.direccion = 180
		#Para Sincronizar
		if teclado[K_a]:
			sincronizar = sincronizar + 100000
		if teclado[K_b]:
			sincronizar = sincronizar - 100000
		
		for i in range(1, sincronizar):
			a = 1	
		borrar(gusano.cuerpo[gusano.cola])
		gusano.avanzar()
		dibujar(gusano.cuerpo[gusano.cabeza])
		comida.comio(gusano)
		if comida.comido is True:
			borrar(comida.posicion)
			gusano.add()
			dibujar(gusano.cuerpo[gusano.cabeza])
			comida.add()
			dibujar(comida.posicion)
		pygame.display.flip()
		pygame.display.update()

#PRINCIPAl
if __name__ == '__main__':
  	pygame.init()
  	main()