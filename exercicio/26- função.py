import os

#função sem retorno.
def media ():
    os.system("cls|| clear")
    print("=== media ===")

#função sem retorno.
def somar(n1,n2):
    resultado = (n1+n2) / 2
    return resultado

#solicitando dados para o usuario...
media ()
primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int (input("Digite o segundo numero: "))

soma = somar(primeiroNumero , segundoNumero)

#Exibindo dados para usuário.
print(f"somar: {soma}")