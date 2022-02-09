###Modulo6
##Crear una lista

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']#las listas se guardan en corchetes
print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])
planets[3] = 'Red Planet'#cambiamos el valor de ese numero por otro
print('Mars is also known as', planets[3])


number_of_planets = len(planets)#len es para saber cuantos espacios utiliza la lista
number_of_planets= str(number_of_planets)
print('There are', number_of_planets, 'planets in the solar system.')

planets.append('Pluto')#append es para agregar valores a una lista ya existente
number_of_planets = len(planets)
number_of_planets= str(number_of_planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

planets.pop()  # Goodbye, Pluto, pop es para eliminar elementos existentes 
#aunque no se porque no puedo poner nada entre los parentecis, me da error
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

print('The last planet is', planets[-1])#El numero negativo regresa los valores de regreso
print('The penultimate planet is', planets[-2])

jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')#index busca cosas en las listas


gravity_on_earth = 1.0#variables tipo float
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]#Gravedad de los planetas

bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')#formula para calcular el peso de un camion de 2 pisos

bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('The lightest a bus would be in the solar system is', bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is', bus_weight * max(gravity_on_planets), 'kg')#min devuelve el numero mas pequeño de la lista y max devuelve el numero mas grande de la lista

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]
print(planets_before_earth)#esos son los planetas que estan antes de la tierra

planets_after_earth = planets[3:8]
print(planets_after_earth) #esos son los planetas despues de la tierra

planets_after_earth = planets[3:]
print(planets_after_earth)#si no pones segundo numero python define que quieres hecerlo hasta el final de la lista

#Un slice crea una nueva lista. No modifica la lista actual.


amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons#asi unes listas y creas una nueva
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)#usas dort pra arreglar los elementos de las listas alfabeticamente

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)#ahora utilicamos reverse true para hacerlo en reversa




