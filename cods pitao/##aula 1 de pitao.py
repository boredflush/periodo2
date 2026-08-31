##aula 1 de pitao

#vai tomando

aura = 67

nome = (input("Digite seu nome: "))##por padrao o input vem em txt!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#6767676767676767676767676767676767676

idade = int(input("Digite sua idade: "))

print("seu nome é:", nome)

print("sua idade é:", idade)

#!!!!!!!!!!!!!!!!!!!!!!!!!pitao e case sensitive

#!!!!!!!!!!!!!!!!!!!!!!!!!Print = 2

#!!!!!!!!!!!!!!!!!!!!!!!!!print("seu print é:", Print)

print ("sua aura é:", aura)



print(type(aura))#descobrir tipo do dado da variavel



from datetime import datetime #biblioteca

hoje = datetime.now() #pega data e hora atuais

print("Data e hora atuais:", datetime.now()) #pega data e hora atuais

print(f'data:{hoje:%d/%m/%Y}') #pega data e hora atuais organizados 00/00/0000

'''doc string bonitaooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo vai tomando0000000000000000000000000 
6767676767667766767676767676767676767676766776'''

print(1,2,3, sep=",") #vai separar os numeros com , e nao com espaço

print ('-'*5) #vai printar 5 traços

print(1,2,3, end="#") #vai printar 1,2,3 e no final vai colocar o # e nao pular linha
print("rathalos") #vai printar rathalos na mesma linha do print anterior