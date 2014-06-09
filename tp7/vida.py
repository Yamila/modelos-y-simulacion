# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from entorno import *
zoom = 1
inicial = 'inicial.txt'
filas = 10
columnas = 10
cant_pulsos = 10

#Principal
def main():
	ancho = zoom*200 # 300
	alto = zoom*200 # 300
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('Juego de la Vida')
	entorno = Entorno(ancho,alto,filas,columnas,pantalla,inicial)
	pulsos = 1
	while True:
		for e in pygame.event.get():
			if (e.type == QUIT):
				pygame.quit()
				sys.exit()
		entorno.dibujar_fondo()
		entorno.imprimir()	
		if pulsos<=cant_pulsos:
			print 'pulso:', pulsos
			for f in range(entorno.filas):
				for c in range(entorno.columnas):
					entorno.actualizar(f,c)
					#entorno.actualizar_tablero()
					#entorno.imprimir()
		entorno.actualizar_tablero()
		pulsos= pulsos + 1			
		pygame.display.flip()
		pygame.time.wait(600) 

if __name__ == '__main__':
	pygame.display.init()
	main()