# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Asignatura: Modelo y Simulacio
# Trabajo de Clase: 14-Abril-2014
# Integrales definidas
def f(x):
	funcion = (-0.5*(x**2)) + 0.5
	return funcion
def sumatoria(a,b,h):
	s = 0
	i = a+h
	while i <= (b-h):
		s=s+f(i)
		i = i +h	
	return 2*s	

n = float(raw_input('Ingrese la cantidad de Intervalos: '))
a = float(raw_input('Ingrese el limite a: '))
b = float(raw_input('Ingrese el limite b: '))

h = (b-a)/n
integral = (h/2)*(f(a)+f(b)+(sumatoria(a,b,h)))
error = 0.2 - integral
print 'para h:',h, '. La integral: ',integral,' Error: ',error