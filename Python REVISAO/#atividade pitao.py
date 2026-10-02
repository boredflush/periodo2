#atividade pitao

import random

print("sorteio de um número bacana de 1 a 10")

def sorteio(numeroBacana):
    return numeroBacana

numeroAdivinhado = int(input("digite numero de 0 a 10 plz:"))

while numeroAdivinhado != sorteio(random.randint(1,10)):
    print("numero errado, bora mais uma vez:")
    numeroAdivinhado = int(input("digite numero de 0 a 10 plz:"))

print("numero certo, parabens!")