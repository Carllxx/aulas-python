import os

def tabuada(numeros):
     os.system("cls || clear")
     print("=== Tabuada (numeros)===")
     for i in range (1, 11):
          print(f"{numeros}+{i} = {numeros * i} ")

numero = int(input(f"Digite um numero: "))
tabuada (numero)
