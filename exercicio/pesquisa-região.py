import os
os.system ("clear")

idade : int
soma: float = 0
media = 0
contador = 0

while True:
    print = ("=== MENO ===")
    escolha = int(input("1. Adicionar\n2. Exibir Resultado\n3. Sair\nR= "))
    if escolha == 1:
        idade = int(input("Digite a sua idade: "))
        sexo = str(input("Informe seu sexo usando 'M' ou 'F': "))
        salario = float(input("Informe seu salário: "))
        contador += 1
        soma += salario
    elif escolha == 2:
        media = soma / contador
        print(f"Idade: {idade}")
        print(f"Sexo: {sexo}")
        print(f"Salário: {salario}")
        print(f"Média: {media}")
    elif escolha == 3:
        break
    else:
        print ("Invalida! ")    
