# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Objetos que seran usados en los juegos de microgolf
from random import *
from math import *
from color import *
def seny(grados):
	return sin(radians(grados))

def cosx(grados):
	return cos(radians(grados))

margen = 30
distancia_bola = margen*3

class Bola:
	def __init__(self,ancho,alto):
		self.ancho = ancho
		self.alto = alto
		self.color = blanco
		self.posicion = [distancia_bola,randint(distancia_bola,self.alto- distancia_bola)]
		self.velocidad = 0
		self.velocidad_x = 0
		self.velocidad_y = 0
		#tamanio de la pelota
		self.radio = 6
		self.grosor = self.radio
		self.fuera = False

	
	def avanzar(self):
		self.velocidad_x = self.velocidad * cosx(self.orientacion)
		self.velocidad_y = self.velocidad * seny(self.orientacion)
		#Determino la nueva posicion de la bola
		self.posicion[0] = self.posicion[0] + self.velocidad_x
		self.posicion[1] = self.posicion[1] + self.velocidad_y
		# cuando se fue del campo
		if (self.posicion[0] <0) or (self.posicion[0]>self.ancho):
			self.fuera = True
		if (self.posicion[1] <0) or (self.posicion[1]>self.alto):
			self.fuera = True

	# Determina la velociad de la bola y la orientacion cuando es golpeada por el palo	
	def tirar(self,orientacion,velocidad):
		self.velocidad = velocidad
		self.orientacion = orientacion

class Palo:
	# Es necesario crear la clase bola antes
	def __init__(self,bola):
		self.velociad = 10
		self.grosor = 2
		self.orientacion = randint(-90,90)
		self.color = rojo
		#tamanio del palo
		self.tam = 30
		# Posicion del Palo
		a = (self.tam/2) *cosx(self.orientacion)
		b = (self.tam/2) *seny(self.orientacion)
		# Originalmente bola.radio -1 
		c = (self.velociad + (bola.radio+3)) * cosx (self.orientacion)
		d = (self.velociad + (bola.radio+3)) * seny (self.orientacion)
		self.inicio = [bola.posicion[0] - c + b,bola.posicion[1] + d + a]
		self.final = [bola.posicion[0] - c - b,bola.posicion[1] + d -a ]

class Hoyo:
	# Es necesario crear la bora primero
	def __init__(self,ancho,alto,bola):
		self.radio = bola.radio + 4
		self.grosor = self.radio
		self.color = negro
		self.posicion = [ancho-(ancho/10),alto/2]



class Campo:
	def __init__(self,ancho,alto):
		self.color = verde
		self.borde = 0
		self.medida = [ancho - (margen*2),alto - (margen*2)]
		self.posicion = [margen,margen]
		self.rectangulo = (self.posicion[0],self.posicion[1],self.medida[0],self.medida[1])



