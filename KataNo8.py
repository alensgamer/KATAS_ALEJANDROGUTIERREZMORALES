planeta = {
    'nombre':'marte',
    'lunas' : 42
}
print(planeta['nombre'])
print(planeta['lunas'])

planeta['polar']='6752'
planeta['equatorial']='6792'

print (planeta['nombre'] ,"tiene una circunferencia polar de ", planeta['polar'],"km")
