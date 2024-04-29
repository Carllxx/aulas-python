import os

os.system("clear")

soma = 0
contador = 0
while True:
    nota = float(input("Digite uma nota positva: "))
    if nota >= 0:
        soma += nota
        contador += 1
    if nota < 0:
        break
print ("Calculando... ")
media = soma / contador

os.system("clear")
print(f"Média Geral: {media}")
