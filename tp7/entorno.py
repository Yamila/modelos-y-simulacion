# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *

#Conf_inicial --> sera un archivo txt con la configuracion inicial del juego de la vida

class Entorno:
	def __init__(self, ancho, alto,pantalla,conf_inicial):
		self.pantalla = pantalla
		self.ancho = ancho
		self.alto = alto
		#mantiene la relacion del tamanio de la pantalla con los demas objetos
		self.inicial = self.cargar_inicial(conf_inicial)
		#teblero con el contenido
		self.contenido = self.cargar_contenido()
		self.x_aumento = self.ancho/self.columnas
		self.y_aumento = self.alto/self.filas
		self.estados = self.cargar_estados()
		self.fondo = pygame.Surface((ancho,alto)).convert()
		self.dibujar_fondo()

	def cargar_inicial(self,ruta):
		archivo = file(ruta, 'rt')
		contenido = archivo.readlines()
		archivo.close()
		self.filas = len(contenido) 
		self.columnas = len(contenido[0]) -1
		return contenido


	#determinar las posiciones de la mesa
	def cargar_contenido(self):
		contenido = []
		for x in range(self.filas):
			fila = []
			for y in range(self.columnas):
				fila.append(int(self.inicial[x][y]))
			contenido.append(fila)
		return contenido

	def cargar_estados(self):
		#Cargar estados posibles(0-False-Muerta)(1-True-Viva)
		estados = []
		for i in range(2):
			img = pygame.image.load('%d.png' %i).convert_alpha()
			img = pygame.transform.scale(img, (self.x_aumento,self.y_aumento))
			estados.append(img)
		return estados

	def dibujar_fondo(self):
		self.fondo.fill((0, 0, 0))
		for f in range(self.filas):
			for c in range(self.columnas):
				indice = int(self.contenido[f][c])
				pos_x = c* self.x_aumento
				pos_y = f* self.y_aumento
				self.fondo.blit(self.estados[indice],(pos_x,pos_y))
	
	def imprimir(self):
		self.pantalla.blit(self.fondo,(0,0))
		
	def vida(self,x,y):
		if (x<0 or y<0):
			return False
		try:
			ubicacion = self.contenido[x][y]
		except:
			return False
		if ubicacion==1:
			return True
		return False

	def aplicar_regla(self,x,y,proximo):
		esta_viva = self.vida(x,y)
		vecinos = 0
		# contar los vecinos vivos que tiene
		v_x = x -1
		v_y = y -1
		for i in range(3):
			for j in range(3):
				if self.vida(v_x+i,v_y+j) is True:
					vecinos = vecinos + 1
		if esta_viva is True:
			vecinos= vecinos - 1
		# Reglas
		if (esta_viva is True) and (vecinos==2 or vecinos==3):	
			proximo.append(1)
		elif (esta_viva is False) and vecinos==3:
			proximo.append(1)
		else:
			proximo.append(0)
		return proximo

	def actualizar_tablero(self,proximo):
		self.contenido = proximo[:]