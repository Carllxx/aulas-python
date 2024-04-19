import os
os.system

valores = []
soma = 0


for i in range (5):
    valor = float (input(f"Insira {i+1} número: "))
    valores.append(valor)  
    if valor < 0:
        valores [i] = 0


for i in range (len(valores)):
    print(f"valor: {valores [i]}")
