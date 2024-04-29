import os
os.system("clear")

impares = 0
pares = 0
positivos = 0
negativos = 0
contador = 0
n = int (input (f"Informe o {contador +1}º numero inteiro: "))
contador += 1
while n != 0:
    n = int(input(f"Informe o {contador +1}º numero inteiro: "))

    if n < 0 or n > 0:
        contador += 1
    if n > 0:
        positivos += 1
    if n < 0:
        negativos +=1
    if n % 2 != 0:
        pares += 1      
    if n % 2 !=0:
        impares += 1

print (f"Quantidade de pares: {pares}")
print (f"Quantidade de impares: {impares}")
print (f"Quantidade de negativos: {negativos}")
print (f"Quantidade de positivio: {positivos}")
print (f"Quantidade de numeros inseridos: {contador}")
