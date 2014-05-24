# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from math import *
from color import *
from random import *
from gusano import *
from menu import *
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


def snake():
	
	def borrar(posicion,color=negro):
		pygame.draw.circle(fondo,color,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))
	
	def dibujar(posicion,color=blanco):
		pygame.draw.circle(fondo,color,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))

	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
	fondo.fill(negro)
	# Crear Gusano
	gusano = Gusano(ancho,alto,angulo,distancia,radio)
	dibujar(gusano.cuerpo[gusano.cabeza],verde_snake)
	
	while  gusano.tam <= tam:
		gusano.add()
		dibujar(gusano.cuerpo[gusano.cabeza],verde_snake)
	sincronizar = 100
	comida = Comida(ancho,alto,radio)
	comida.add()
	dibujar(comida.posicion,naranja)
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
			return True
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
			sincronizar = sincronizar + 10
		if teclado[K_b]:
			sincronizar = sincronizar - 10
		borrar(gusano.cuerpo[gusano.cola])
		gusano.avanzar()
		dibujar(gusano.cuerpo[gusano.cabeza],verde_snake)
		comida.comio(gusano)
		if comida.comido is True:
			borrar(comida.posicion)
			gusano.add()
			dibujar(gusano.cuerpo[gusano.cabeza],verde_snake)
			comida.add()
			dibujar(comida.posicion,naranja)
		pygame.time.delay(sincronizar)
		pygame.display.flip()
		pygame.display.update()

def salir():
	pygame.quit()
	sys.exit()

def instrucciones():
	print('[K_UP] : Mover arriba \n [K_DOWN] : Mover abajo \n [K_LEFT] : Mover izquierda \n [K_RIGHT] : Mover Derecha \n [K_ESCAPE] : Volver al Menu')	
	return True

#PRINCIPAl
if __name__ == '__main__':
	opciones = [
		("Jugar",snake),
		("instrucciones",instrucciones),
		("Salir",salir),
		]
	pygame.init()
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('SNAKE')
	fondo_menu = pygame.display.get_surface()
	fondo_menu = fondo_menu.convert()
	menu = Menu(opciones,pantalla,fondo_menu,ancho,alto)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		menu.screen.blit(menu.fondo,(0,0))
		menu.imprimir()
		menu.actualizar()
		pygame.display.flip()
		pygame.time.delay(20)
