# -*- coding: utf-8 -*-
#! /usr/local/bin/python2.7
# Asignatura: Modelo y Simulacio
# Trabajo de Clase: 07-Abril-2014
# Trabajo con Acciones de la pagina http://www.invertironline.com
#Fecha,Apertura,Maximo,Minimo,Cierre,CantNominal
#2014-04-07 16:41:27,2.44,2.44,2.40,2.43,1468773.00
# Se debe invertir 1000
inversion = 1000
#archivo = 'CotizacionesHisto'
archivo = 'APBR'

def cargardatos(a):
    archi=open(a,'r')
    linea=archi.readline() #descarto el primero
    linea=archi.readline()
    lista = []
    while linea!="":
        datos = linea.split(',')
    	fecha = datos[0].split(' ')
        lista.append([fecha[0],datos[4]])
        linea=archi.readline()	        
    archi.close()
    return lista

# [fecha,cierre]
def invertirlista(lista):
    lista.reverse()
    for i in lista:
        print i

def cada_quince(datos):
    cant = 1
    registro = datos[0]
    fecha = registro[0].split('-')    
    mes_actual = fecha[1]
    total_acciones = inversion/float(registro[1])
    dia = 1
    for i in datos:
        cierre = float(i[1])
        dia = dia + 1
        if dia == 15:
            dia = 1
            cant = cant + 1
            total_acciones = total_acciones + (inversion/cierre)
        fecha_hoy = i[0]
        cierre_hoy = float(i[1]) 
    invertido = cant*inversion
    pesos_hoy = total_acciones*cierre_hoy
    print '{0:10} | {1:4} | {2:.3f} | {3:.2f} | {4:.2f} | {5:.2f}'.format(fecha_hoy,cant,invertido,total_acciones,pesos_hoy,pesos_hoy-invertido)
# acciones recibe la lista de datos y el intervado de cada cuantos meses se realiza la inversion
def acciones_meses(datos,intervalo):
    cant = 1
    #los primeros valores
    registro = datos[0]
    fecha = registro[0].split('-')    
    mes_actual = fecha[1]
    total_acciones = inversion/float(registro[1])
    cont = 0
    for i in datos:
        fecha = i[0].split('-')    
        mes = fecha[1]
        cierre = float(i[1])
        if mes != mes_actual:
            mes_actual = mes
            cont = cont + 1
            if cont==intervalo:            
                cont = 0
                cant = cant + 1
                total_acciones = total_acciones + (inversion/cierre)
        #Los datos de la ultima fecha
        fecha_hoy = i[0]
        cierre_hoy = float(i[1]) 
    invertido = cant*inversion
    pesos_hoy = total_acciones*cierre_hoy
    print '{0:10} | {1:4} | {2:.3f} | {3:.2f} | {4:.2f} | {5:.2f}'.format(fecha_hoy,cant,invertido,total_acciones,pesos_hoy,pesos_hoy-invertido)

#Bloque Principal
datos = cargardatos(archivo)
datos.reverse()
print '{0:10} | {1:4} | {2:9} | {3:8} | {4:8} | {5:8}'.format('Fecha','Cant','Invertido','Acciones','Total $','Ganancia')
cada_quince(datos)
acciones_meses(datos,1) # Cada un mes
acciones_meses(datos,2) # Cada dos meses