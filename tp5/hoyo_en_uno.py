# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from color import *
from random import *
from menu import *
from actores import *
ancho = 800
alto = 500


def hoyo_en_uno():
	
	def borrar(posicion,color=verde,radio=1,grosor=1):
		pygame.draw.circle(fondo,color,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))
	
	def dibujar_circulo(circulo):
		pygame.draw.circle(fondo,circulo.color,(circulo.posicion[0],circulo.posicion[1]),circulo.radio,circulo.grosor)
		pantalla.blit(fondo,(0,0))

	def dibujar_campo(campo):
		pygame.draw.rect(fondo,campo.color,campo.rectangulo,campo.borde)
		pantalla.blit(fondo,(0,0))

	def dibijar_palo(palo):
		pygame.draw.line(fondo, palo.color, palo.inicio, palo.final , palo.grosor)
		pantalla.blit(fondo,(0,0))
		
	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
	fondo.fill(negro)
	sincronizar = 60
	campo = Campo(ancho,alto)
	dibujar_campo(campo)
	bola = Bola(ancho,alto)
	dibujar_circulo(bola)
	palo = Palo(bola)
	dibijar_palo(palo)
	hoyo = Hoyo(ancho,alto,bola)
	dibujar_circulo(hoyo)

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
		
		pygame.time.delay(sincronizar)
		pygame.display.flip()
		pygame.display.update()

def salir():
	pygame.quit()
	sys.exit()

#PRINCIPAl
if __name__ == '__main__':
	opciones = [
		("Hoyo en Uno",hoyo_en_uno),		
		("Salir",salir),
		]
	pygame.init()
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('microgolf')
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