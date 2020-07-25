'''
Cifrado de Información
Laboratorio #1
Grupo #3
Parte 2 - Linear Congruential Generators
'''

def sigEstado(sa, a, m, c):
    '''
    sa - Estado anterior
    a  - Multiplicador
    m  - Modulo
    c  - Incremento
    '''
    return ((a * sa) + c) % m

def incremento(san, sac, a, m):
    '''
    san - Estado anterior
    sac - Estado actual
    a  - Multiplicador
    m  - Modulo
    '''
    return ((sac - ((a * san) % m)) + m)

def multiplicador(a, b, m):
    '''
    a = s1 - s2
    b = s2 - s3
    m = modulo
    '''
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    while a > m:
        a -= m

    return (m * multiplicador(m, -b, a) + b) // a

opcion = 0

while opcion != 4:
    if opcion == 1:
        print("\nInciso A - Calcular el estado siguiente\n")
        sa = int(input("¿Cuál es el estado actual? "))
        a = int(input("¿Cuál es el multiplicador? "))
        m = int(input("¿Cuál es el módulo? "))
        c = int(input("¿Cuál es el incremento? "))
        ne = sigEstado(sa, a, m, c)
        print("\nEl estado siguiente es: ", ne)
    elif opcion == 2:
        print("\nInciso B - Calcular el incremento y el estado siguiente\n")
        san = int(input("¿Cuál es el estado anterior? "))
        sac = int(input("¿Cuál es el estado actual? "))
        a = int(input("¿Cuál es el multiplicador? "))
        m = int(input("¿Cuál es el módulo? "))
        c = incremento(san, sac, a, m)
        print("\nEl incremento es: ", c)
        ne = sigEstado(sac, a, m, c)
        print("\nEl estado siguiente es: ", ne)
    elif opcion == 3:
        print("\nInciso C - Calcular el multiplicador, incremento y estado siguiente\n")
        s1 = int(input("¿Cuál es el estado 1? "))
        s2 = int(input("¿Cuál es el estado 2? "))
        s3 = int(input("¿Cuál es el estado 3? "))
        m = int(input("¿Cuál es el módulo? "))
        a = s1 - s2
        b = s2 - s3
        mul = multiplicador(a, b, m)
        print("\nEl multiplicador es: ", mul)
        c = incremento(s2, s3, mul, m)
        print("\nEl incremento es: ", c)
        ne = sigEstado(s3, mul, m, c)
        print("\nEl estado siguiente es: ", ne)
    
    print("\n1. Inciso A - Calcular el estado siguiente \n2. Inciso B - Calcular el incremento y el estado siguiente \n3. Inciso C - Calcular el multiplicador, incremento y estado siguiente")
    opcion = int(input("Ingrese una opcion: "))