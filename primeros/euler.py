# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Asignatura: Modelo y Simulacio
# Trabajo de Clase: 21-Abril-2014
# Metodo de Euler
# y' = 2xy
# y(0.5) = 1.284025

def d(x,y):
	derivada = 2*x*y 
	return derivada

def calcular(h):
	y_manual = 1.284025
	#h = float(raw_input("Ingrese el h:  "))
	xf = 8 
	#0.5 # X Final
	xi= 0 # X inicial
	yi = 1 
	s = 0
	# Solo si quiero ver el Incremento paso a paso
	#print '     {0:6}   | {1:7} '.format('  xi','yi ') 
	#print '     {0:6}   | {1:7} '.format(xi,yi)
	while xi < xf:
		s += 1
		yi = yi + h* d(xi,yi)
		xi = xi + h
		print 'cuenta:', s
		
		#print '     {0:6}   | {1:7} '.format(xi,yi) # para ir viendo el incremento
	error = y_manual - yi
	print '     {0:6}   | {1:.6f} | {2:6}'.format(h,yi,error)

print ''
print '     {0:6}   | {1:7} | {2:6}'.format('  h','f(0.25) ',"error")
#calcular(0.25)
#calcular(0.1)
#calcular(0.05)
calcular(0.01)
#calcular(0.005)
#calcular(0.0005)
#calcular(0.0000001)