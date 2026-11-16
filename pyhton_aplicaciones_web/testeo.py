edad = int(input('Que edad tienes?'))
nombre = input('Cual es tu nombre?')

if edad > 0 and edad < 100:
    print('Hola ' + nombre + ', en ' + str(2026 + 100 - int(edad)) + ' cumpliras 100 años.')
elif edad > 100:
    print('Hola ' + nombre + ', ya has cumplido 100 años.')
else:
    print('Ni has nacido aun, no puedes tener edad negativa.')