# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Minigolf
import pygame, sys
from pygame.locals import *
from color import *

class Escena:
	def __init__(self, fondo, pantalla, ancho,alto):
		self.fondo = fondo
		self.pantalla = pantalla
		self.ancho = ancho
		self.alto = alto

	# tiene que ir en cada objeto
	def borrar(self,circulo,objeto_fondo):
		pygame.draw.circle(self.fondo,objeto_fondo.color,(circulo.posicion[0],circulo.posicion[1]),circulo.radio,circulo.grosor)
		self.pantalla.blit(self.fondo,(0,0))

	def dibujar_circulo(self,circulo):
		pygame.draw.circle(self.fondo,circulo.color,(circulo.posicion[0],circulo.posicion[1]),circulo.radio,circulo.grosor)
		self.pantalla.blit(self.fondo,(0,0))

	def dibujar_fondo(self):
		pygame.draw.rect(self.fondo,verde_oscuro,(0,0,self.ancho,self.alto),0)
		self.pantalla.blit(self.fondo,(0,0))

	def dibujar_campo(self,campo):
		pygame.draw.rect(self.fondo,campo.color,campo.rectangulo,campo.borde)
		self.pantalla.blit(self.fondo,(0,0))

	def dibujar_palo(self,palo):
		pygame.draw.line(self.fondo, palo.color, palo.inicio, palo.final , palo.grosor)
		self.pantalla.blit(self.fondo,(0,0))

	def borrar_palo(self,palo,campo):
		pygame.draw.line(self.fondo, campo.color, palo.inicio, palo.final , palo.grosor)
		self.pantalla.blit(self.fondo,(0,0))

	def dibujar_limite(self,campo):
		pygame.draw.line(self.fondo, campo.limite_color, campo.limite[0], campo.limite[1] , 2)
		self.pantalla.blit(self.fondo,(0,0))

	def dibujar_actores(self,campo,bola,palo,hoyo):
		# Dibujo todos los objetos en la pantalla
		self.dibujar_fondo()
		self.dibujar_campo(campo)
		self.dibujar_circulo(bola)
		self.dibujar_palo(palo)
		self.dibujar_circulo(hoyo)
		self.dibujar_limite(campo)	