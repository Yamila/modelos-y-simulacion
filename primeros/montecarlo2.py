# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Asignatura: Modelo y Simulacio
# Trabajo de Clase: 21-Abril-2014
# Aleatorios con Integrales
# Integrales con Simulacio
# Metodo de Montecarlo
from random import *

def f(x):
	funcion = (0.6*(x**2))
	return funcion

# Le tengo que indicar la cantidad de dardos que que voy a tirar 
def tirar(cant):	
	si = 0
	for i in range(1,cant):
			x = 0.5 + (2 * random())
			y = 3.75 *random()
			if y < f(x) :
				si = si + 1
				#print si
	
	st = float(si)/float(cant)
	integral = st *(3.75*2)				
	print '  {0:10}   | {1:7} | {2:7}'.format(cant,st,integral)

print ''
print '  {0:10}   | {1:7} | {2:7}'.format('      cant','     I','Integral')
tirar(100)
tirar(1000)
tirar(10000)
tirar(100000)