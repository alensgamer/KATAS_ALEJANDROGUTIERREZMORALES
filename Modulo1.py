#print('Hola Mundo uwu')
##Operadores
sum=1+2 

producto = sum*2

#print( producto )
#descubrimos que es una variable con type
type(sum)


##Fechas
from datetime import date

date.today()
print(date.today())

##Convercion de tipos de datos
date.today()
print('la Fecha de hoy es: '+ str(date.today()))#el srt convierte a la fecha en cadena

##Entrada al usuario
print('Bienvenido al programa de Hola Mundo')
nom=input('introduzca su nombre pls')
print('saludos y hola mundo        '+nom)

##Trabajar con numeros
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))