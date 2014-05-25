# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from math import *
from color import *
from random import *
from gota import *
from menu import *
grosor = 1
ancho = 400
alto = 400
#tamanio de la gota
tam = 10
def lluvia():
	
	def borrar(posicion,color=negro,radio = 2):
		pygame.draw.circle(fondo,color,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))
	
	def dibujar(posicion,color=blanco, radio = 1):
		pygame.draw.circle(fondo,color,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))

	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
	fondo.fill(negro)
	#Lista de GOTAS
	gotas = []
	sincronizar = 100
	#Cada cuantas vueltas crea otra gota
	creador = 3
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
		#Para Sincronizar
		if teclado[K_a]:
			sincronizar = sincronizar + 10
		if teclado[K_b]:
			sincronizar = sincronizar - 10
		if creador == 3:	
			gotas.append(Gota(ancho,alto,tam))
			creador = 0
		for i in gotas:
			i.avanzar()
			dibujar(i.centro,blanco,i.onda[i.final])
			borrar(i.centro,negro,i.onda[i.inicio])
			if i.muerta is True:
				gotas.remove(i)
		creador += 1
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
		("LLUVIA",lluvia),		
		("Salir",salir),
		]
	pygame.init()
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('LLUVIA')
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

