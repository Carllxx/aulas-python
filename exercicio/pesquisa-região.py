import os
os.system ("clear")

idade = int
sexo = str
escolha = str
salario = float
soma = 0
media = 0

while True:
    print = ("=== MENO ===")
    escolha = input ("1. Adicionar \n2. Exibir Resultado\n3. Sair\n" R= ")
if escolha == '1':
    idade = int (input ("Digite a sua idade: "))
    sexo = str (input ("Informe seu sexo usando 'M' ou 'F': "))
    salario = float (input ("Informe seu salário: "))
    contador += 1
elif escolha == '2':
    soma += salário
    media = soma / salario
    print (f"Idade : {idade}")
    print (f"Sexo : {sexo}")
    print (f"Salário : {salario}")
    print (f"Média : {media}")
elif escolha == '3':
    break
else:
print ("Invalida! ")    
