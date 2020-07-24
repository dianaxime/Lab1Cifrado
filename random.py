""" Grupo 3 - Laboratorio 1
Parte 1.b 
Codigo basado en: https://medium.com/asecuritysite-when-bob-met-alice/for-the-love-of-computing-the-lagged-fibonacci-generator-where-nature-meet-random-numbers-f9fb5bd6c237
"""
import array
import sys

print("************* THE LAGGED FIBONACCI GENERATOR *************\n")
j = int(input("Ingrese posicion 1: "))
k = int(input("Ingrese posicion 2: "))
modval = int(input("Ingrese el modulo a utilizar: "))
#val = "8675309"
val = input("Ingrese la seed: ")
cantidad = int(input("Ingrese la cantidad de numeros a generar: "))
valorfinal = []
def conv(val):
	arr = []
	for i in range(len(val)):
		arr.append(int(val[i]))
	return arr

def showvals(val,j,k):
	for i in range(len(val)):
		if (i==j-1):  
			print ("[%3d]"%val[i], end=" ")
		elif (i==k-1):  
			print ("[%3d]"%val[i], end=" ")
		else:
			print ("[%3d]"%val[i], end=" ")

s=conv(val)

print( "\nj=",j," k=",k)
print ("Seed:\t",val)

if (len(s)<k):
	print ("La seed tiene que ser mayor que ", k)
	exit()

showvals(s,j,k)

for n in range(cantidad):
    out = (s[j-1] + s[k-1]) % modval
    for i in range(len(s)-1):
    	s[i] = s[i+1] 
    s[len(s)-1] = out
    valorfinal.append(out)
             
    print ("-->",out)
    print("Ahora el resultado anterior (", out, ") se anexa al final de la seed y todos los items rotan hacia la izquierda\n")
    showvals(s,j,k)

print ("-->",out)
print("\nValor generado ", valorfinal)