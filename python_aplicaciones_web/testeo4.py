lista1=[1,2,3,4,5,6]
lista2=[1,4,8,2,6,9,10]

for numero in lista1:
    for numero2 in lista2:
        if numero == numero2:
            print('el numero ' + str(numero) + ' esta en ambas listas')