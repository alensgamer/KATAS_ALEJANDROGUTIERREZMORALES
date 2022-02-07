###Modulo 4

#Inmutabilidad de las cadenas
from turtle import heading, title


fact = 'The Moon has no atmosphere.'
fact + 'No sound can be heard on the Moon.'
print(fact)
#pero para agregar un valor puedo hacer esto
who_fact=fact+"No sound can be heard on the moon"
print(who_fact)
#/n es para dar un salto de linea o un enter para que lo entiendas mejor xd

#Metodos de string en python
'temperatures and facts about the moon'.title()

heading="temperatures and facts about the moon"
heading.title()

#Dividir una cadena
#.split() esta madre separa la cadena en cada espacio
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
temperatures .split()
temperatures .split('\n')



#Buscar una cadena
#Metodo in
"moon" in "this text will describe facts and challenges whit espace travel"

"moon" in "this text will describe facts about the moon"
#Metodo .find
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
temperatures.find('Moon')
temperatures.find('Mars')
#El método .find() devuelve -1 un cuando no se encuentra la palabra o devuelve el índice (el número que representa el lugar en la cadena).

#Metodo .count
temperatures.count('Mars')

#Metodo lower
#el metodo lower no hace distincion entre letras mayusculas y minusculas
"The Moon And The Earth".lower()
#Y el metodo al contrario osea mayusculas funciona con el metodo .upper
'The Moon And The Earth'.upper()

##Transformar texto
#puedes utilizar el metodo .replace para buscar y remplazar apariciones de un caracter o un grupo de caracteres
'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C')
text = 'Temperatures on the Moon can vary wildly.'
'temperatures' in text
'temperatures' in text.lower()
#con el metodo split puedes separar cadenas pero con el metodo .join puedes volver a unirlos
moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']
'\n'.join(moon_facts)

##Formatos de cadenas en python
#Formato con signo porcentaje
mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)
#Metodo .format utiliza llaves para remplazar el texto 
mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

##Formatos de las codenas con f
print(f'On the Moon, you would weigh about {mass_percentage} of your weight on Earth')





