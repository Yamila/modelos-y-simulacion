# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Asignatura: Modelo y Simulacio
# Trabajo de Clase: 14-Abril-2014
# Integrales definidas


def f(x):
	funcion = (0.6*(x**2))
	return funcion


def sumatoria(a,b,h):
	s = 0
	i = a+h
	while i <= (b-h):
		s=s+f(i)
		i = i +h	
	return 2*s	


#Ingreso los parametros necesarios
n = float(raw_input('Ingrese la cantidad de Intervalos: '))
a = float(raw_input('Ingrese el limite a: '))
b = float(raw_input('Ingrese el limite b: '))
# Calculo el incremento de los Intervalos. Establece la relacion entre n y h
h = (b-a)/n
#Calculo la integral definida mediante el metodo de los trapecios
integral = (h/2)*(f(a)+f(b)+(sumatoria(a,b,h)))
# El error cometido, sabiendo de antemano que la integral calculada a mano da 0.2
error = 0.2 - integral
print 'para h:',h, '. La integral: ',integral,' Error: ',error