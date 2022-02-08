#kata No.5
#Ejercicio No.1
#Comenzaremos usando dos distancias de planetas: Tierra (149.597.870 km) y Júpiter (778.547.200 km).
from dis import dis
from queue import PriorityQueue


dtierra=149597870
djupiter=778547200
M=0.621
D1=(dtierra-djupiter)

D1=abs(D1)
Dm1=(D1*M)

print("La distancia en Kilometros es: "+ str(D1))
print("La distancia en millas es: "+str(Dm1))

#Ejercicio 2
#convierte cadenas en números y usa valores absolutos
Dis1=input("Dame la distancia del sol al primer planeta")
Dis1=int(Dis1)
Dis1=abs(Dis1)
Dis2=input("Dame la distancia del sol al segundo planeta")
Dis2=int(Dis2)
Dis2=abs(Dis2)
dis=(Dis1-Dis2)
dis=abs(dis)
dism=(dis*0.621)

print("La distancia de los planetas en kilometros es: "+dis)
print("La distancia de los planetas en Millas es: "+dism)

