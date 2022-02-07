# Tip de práctica 1: Intenta ejecutarlo en un notebook.
a = 97
b = 55
# test expression / expresión de prueba
if a >= b:
    # statement to be run / instrucción a ejecutar
    print(b)
    
#Declaraciones else y elif
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

#Trabajando con elif
a = 93
b = 27
if a >= b:
    print("a es mayor o igual que b")
elif a == b:
    print("a es igual que b")

#Convinar declaraciones if, else, elif
a = 93
b = 27
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else: 
    print ("a es igual que b")
#Logica condicional anidada
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a es mayor que b y b es mayor que c")
    else: 
        print ("a es mayor que b y menor que c")
elif a == b:
    print ("a es igual que b")
else:
    print ("a es menor que b")
#Que son los operadores and y or
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

###Kata nomero 3
#problema1
asteroide = 49
if asteroide > 25:
    print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
else:
    print('¡Sigue con tu día!')

#Problema 2
asteroide = 19
if asteroide > 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif asteroide == 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
else:
    print('¡Nada que ver aquí!')

#Problema3
velocidad_asteroide = 25
tamano_asteroide = 40
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')