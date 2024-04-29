import os
os.system

numero = int(input("Digite um número para a tabuada: "))

for i in range(1,11):
    print(f"{numero} * {i} = {numero * int(i)}")



