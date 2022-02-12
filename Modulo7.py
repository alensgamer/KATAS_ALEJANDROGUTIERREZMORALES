'''user_input = ''#variable vacia para que pueda asignarle el valor que quiera

while user_input.lower() != 'done':#hasta que el valor que asignemos en el imput sea done se seguira ejecutando
    #recuerda que el .lower es para que los valores se transformen en valores de caracter minusculo
    user_input = input('Enter a new value, or done when done')#pide la variable
'''



'''
user_input = ''
inputs = []#se crea un array

# Ciclo while
while user_input.lower() != 'done':
    # Verificamos si hay un valor en user_input
    if user_input:
        # Almacenamos ese valor en la lista
        inputs.append(user_input)
    # Capturamos un nuevo valor
    user_input = input('Enter a new value, or done when done')

print(inputs)
#yo lo habria hecho de otra forma creo
'''
'''
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])
'''
'''
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")
'''
# De la biblioteca time, importamos (traemos) la clase sleep

from time import sleep

# Creamos una lista de 5 números llamada countdown
countdown = [4, 3, 2, 1, 0]

# Para cada número en countdown
for number in countdown:
    #Muestra el número
    print(number)

    # Espera (1segundo)
    sleep(1)

# Muestra el mensaje Blast off
print("Blast off!! 🚀")