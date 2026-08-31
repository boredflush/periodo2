   
#x = 3
#x += 100000000000000000000
#n = 2


# atribuicao de valores + soma com valor ja atribuido a variavel


#print(x, " maior que", n)


#estrutura condicional simples

idade = 25
if (idade >= 16):
    print("ja ta podendo votar")

#estrutura composta - recebe duas alternativas

senha = "1020p"
if senha == "30":
    print("acesso permitido")
else:
    print("acesso negado")

#estrutura condicional encadeada - recebe mais de duas alternativas

#ex 1

nota = 7
if nota >= 7:
    print("aprovado")
elif nota >= 5:
    print("recuperacao")
elif nota == 0:
    print("caraca vei, zerou")
else:
    print("perdeu")

#ex 2 

idade = 16
carta_conducao = False

if idade >= 18 and carta_conducao==True:
    print("ja pode dirigir")
else:
    print("nao pode dirigir")

#condicional alinhada - if dentro do if 

idade = 25
tem_cnh = True

if idade >= 18:
    if tem_cnh:
        print("ja pode dirigir")
    else:
        print("nao pode dirigir, tire a cnh")
else:
    print("nao pode dirigir, ainda é menor de idade")

#xablalisson