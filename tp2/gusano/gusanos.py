# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from math import *
from color import *
from random import *
# Constantes
ancho = 800 
alto = 500
sincronizar = 100000
radio = 8
grosor = 1
tam = 25 # Tamaño del gusano
angulo = 10
# Distancia entre una parte del cuerpo y la siguiente
distancia = 8  

def seny(grados):
    return sin(radians(grados))

def cosx(grados):
    return cos(radians(grados))

def main():
	
	def borrar(posicion):
		pygame.draw.circle(fondo,negro,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))
	
	def dibujar_gusano(posicion):
		pygame.draw.circle(fondo,rojo,(posicion[0],posicion[1]),radio,grosor)
		pantalla.blit(fondo,(0,0))
	
	# ( Direccion, [posicion x , posicion y] )	
	def proxima_posicion(d,posicion):
		x = posicion[0]
		y = posicion[1]
		cambio = random()
		if cambio < 0.5:
			d = d + angulo 
		else:
			d = d - angulo
		xnuevo = x + distancia* cosx(d)
		ynuevo = y + distancia* seny(d)
		xnuevo = xnuevo % ancho
		ynuevo = ynuevo % alto
		if xnuevo < 0:
			xnuevo = xnuevo + ancho
		if ynuevo < 0:
			ynuevo = ynuevo + alto
		return (d,[int(xnuevo),int(ynuevo)])			

	def crear_gusano(direccion):		
		cuerpo = []
		# determinar aleatoriamente el punto inicial
		x = int(random()*ancho)
		y = int(random()*alto)
		# Agregar las coordenadas en partes del Cuerpo
		cuerpo.append([x,y])
		dibujar_gusano(cuerpo[0])
		for i in range(0,(tam-1)):
			# Para obtener la proxima direccion le paso la direccion y la cabeza
			direccion,nueva_cabeza = proxima_posicion(direccion,cuerpo[i])
			cuerpo.append(nueva_cabeza)
			dibujar_gusano(cuerpo[i+1])
		return cuerpo,direccion		
	
	def mover_gusano(direccion,cuerpo,cola,cabeza):
		cola = (cola % tam) # Puntero de la cola
		borrar(cuerpo[cola])
		eracola = cola
		cabeza = (cabeza % tam)
		direccion,nueva_cabeza = proxima_posicion(direccion,cuerpo[cabeza])
		cuerpo[eracola] = nueva_cabeza
		dibujar_gusano(cuerpo[eracola])
		cola = cola + 1
		cabeza = cabeza + 1	
		return direccion,cuerpo,cola,cabeza

	#crear ventana 
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('GUSANOS')
	clock = pygame.time.Clock()
	fondo = pygame.display.get_surface()
	fondo = fondo.convert() #convertir la superficie al mismo formato de píxel que la pantalla
	fondo.fill(negro)
	direccion = 0 # direccion inicial
	cola = 0
	cuerpo,direccion = crear_gusano(direccion)
	cabeza = len(cuerpo)-1
	#Bloque principal
	while True: 
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		for i in range(1, sincronizar):
			a = 1	
		direccion,cuerpo,cola,cabeza = mover_gusano(direccion,cuerpo,cola,cabeza)	
		pygame.display.flip()
		pygame.display.update()

#PRINCIPAl
if __name__ == '__main__':
	#Crear el gusano o los gusanos
  	pygame.init()
  	main()