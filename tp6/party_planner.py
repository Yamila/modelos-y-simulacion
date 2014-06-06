# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7

import pygame, sys
from pygame.locals import *
from sala import *
from invitado import *
zoom = 2

def ideales(lista,a,b,d,h,m,n,p,v,t):
	d = {lista[0]:a,
	lista[1]:b,
	lista[2]:d,
	lista[3]:h,
	lista[4]:m,
	lista[5]:n,
	lista[6]:p,
	lista[7]:v,
	'mesa':t}
	return d

def cargar_inivitados(sala):
	alberto = Invitado('alberto','A',sala)
	berta = Invitado('berta','B',sala)
	demetrio = Invitado('demetrio','D',sala)
	hilario = Invitado('hilario','H',sala)
	monica = Invitado('monica','M',sala)
	nemesio = Invitado('nemesio','N',sala)
	penelope = Invitado('penelope','P',sala)
	violeta = Invitado('violeta','V',sala)
	invitados = [alberto,berta,demetrio,hilario,monica,nemesio,penelope,violeta]
	alberto.ideal = ideales(invitados, 0,3,2,3.5,0.5,4.5,2,1,0.5)
	berta.ideal = ideales(invitados, 3.5,0,1,1,2.5,0.5,1.5,3.5,0.5)
	demetrio.ideal = ideales(invitados, 3.5,0.5,0,2,1.5,1,3.5,2.5,0.5)
	hilario.ideal = ideales(invitados,2,2.5,4,0,2,2,1,2.5,1.5)
	monica.ideal = ideales(invitados,2,2,1,1.5,0,2.5,3,4,1.5)
	nemesio.ideal = ideales(invitados,2.5,1,2,3,1,0,2,3,0.5)
	penelope.ideal = ideales(invitados,1,3.5,1.5,4.5,4,3,0,2,1.5)
	violeta.ideal = ideales(invitados,2,4,4,1,3,2.5,1.2,0,1.5)
	return invitados

#Principal
def main():
	ancho = zoom*300 # 300
	alto = zoom*200 # 200
	pantalla = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption('Equilibrio Social')
	sala = Sala(ancho,alto,pantalla)
	invitados = cargar_inivitados(sala)
	#invitados[0].avanzar(invitados)
	while True:
		for e in pygame.event.get():
			if (e.type == QUIT):
				pygame.quit()
				sys.exit()
		sala.imprimir()
		#invitados[1].avanzar(invitados)
		for i in invitados:
			i.avanzar(invitados)
			i.imprimir(pantalla)	
		pygame.display.flip()
		pygame.time.wait(600) 

if __name__ == '__main__':
	pygame.display.init()
	main()