# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from math import *
from color import *
from random import *
from estrella import *
from menu import *
ancho = 500
alto = 500


def nova():
	
	def borrar(posicion,color=negro,radio=1,grosor=1):
		pygame.draw.circle(fondo,color,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))
	
	def dibujar(posicion,color=blanco, radio=1,grosor=1):
		pygame.draw.circle(fondo,color,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))

	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
	fondo.fill(negro)
	#Lista de Estrellas
	estrellas = []
	sincronizar = 0
	estrellas.append(Estrella(ancho,alto))
	#Cada cuantas vueltas crea otra estrella
	creador = 1
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
		# Creador de nuevas estrellas
		if creador == 1:	
			estrellas.append(Estrella(ancho,alto))
			estrellas.append(Estrella(ancho,alto))
			estrellas.append(Estrella(ancho,alto))
			creador = 0
		for i in estrellas:
			i.avanzar()
			borrar(i.posicion_anterior,negro,i.radio,i.grosor)
			dibujar(i.posicion,i.color,i.radio,i.grosor)
			# si la estrella salio de foco la quita de la lista de estrellas
			if i.fuera_de_foco is True:
				estrellas.remove(i)
		creador += 1
		pygame.time.delay(sincronizar)
		pygame.display.flip()
		pygame.display.update()

def salir():
	pygame.quit()
	sys.exit()

#PRINCIPAl
if __name__ == '__main__':
	opciones = [
		("VIAJE POR LAS ESTRELLAS",nova),		
		("Salir",salir),
		]
	pygame.init()
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('Nova')
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

