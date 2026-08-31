nome = (input("Digite seu nome: "))

altura = (input("Digite sua altura: "))

peso = (input("Digite seu peso: "))

imc = float(peso) / (float(altura) ** 2)

print ("olá", nome, "sua altura é:", altura, "e seu peso é:", peso)

print("Seu IMC é :", f"{imc:.2f}")