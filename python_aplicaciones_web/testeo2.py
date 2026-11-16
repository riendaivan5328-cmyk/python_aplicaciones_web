numero = int(input('Dame un numero:'))
numero2 = int(input('Dame otro numero:'))


if numero%numero2 == 0:
    print('El numero es divisible por ' + str(numero2))
elif numero%4 == 0:
    print('El numero es divisible por 4')
elif numero%2 == 0:
    print('El numero es par')
else:
    print('El numero no es par')

    #hola