
##ejercicio1
plan= ""
array= []
while plan.lower() != "terminado":
    if plan:
        array.append(plan)
    plan=input("Agrega un planeta a la lista de planetas uwu(escribe 'terminado' cuando ya no quieras agregar mas):  ")

##ejercicio2
for num in array:
    print(num)
    

print("esos son todos los planetas en la base de datos")