# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
from reloj import *
import os

sincronizar = 1999000

#Usando Reloj por consola	
x = inicializar()
r = Reloj(x[0],x[1],x[2])
os.system ("clear")
r.mostrar()
while True:
	for x in range(1, sincronizar):
		a = 1
	r.avanzar()
	os.system ("clear")
	r.mostrar()

