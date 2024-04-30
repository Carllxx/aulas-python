import os

def porcentagem (produto):

    if produto < 100:
        return produto + (produto * (10/100))
    return produto - (produto * (10/100))

os.system ("cls||clear")
preco = int (input("Digite um valor: "))

final = porcentagem (preco)


print (final)
