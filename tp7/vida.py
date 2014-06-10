# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from entorno import *
zoom = 1
inicial = 'inicial.txt'
cant_pulsos = 1000000

#Principal
def main():
	ancho = zoom*200 # 300
	alto = zoom*200 # 300
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('Juego de la Vida')
	entorno = Entorno(ancho,alto,pantalla,inicial)
	pulsos = 1
	while True:
		for e in pygame.event.get():
			if (e.type == QUIT):
				pygame.quit()
				sys.exit()
		entorno.dibujar_fondo()
		entorno.imprimir()	
		if pulsos<=cant_pulsos:
			proximo = []
			for f in range(entorno.filas):
				fila = []
				for c in range(entorno.columnas):
					fila= entorno.aplicar_regla(f,c,fila)
				proximo.append(fila)
		pulsos= pulsos + 1			
		entorno.actualizar_tablero(proximo)
		pygame.display.flip()
		pygame.time.wait(160) 

if __name__ == '__main__':
	pygame.display.init()
	main()