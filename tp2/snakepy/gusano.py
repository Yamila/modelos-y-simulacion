# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
from random import *
from math import *

def seny(grados):
    return sin(radians(grados))

def cosx(grados):
    return cos(radians(grados))

# Objeto Gusano
class Gusano:
	def __init__(self,ancho_pantalla,alto_pantalla,angulo,distancia, radio):
		# tam es el tamanio del gusano
		self.tam = 1
		self.ancho = ancho_pantalla
		self.alto = alto_pantalla
		# angulo de movimiento del gusano
		self.angulo = angulo
		# Distancia entre partes del cuerpo del gusano
		self.distancia = distancia
		# El cuerpo del gusano es una lista de posiciones [x,y]
		self.cuerpo = []
		# Posicion inicial en el medio de la pantalla
		self.cuerpo.append( [self.ancho/2,self.alto/2] )
		self.direccion = 0
		#punteros de la posicion del cuerpo
		self.cabeza = 0
		self.cola = 0
		self.d = 0
		self.radio = radio
	
	def proxima_posicion(self):
		x = self.cuerpo[self.cabeza][0]
		y = self.cuerpo[self.cabeza][1]
		xnuevo = x + self.distancia * cosx(self.direccion)
		ynuevo = y + self.distancia * seny(self.direccion)
		xnuevo = xnuevo % self.ancho
		ynuevo = ynuevo % self.alto
		if xnuevo < 0:
			xnuevo = xnuevo + self.ancho
		if ynuevo < 0:
			ynuevo = ynuevo + self.alto
		return ([int(xnuevo),int(ynuevo)])				

	# Hacer Crecer el Gusano
	def add(self):
		self.cuerpo.insert(self.cabeza,self.proxima_posicion())
		self.tam = self.tam + 1
		self.cabeza = (self.cabeza + 1) % self.tam
		self.cola = (self.cabeza + 1) % self.tam

	# Antes de avanzar se tendra que borrar la cola	
	def avanzar(self):
		self.cuerpo[self.cola] = self.proxima_posicion()
		self.cabeza = (self.cabeza + 1) % self.tam	
		self.cola = (self.cabeza + 1) % self.tam


class Comida:
	def __init__(self,ancho,alto,radio):
		self.ancho = ancho
		self.alto = alto
		self.radio = radio
		self.posicion = []
		self.comido = False

	def add(self):
		self.posicion = [randint(1,self.ancho-self.radio),randint(1,self.alto-self.radio)]
		self.comido = False

	def comio(self,gusano):
		punto = gusano.cuerpo[gusano.cabeza]
		x = self.posicion[0]
		y = self.posicion[1]
		xi,xf = x - self.radio , x + self.radio
		yi,yf = y - self.radio , y + self.radio
		if (punto[0] >= xi) and (punto[0] <= xf):
			if (punto[1]>=yi) and (punto[1]<=yf):
				self.comido = True
