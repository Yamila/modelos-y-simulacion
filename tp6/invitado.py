# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
from random import *
import math

blanco = (255,255,255)

class Invitado:

	def __init__(self, nombre,inicial,sala):
		self.sala = sala
		self.nombre = nombre
		self.inicial = inicial
		#self.img = imagen
		libre = False
		#definir la posicion inicial del invitado y que no sea un lugar que no puede estar
		while not libre:
			x = (randint(0,sala.columnas-1))
			y = (randint(0,sala.filas-1)) 
			if self.sala.mapa[y][x] == '0':
				libre = True
		self.posicion = [x,y]
		#self.satisfaccion = 10000
		# diccionario con las distancias ideales a los demas invitados [invitado,distancia mts]
		self.ideal = {}


	def avanzar(self,invitados):
		#lista de las posiciones posibles
		posiciones_posibles = []
		x = self.posicion[0] - 1
		y = self.posicion[1] -1
		for i in range(3):
			for j in range(3):
				if (self.sala.libre(x+i,y+j) is True) and (self.sala.libre_de_invitados(x+i,y+j,invitados) is True):
					posiciones_posibles.append([x+i,y+j])
		presuma = 1000
		for p in posiciones_posibles:
			suma = 0
			for i in invitados:
				distancia = (p[0]-i.posicion[0])**2 + (p[1]-i.posicion[1]) **2
				distancia = math.sqrt(distancia)
				suma = suma + abs(distancia-self.ideal[i])
			#sumo tambien la mesa
			for m in self.sala.mesa:
				distancia = (p[0]-m[0])**2 + (p[1]-m[1]) **2
				distancia = math.sqrt(distancia)
				suma = suma + abs(distancia-self.ideal['mesa'])
			if suma < presuma:
				presuma = suma
				self.posicion[0] = p[0]
				self.posicion[1] = p[1]
		#self.satisfaccion = presuma

	def imprimir(self,pantalla):
		# Muestra una letra en pantalla que corresponde al invitado
		pygame.font.init()
		font = pygame.font.Font(None, self.sala.x_aumento+5)
		text = font.render(self.inicial, 1,blanco)
		pantalla.blit(text, (self.posicion[0]*self.sala.x_aumento, self.posicion[1]*self.sala.y_aumento))