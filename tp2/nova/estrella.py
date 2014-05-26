# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
from color import *
from random import *
from math import *

def seny(grados):
	return sin(radians(grados))

def cosx(grados):
	return cos(radians(grados))

class Estrella:
	def __init__(self,ancho,alto):
		self.ancho = ancho
		self.alto = alto
		#generar color al azar
		self.color = (randint(0,250),randint(0,250),randint(100,255))
		centro = [self.ancho/2,alto/2]
		# determina en que cuadrante aparece la estrella, angulo y posicion
		self.cuadrante = randint(1,4)
		if self.cuadrante == 1:
			self.angulo = randint(270,360) #(280,360)
			self.posicion = [randint(centro[0],centro[0]+centro[0]/3),randint(centro[1]/3,centro[1])]
		elif (self.cuadrante == 2):
			self.angulo = randint(0,90) #(30,70)
			self.posicion = [randint(centro[0],centro[0]+centro[0]/3),randint(centro[1],centro[1]+centro[1]/3)]
		elif (self.cuadrante == 3):
			self.angulo = randint(90,180) #(110,170)
			self.posicion = [randint(centro[0]/3,centro[0]),randint(centro[1],centro[1]+centro[1]/3)]
		elif (self.cuadrante == 4):
			#(190,260)
			self.angulo = randint(180,270)
			self.posicion = [randint(centro[0]/3,centro[0]),randint(centro[1]/3,centro[1])]
		self.radio = 1
		self.grosor = 1
		self.k = 5
		self.cercano = 0
		self.fuera_de_foco = False

	def avanzar(self):
		self.posicion_anterior = self.posicion
		x = self.posicion[0]
		y = self.posicion[1]
		self.k = self.k + 1
		self.cercano +=1
		# Mientras mas cerca esta la estrella, mas grande
		if self.cercano == 5:
			self.radio +=1
			self.grosor = self.radio
			self.cercano = 0
		xnuevo = x + (self.k * cosx(self.angulo))
		ynuevo = y + (self.k * seny(self.angulo))
		self.posicion = [int(xnuevo),int(ynuevo)]
		# para determinar cuando la estrella se va de la pantalla
		if (self.posicion[0]>=self.ancho+self.radio) or (self.posicion[1]>=self.alto+self.radio):
			self.fuera_de_foco = True
		if (self.posicion[0]<=(-self.radio)) or (self.posicion[1]<=(-self.radio)):
			self.fuera_de_foco = True