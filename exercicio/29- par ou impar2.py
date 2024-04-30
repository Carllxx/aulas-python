import os
os.system("clear")
     
def verificar (num):
    if num % 2 == 0:
        resultado = "par"
        return resultado
    else:
        resultado = "impar"
        return resultado

numero = int (input("Digite um numero: "))

total = verificar (numero)

os.system ("cls || clear")
print (total)