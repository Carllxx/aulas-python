import os

#limpar o terminal.
s.system("cls|| clear")
o
#Solicitando dados para usuario...
nome= str(input("informe seu nome completo: "))
idade= int(input("Digite a sua idade: "))
peso= float(input("Digite seu peso: "))
telefone= int(input("Digite seu telefone: "))
dataN= int(input("Digite sua data de nascimento: "))
CPF= int(input("Infome seu CPF: "))

os.system("cls || clear")

#EXIBINDO DADOS INSERIDOS PELO USÚARIO.
print("\n===Exibindo Resultados ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
print(f"telefone: {telefone}")
print(f"Data de nascimento: {dataN}")
print(f"CPF: {CPF}")