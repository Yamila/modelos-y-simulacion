# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from color import *
from random import *
from menu import *
from actores import *
ancho = 800
alto = 400


def hoyo_en_uno():
	# tiene que ir en cada objeto
	def borrar(circulo,objeto_fondo):
		pygame.draw.circle(fondo,objeto_fondo.color,(circulo.posicion[0],circulo.posicion[1]),circulo.radio,circulo.grosor)
		pantalla.blit(fondo,(0,0))
	
	def dibujar_circulo(circulo):
		pygame.draw.circle(fondo,circulo.color,(circulo.posicion[0],circulo.posicion[1]),circulo.radio,circulo.grosor)
		pantalla.blit(fondo,(0,0))

	def dibujar_fondo():
		pygame.draw.rect(fondo,verde_oscuro,(0,0,ancho,alto),0)
		pantalla.blit(fondo,(0,0))

	def dibujar_campo(campo):
		pygame.draw.rect(fondo,campo.color,campo.rectangulo,campo.borde)
		pantalla.blit(fondo,(0,0))

	def dibujar_palo(palo):
		pygame.draw.line(fondo, palo.color, palo.inicio, palo.final , palo.grosor)
		pantalla.blit(fondo,(0,0))
	
	def borrar_palo(palo,campo):
		pygame.draw.line(fondo, campo.color, palo.inicio, palo.final , palo.grosor)
		pantalla.blit(fondo,(0,0))

	def dibujar_limite(campo):
		pygame.draw.line(fondo, campo.limite_color, campo.limite[0], campo.limite[1] , 2)
		pantalla.blit(fondo,(0,0))	

	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
	fondo.fill(rojo)
	sincronizar = 60
	# Creo todos los actores
	campo = Campo(ancho,alto)
	bola = Bola(ancho,alto)
	palo = Palo(bola)
	hoyo = Hoyo(ancho,alto,bola)
	def dibujar_actores():
		# Dibujo todos los objetos en la pantalla
		dibujar_fondo()
		dibujar_campo(campo)
		dibujar_circulo(bola)
		dibujar_palo(palo)
		dibujar_circulo(hoyo)
		dibujar_limite(campo)	
	#Bloque principal
	while True: 	
		dibujar_actores()
		clock.tick(60)
		#Tomamos la entrada del teclado
		teclado = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		if teclado[K_ESCAPE]:
			return True
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
			borrar_palo(palo,campo)
			palo.recalcular(bola)
			dibujar_palo(palo)
			dibujar_limite(campo)			
		else:
			# Efecto cuando golpea la pelota
			while palo.velocidad>=0:
				palo.velocidad -= 1
				borrar_palo(palo,campo)
				palo.recalcular(bola)
				dibujar_palo(palo)
			borrar(bola,campo)
			dibujar_limite(campo)
			bola.avanzar()
			dibujar_circulo(bola)
			hoyo.comprobar(bola)
			
			if bola.adentro is True:
				print('Adentro!')
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