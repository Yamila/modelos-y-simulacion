# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from color import *
from random import *
from menu import *
from actores import *
from escena import *
ancho = 800
alto = 400

def hoyo_en_uno():
	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert()
	fondo.fill(negro)
	sincronizar = 60
	# Creo todos los actores
	escena = Escena(fondo,pantalla,ancho,alto)
	campo = Campo(ancho,alto)
	bola = Bola(ancho,alto)
	palo = Palo(bola)
	hoyo = Hoyo(ancho,alto,bola)
	escena.dibujar_actores(campo,bola,palo,hoyo)
	puntaje = 0
	#Bloque principal
	while True: 	
		escena.dibujar_actores(campo,bola,palo,hoyo)
		clock.tick(60)
		#Tomamos la entrada del teclado
		teclado = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		if teclado[K_ESCAPE]:
			return True
			#principal()
		#Orientacion
		if teclado[K_UP]:
			palo.orientacion -= 10 
		if teclado[K_DOWN]:
			palo.orientacion += 10
		# Velocidad
		if teclado[K_RIGHT]:
			palo.velocidad -= 1
		if teclado[K_LEFT]:
			palo.velocidad += 1
		if teclado[K_SPACE] and bola.detenida:
			bola.tirar(palo.orientacion,palo.velocidad)
		# tiene que darle la orientacion que quiere
		if bola.detenida is True:
			escena.borrar_palo(palo,campo)
			palo.recalcular(bola)
			escena.dibujar_palo(palo)
			escena.dibujar_limite(campo)			
		else:
			# Efecto cuando golpea la pelota
			while palo.velocidad>=0:
				palo.velocidad -= 1
				escena.borrar_palo(palo,campo)
				palo.recalcular(bola)
				escena.dibujar_palo(palo)
			
			escena.borrar(bola,campo)
			escena.dibujar_limite(campo)
			bola.avanzar()
			escena.dibujar_circulo(bola)
			hoyo.comprobar(bola)
			print(palo.tiros)
			if (bola.adentro is True) or (palo.tiros > 2):
				puntaje = (300 - 100*palo.tiros) + 100 
				#pygame.time.delay(100)
				print puntaje
				#fin_juego(puntaje)
			if bola.velocidad == 0: 
				palo.reiniciar(bola)
		pygame.time.delay(sincronizar)
		pygame.display.flip()
		pygame.display.update()

def salir():
	pygame.quit()
	sys.exit()

#PRINCIPAl
if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode((ancho,alto))
	opciones = [
			("Hoyo en Uno",hoyo_en_uno),		
			("Salir",salir),
			]
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
