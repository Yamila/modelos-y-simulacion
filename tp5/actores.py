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
		#self.mover = False
		self.detenida = True
		self.rozamiento = 10
		self.adentro = False
		self.a = self.b = 1
	def avanzar(self):
		self.rozamiento += 1
		self.velocidad_x = self.velocidad * (self.a*cosx(self.orientacion))
		self.velocidad_y = self.velocidad * (self.b*seny(self.orientacion))
		#Determino la nueva posicion de la bola
		self.posicion[0] = int(self.posicion[0] + self.velocidad_x)
		self.posicion[1] = int(self.posicion[1] + self.velocidad_y)
		# cuando se fue del campo
		limite_bola = margen + self.radio*2
		if (self.posicion[0] < limite_bola) or (self.posicion[0]>self.ancho-limite_bola):
			self.a = self.a * -1
		if (self.posicion[1] < limite_bola) or (self.posicion[1]>self.alto-limite_bola):
			self.b = self.b * -1
			#self.orientacion = self.orientacion +a#-(self.orientacion)
		# Para que se vea disminuida la velocidad a medida que corre
		if (self.rozamiento>= 10):
			self.rozamiento = 0
			self.velocidad -= 1
		if self.velocidad <= 1:
			self.detenida = True
			self.velocidad = 0

	# Determina la velocidad de la bola y la orientacion cuando es golpeada por el palo	
	def tirar(self,orientacion,velocidad):
		self.velocidad = velocidad
		self.orientacion = -(orientacion)
		self.mover = True
		self.detenida = False

class Palo:
	# Es necesario crear la clase bola antes
	def __init__(self,bola):
		self.velocidad = bola.radio + 4
		self.grosor = 4
		self.orientacion = randint(-90,90)
		self.color = color_palo
		#tamanio del palo
		self.tam = 30
		# Posicion del Palo
		a = (self.tam/2) *cosx(self.orientacion)
		b = (self.tam/2) *seny(self.orientacion)
		# Originalmente bola.radio -1 
		c = (self.velocidad + (bola.radio+3)) * cosx (self.orientacion)
		d = (self.velocidad + (bola.radio+3)) * seny (self.orientacion)
		self.inicio = [bola.posicion[0] - c + b,bola.posicion[1] + d + a]
		self.final = [bola.posicion[0] - c - b,bola.posicion[1] + d -a ]
		self.tiros = 0

	def reiniciar(self,bola):
		self.velocidad = bola.radio +4
		bola.a = bola.b = 1 
		self.tiros = self.tiros + 1
	
	def recalcular(self,bola):
		#Para que no salga de los limites
		if self.orientacion < -90:
			self.orientacion = -90
		if self.orientacion > 90:
			self.orientacion = 90
		# Posicion del Palo
		a = (self.tam/2) *cosx(self.orientacion)
		b = (self.tam/2) *seny(self.orientacion) 
		c = (self.velocidad + (bola.radio+3)) * cosx (self.orientacion)
		d = (self.velocidad + (bola.radio+3)) * seny (self.orientacion)
		self.inicio = [bola.posicion[0] - c + b,bola.posicion[1] + d + a]
		self.final = [bola.posicion[0] - c - b,bola.posicion[1] + d -a ]

class Hoyo:
	# Es necesario crear la bora primero
	def __init__(self,ancho,alto,bola):
		self.radio = bola.radio + 3
		self.grosor = self.radio
		self.color = color_hoyo
		self.posicion = [ancho-(ancho/10),alto/2]

	def comprobar(self,bola):
		# Verificar si la bola entro en el hoyo
		punto = bola.posicion
		x = self.posicion[0]
		y = self.posicion[1]
		xi,xf = x - bola.radio , x + bola.radio
		yi,yf = y - bola.radio , y + bola.radio
		if (punto[0] >= xi) and (punto[0] <= xf):
			if (punto[1]>=yi) and (punto[1]<=yf):
				bola.adentro = True
				bola.posicion = self.posicion
				bola.velocidad = 0 

class Campo:
	def __init__(self,ancho,alto):
		self.color = verde
		self.borde = 0
		self.medida = [ancho - (margen*2),alto - (margen*2)]
		self.posicion = [margen,margen]
		self.rectangulo = (self.posicion[0],self.posicion[1],self.medida[0],self.medida[1])
		#linea blanca delante de la bola
		self.limite = [(distancia_bola+10,margen),((distancia_bola+10,alto-margen))]
		self.limite_color = linea 
