#simples

numero = 10
if (numero == 10):
    print("numero é 10!")

#composta

numero = 10
if (numero == 10):
    print("numero é 10!")
else:
    print("o numero nao é 10!")


#encadeada

numero = 10 
if (numero == 10):
    print("numero é 10!")
elif (numero > 10):
    print("numero é maior que 10!")
elif(numero == 0 ):
    print("numero é 0!")
else:
    print("o numero é menor que 10!")

#alinhada if dentro do if

numero = 10
if (numero >= 10):
    print("é 10")
    if (numero == 10):
        print("e é igual a 10")
    elif(numero > 10):
        print("e é maior que 10")
else:
    print("menor que 10")