import os
os.system("clear")

impares = 0
pares = 0
positivos = 0
negativos = 0
contador = 0

for i in range (1, 6):
    n = int(input(f"Informe o {i} º numero inteiro: "))
    contador += 1
    if n % 2 == 0:
        pares +=1
    else:
        impares +=1 
    if n >= 0:
        positivos += 1
    else:
        negativos += 1

print (f"Quantidade de pares: {pares}")
print (f"Quantidade de impares: {impares}")
print (f"Quantidade de negativos: {negativos}")
print (f"Quantidade de positivio: {positivos}")

