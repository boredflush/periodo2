#1

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a + b > c:
    print("a + b e maior que c")
elif a + b == c:
     print("a + b e igual a c")
else:
    print("a + b nao e maior que c")

#2 

cnh = True
cpf = True

if cnh == True and cpf == True:
    print("tudo em ordem")
elif cnh == True and cpf == False:
    print("cnh ok, cpf nao")

elif cnh == False and cpf == True:
    print("cnh nao, cpf ok")
else:
    print("ta tudo errado")

#3



altura = float(input("Digite sua altura em cm: "))

peso = float(input("Digite seu peso em kg: "))

imc = peso / (altura / 100) ** 2

print("Seu IMC é :", f"{imc}")

if imc < 18.5:
    print("ta maguinho vei, vamo se alimentar")
elif imc >= 18.5 and imc < 25:
        print("Peso normal")
elif imc >= 25 and imc < 30:
        print("Sobrepeso")
elif imc >= 30:
        print("tais obeso vamo se cuidar")
#4

lapis = input("Digite a cor do lapis: ")
while lapis != "azul":
    print("errrrrrouuuuuu")
    
    lapis = input("Digite a cor do lapis: ")
print("boaa cabroonco, acertou a cor do lapis")


    