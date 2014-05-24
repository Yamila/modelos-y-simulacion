#! /usr/local/bin/python
from math import *

# aceleracion = 9,81m/seg2
a = -9.81
# altura inicial
hi = 1
# Velocidad Inicial
vi = 0
#Calculo la velocidad y la altura para cada instante de tiempo
t = 0
h = hi
print ''
print '{0:10} | {1:10}'.format('Vel.Inicial','Tiempo')
print ''
while vi < 2:
	while h >= 0:
		v = (a*t) + (vi)
		h = 0.5*a*(t**2) + vi*t + hi
		#print '%1.1f   %1.1f  %1.1f ' %(t,v,h)
		#print '{0:10} | {1:10} | {2:10}'.format(t,v,h)
		t = t + 0.1

print '{0:10} | {1:10}'.format(vi,t)
vi = vi + 1	
