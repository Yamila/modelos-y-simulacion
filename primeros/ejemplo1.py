#! /usr/local/bin/python
from math import *

# aceleracion = 9,81m/seg2
a = -9.81
# altura inicial
hi = float(raw_input('Ingrese Altura Inicial(metros): '))
# Velocidad Inicial
vi = float(raw_input('Ingrese Velocidad Inicial(m/seg) : '))
#Calculo la velocidad y la altura para cada instante de tiempo
t = 0
h=hi
print ''
print '{0:10} | {1:10} | {2:10}'.format('Tiempo','Velocidad','Altura')
print ''
while h >= 0:
	v = (a*t) + (vi)
	h = 0.5*a*(t**2) + vi*t + hi
	#print '%1.1f   %1.1f  %1.1f ' %(t,v,h)
	print '{0:10} | {1:10} | {2:10}'.format(t,v,h)
	t = t + 0.01
	


