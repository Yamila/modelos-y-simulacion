# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from color import *
#Menu para usar en cualquier juego
#tupla = ('Nuevo juego', funcion_para_iniciar_el_juego)

class Menu:
	def __init__(self,opciones,pantalla,fondo,ancho,alto):
		self.opciones = opciones
		self.seleccionado = False
		self.mantiene_pulsado = False
		self.ancho = ancho
		self.alto = alto
		self.screen = pantalla
		self.fondo = fondo
		self.font = pygame.font.Font(None, 40)
	
	def actualizar(self):
		# Altera el valor de self.seleccionado	
		tecla = pygame.key.get_pressed()
		if not self.mantiene_pulsado:
			if tecla[K_UP]:
				self.seleccionado -= 1
			elif tecla[K_DOWN]:
				self.seleccionado += 1
			elif tecla[K_RETURN]:
				titulo,funcion = self.opciones[self.seleccionado]
				funcion()
		if self.seleccionado < 0:
			self.seleccionado = self.seleccionado + len(self.opciones)
		self.seleccionado = self.seleccionado % len(self.opciones)
		self.mantiene_pulsado = (tecla[K_UP] or tecla[K_DOWN] or tecla[K_RETURN])
		
	def imprimir(self):
		# Imprime en la pantalla las opciones del menu
		total = len(self.opciones)
		indice = 0
		altura_de_opcion = 40
		x = self.ancho/3
		y = self.alto/4
		for (titulo,funcion) in self.opciones:
			if indice == self.seleccionado:
				color = verde
				self.font = pygame.font.Font(None, 33)
			else: 
				color = verde_oscuro
				self.font = pygame.font.Font(None, 30)
			text = self.font.render(titulo, 1, color)
			posicion = (x, y + altura_de_opcion * indice)
			indice += 1
			self.screen.blit(text, posicion)
		