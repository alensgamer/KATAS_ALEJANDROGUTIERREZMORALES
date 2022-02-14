#creacion de un diccionario
planet = {
    'name': 'Earth',
    'moons': 1
}

#manera de imprimir un objeto de un diccionario
print(planet.get('name'))#el .get invoca al objeto
# planet['name'] es idéntico a usar planet.get('name')
print(planet['name'])#xd tambien puedo usar corchetes para esto xd


planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'
# Usando update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Usando corchetes este tambien es update
planet['name'] = 'Jupiter'
planet['moons'] = 79


##Adicion y eliminacion de claves
planet['orbital period'] = 4333#asi agrego una una buena clave a un diccionario uwu

# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
planet.pop('orbital period')#ahora con esta madre pop lo borro alv

# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
# }

##tipos de data complejos
# Añadimos los datos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# el diccionario planet ahora contiene: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f'{planet['name']} polar diameter: {planet['diameter (km)']['polar']}')

# Salida: Jupiter polar diameter: 133709

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():#esta madre me da todo de putazo xd

    print(f'{key}: {rainfall[key]}cm')

# Salida:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

# El valor de december: 2.1cm

# Si, 'december' existe en rainfall
if 'december' in rainfall:
    # rainfall [en la posición december] es igual a
    # rainfall [en la posición december] + 1 (2.1+1)
    rainfall['december'] = rainfall['december'] + 1

# Si no:
else:

    # rainfall [en la posición december] es igual a 1
    rainfall['december'] = 1

# Como december si existe, el valor será 3.1

#Total de precipitaciones 0
total_rainfall = 0

# Para cada valor en los valores de rainfall
for value in rainfall.values():
    
    # El total de las precipitaciones será igual a ese mismo + el valor que se está iterando

    total_rainfall = total_rainfall + value

# Muestra 'Hay un total de precipitaciones (el valor total) en centímetros en el último cuarto (haciendo referencia al cuarto del año)

print(f'There was {total_rainfall}cm in the last quarter')

# Salida:
# There was 10.8cm in the last quarter

