# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Asignatura: Modelo y Simulacio
# Trabajo de Clase: 07-Abril-2014
# Metodo de newton- rapshon
# El método de Newton (conocido también como el método de Newton-Raphson o el método
# de Newton-Fourier) es un algoritmo eficiente para encontrar aproximaciones de 
# los ceros o raíces de una función real. También puede ser usado para encontrar el 
# máximo o mínimo de una función, encontrando los ceros de su primera derivada.
# calcula por ejemplo cuando es 0.5*x^2 - 3 = 0 ... la raiz cuadrada de 6

# Funcion f(x)= 0.5x**2 -3
def f(x):
	funcion = (0.5*(x**2)) -3
	return funcion
# Derivada de la f(x) --> x 
def d(x):
	derivada = x 
	return derivada

def main():
	# Para una buena aproximacion al valor real x0=100 y epsilon= 0.0001S
	x0 = float(raw_input("Ingrese el valor del punto X0: "))
	epsilon =  float(raw_input("ingrese la epsilon: "))
	x = x0
	print '     {0:6}   | {1:10}'.format('X','funcion')
	# Mientras la funcion calculada en x sea mayor que la aproximacion dada, seguir avanzando
	while( f(x) > epsilon ):
		print '    {0:.4f}   | {1:.4f}'.format(x,f(x))
		# Calculo en nuevo X mediante el metodo de newton-raphson
		# X(i+1) = X(i) - Funcion(Xi)/ FuncionDerivada(Xi)
		x = x - (f(x)/d(x))
	print 'valor de la funcion: ' ,f(x)
	print 'valor de x cuando la funcion tiende a 0: ' , abs(x)

if __name__ == '__main__':
	main()