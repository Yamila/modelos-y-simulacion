# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
import pygame, sys
from pygame.locals import *
#corresponde al tamanio del archivo mapa.txt
filas = 20
columnas = 30

class Sala:
	def __init__(self, ancho, alto, pantalla):
		self.pantalla = pantalla
		self.ancho = ancho
		self.alto = alto
		#mantiene la relacion del tamanio de la pantalla con los demas objetos
		self.x_aumento = self.ancho/columnas
		self.y_aumento = self.alto/filas
		self.filas = filas
		self.columnas = columnas
		# la tabla que representa el mapa
		self.mapa = self.cargar_mapa('mapa.txt')
		self.objetos = self.cargar_objetos_sala()
		self.fondo = pygame.Surface((ancho,alto)).convert()
		self.dubujar_fondo()
		self.mesa = self.cargar_mesa()

	def cargar_mapa(self,ruta):
		archivo = file(ruta, 'rt')
		contenido = archivo.readlines()
		archivo.close()
		return contenido

	#determinar las posiciones de la mesa
	def cargar_mesa(self):
		posiciones = []
		for x in range(self.columnas):
			for y in range(self.filas):
				if self.mapa[y][x] == '2':
					posiciones.append([x,y])
		return posiciones

	def cargar_objetos_sala(self):
		#cargar los diferentes objetos que hay en la sala...piso,pared,mesa,etc
		# 0 -->piso 1-->pared 2 -->mesa
		objetos = []
		for i in range(3):
			#puedo poner una imagen
			img = pygame.image.load('%d.png' %i).convert_alpha()
			img = pygame.transform.scale(img, (self.x_aumento,self.y_aumento))
			objetos.append(img)
		return objetos

	def dubujar_fondo(self):
		self.fondo.fill((0, 0, 0))
		for f in range(filas):
			for c in range(columnas):
				indice = int(self.mapa[f][c])
				pos_x = c* self.x_aumento
				pos_y = f* self.y_aumento
				self.fondo.blit(self.objetos[indice],(pos_x,pos_y))
	
	def imprimir(self):
		self.pantalla.blit(self.fondo,(0,0))
	
	def libre(self,columna,fila):
	# Verificar si la posicion en fila y columna esta ocupada o no.
	# Columna x , Fila y
		x = columna
		y = fila
		try:
			ubicacion = self.mapa[y][x]
		except:
			return False
		if ubicacion == '0':
			return True
		return False

	def libre_de_invitados(self,columna,fila,invitados):
		for i in invitados:
			if [columna,fila] == i.posicion:
				return False
		return True
