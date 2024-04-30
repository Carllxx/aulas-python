import os

#função sem retorno.
def logoDoceria ():
    os.system("cls || clear")
    print("=== Doceria ===")

#função sem retorno.
def somar(n1,n2):
    resultado = n1 + n2
    return resultado

#solicitando dados para usuario...
logoDoceria()
primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int (input("Digite o segundo numero: "))

soma = somar(primeiroNumero , segundoNumero)

#Exibindo dados para usuário.
print(f"somar: {soma}")