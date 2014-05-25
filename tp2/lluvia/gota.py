# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
from random import *

class Gota:
	def __init__(self,ancho,alto,tam):
		# En onda guardo todos los radios
		self.onda = []
		self.ancho = ancho
		self.alto = alto
		self.centro = [randint(1,self.ancho),randint(1,self.alto)]
		self.inicio = 0
		self.final = 0
		self.distancia_entre_ondas = 10
		self.cantidad_ondas = 3
		self.muerta = False

		self.tam = tam
		for i in range(0,self.tam):
			self.onda.append((i*self.distancia_entre_ondas)+2)

	def avanzar(self):
		self.final = (self.final + 1)
		if self.final >= (self.tam-1):
			self.final = self.tam -1
		if self.final >= self.cantidad_ondas:
			self.inicio += 1
		if self.inicio >= (self.tam-1):
			self.inicio = self.tam-1
		# Para saber cuando termino de recorrer toda las ondas
		if self.final == self.inicio:
			self.muerta = True	

	def no_existe(self):
		if self.final == self.inicio:
			return True
		else:
			return False	

