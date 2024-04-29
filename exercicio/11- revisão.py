import os

os.system("clear")

# Dinâmico
nome = input("Digite seu nome ")

#Estática
idade: int
idade = int (input("Digite sua idade: "))

#Exibindo dados do usuário...
print(f"Nome: {nome}")
print(f"Idade: {idade}")

if idade >= 65:
    print ("pode requerer a aposentadoria ")

else:
    print ("não pode requerer aposentadoria ")

