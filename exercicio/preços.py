import os

os.system("clear")

notas = []

i = 0
soma = 0
media = 0
maiorValor = 0
menorValor = 999

print ("\n===EXIBINDO INFORMAÇÕES PARA O USUARIO===\n")
numero1 = int(input("Informe o primeiro inteiro: "))
numero2 = int(input("Informe o segundo inteiro: "))

media = (numero1 + numero2) / 2

soma = numero1 + numero2

produto = numero1 * numero2

menorValor = min(numero1, numero2)

maiorValor = max(numero1, numero2)

print("Média:", media)
print("Soma:", soma)
print("Produto:", produto)
print("Menor valor:", menorValor)
print("Maior valor:", maiorValor)


print("\n===FIM DA OPERAÇÃO===\n")
