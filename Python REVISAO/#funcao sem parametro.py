#funcao sem parametro

def nome():
    return "otavio"

print (nome())

#funcao com parametro

#o nome da funcao é nome e o parametro (vulgo variavel local) é nomeCompleto

def nome(nomeCompleto):
    return nomeCompleto

nome1 = input("digite seu nome: ")
print(nome(nome1))