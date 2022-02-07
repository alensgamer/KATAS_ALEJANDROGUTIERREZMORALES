###Katas Modulo 4
##Ejercicio 1
text = """Interesting facts about the Moon. 
 The Moon is Earth's only satellite. 
 There are several interesting facts about the Moon and how it affects life here on Earth. 
 On average, the Moon moves 4cm away from the Earth every year. 
 This yearly drift is not significant enough to cause immediate effects on Earth. 
 The highest daylight temperature of the Moon is 127 C."""
text_parts = text.split('. ')#Lo que esta dentro de las comillas sera lo que las divida en la consola cuando salga

#cprint(text_parts)#tengo que poner print para que salga en la consola

key_words = ["average", "temperature", "distance"]#Se guarda en una cadena lo que voy abuscar
#Ciclo for(el cual no sale en el modulo) para buscar todas las palabras que se solicitan
for sentence in text_parts: 
    for key_word in key_words:
        if key_word in sentence:
            print(sentence)
            break
#for para cambiar C a celcius ptm no entiendo bien como funciona esta madre xd

for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break



##Ejercicio2
#Formateando Cadenas
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

# Creamos el título
title = f'datos de gravedad sobre {nombre}'
# Creamos la plantilla
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2"""
# Unión de ambas cadenas
template = f"""{title.title()} {hechos} """ 
print(hechos)
# Nuevos datos muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
# Comprobamos la plantilla
print(hechos)

new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))
# Pista: print(nueva_plantilla.format(variables))
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))#
#ok si entiendo el codigo
##pero la verdad me confundo a la hora de programarlo por mi mismo xd
