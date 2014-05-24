# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7

#constantes
maxseg =  60
maxmin =  60
maxhora = 12

#Funciones para el uso de Reloj
def validar(lim_inferior,lim_superior,valor,variable):
	if (valor >= lim_inferior) & (valor <= lim_superior):
		return True
	else:
		print ("error: ",variable," es incorrecta")
		print (variable, "debe ser--> MIN=",lim_inferior," MAX=",lim_superior)
		return False

#ingreso para inicializar reloj retorna (hora,minutos,segundos) validos
def inicializar(): 
	h = int(raw_input("Ingrese la hora: "))
	while not(validar(0,maxhora, h,"Hora")):
		h = int(raw_input("Ingrese la hora: "))
	#ingreso de minutos
	m = int(raw_input("Ingrese los minutos: "))
	while not(validar(0,maxmin, m,"Minutos")):
		m = int(raw_input("Ingrese la minutos: "))
	#ingeso de segundos
	s = int(raw_input("Ingrese los segundos: "))
	while not(validar(0,maxseg, s,"Segundos")):
		s = int(raw_input("Ingrese los Segundos: ")	)
	return (h,m,s)

#CLASE RELOJ
class Reloj:

	def __init__(self,h,m,s):
		self.hora = h
		self.minuto = m
		self.segundo = s
				
	def mostrar(self):
		print '     {0:2} : {1:2} : {2:2}'.format(self.hora,self.minuto,self.segundo)
	
	#avanza un segundo y comprueba las variables que tiene que modificar		
	def avanzar(self):
		self.segundo = self.segundo + 1
		if self.segundo >= maxseg:
			self.segundo = 0
			self.minuto = self.minuto + 1
		if self.minuto >= maxmin:
			self.minuto = 0
			self.hora = self.hora +1
		if self.hora >= maxhora:
			self.hora = 0
			
	#Adelantar una cierta cantidad de segundos
	def adelantar(self,cant_seg):
		cant_seg = cant_seg +1
		for x in range(1, cant_seg):
			self.avanzar()
			self.mostrar()
	
	# retorna la hora actual para poder imprimir en pantalla hh:mm:ss				 	
	def get_hora(self):
		return '{0:2} : {1:2} : {2:2}'.format(self.hora,self.minuto,self.segundo)