# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Asignatura: Modelo y Simulacio
# Trabajo de Clase: 31-03-2014 
# Descripcion: Metodo de la biseccion
# Intereses
# formula =500*((1-(1+A9)^(-24))/A9) - 8500
# DATOS
capital = 8500
couta = 24
pago = 500
aproximacion = 0.01

def funcion_i(i):
	valor = pago*((1-(1+i)**(-couta))/i) - capital
	return valor

def main(ipos,ineg):	
	#calculo el promedio entre los dos interes
	ipromedio = (ipos+ineg)/2
	#llamo a la funcion que calcula cuanto vale la funcion en el promedio
	fpromedio = funcion_i(ipromedio)
	print '     {0:7} | {1:10}'.format('i prom','ValorFuncion')
	print '     {0:7} | {1:10}'.format('-------','------------')
	# Aproximar a 0
	while abs(fpromedio) > aproximacion :
		ipromedio = (ipos+ineg)/2
		fpromedio = funcion_i(ipromedio)	
		#Voy acotando el intervalo de busqueda
		if fpromedio < 0 :
			ineg = ipromedio
		else:
			ipos = ipromedio
		print '     {0:.5f} | {1:.2f}'.format(ipromedio,fpromedio)
	print ''
	# El interes final aproximado
	print 'interes=~ ', ipromedio 	

if __name__ == '__main__':
	# le doy a main los valores del intervalo de intereses para comenzar con el metodo
	main(0.01,0.3)

