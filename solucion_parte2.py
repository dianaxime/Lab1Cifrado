'''
Laboraorio 1 Cifrado de Informacion 
Grupo #3
Parte 2 Inciso A,B,C
Las funciones utilizan como parametros los datos ingresados por el 
usuario.
'''
def generador_de_estados(modulo, incremento, multiplicador,estado_anterior):
	state = (estado_anterior * multiplicador +incremento) % modulo
	return state

from sympy import mod_inverse

def calculador_incremento(modulo, multiplicador,estado_anterior, estado_actual):
	algo= multiplicador*estado_anterior
	algo2= (algo)%modulo
	algo3=estado_actual-algo2
	incremento= modulo+algo3
	return incremento

def calculador_multiplicador(modulo, estado1, estado2, estado3):
	alguito = estado2 - estado3 
	print(alguito)
	alguito = (estado1- estado2)

modulo =int(input('ingrese modulo: '))
s1 = int(input('ingrese el estado 1: '))
s2 = int(input('ingrese el estado 2: '))
s3 = int(input('ingrese el estado 3: '))

print()
#incremento = calculador_incremento(modulo, multiplicador,estado_anterior, estado_actual)
#generador_est= generador_de_estados(modulo,incremento,multiplicador,estado_actual)
calcular_multi = calculador_multiplicador(modulo,s1,s2,s3)
#print('El nuevo estado:',generador_est)