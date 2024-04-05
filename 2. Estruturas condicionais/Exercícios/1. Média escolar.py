import os

os.system

nome= input ("Imforme seu nome: ")
idade= int (input("Digite sua idade: "))
nota1= float (input("Digite sua primeira nota: "))
nota2= float (input("Digite segunda nota: "))
nota3= float (input("Digite terceira nota: "))
nota4= float (input("Digite Quarta nota: "))
media= float

soma= nota1 + nota2 + nota3 + nota4 /4
media = soma /4

print ("\n=== MENU PRINCIPAL === \n")
print (f"Nome: {nome}")
print(f"idade: {idade}")
print (f"Primeira Nota: {nota1}")
print (f"Segunda Nota: {nota2}")
print (f"Terceira nota: {nota3}")
print (f"Quarta nota: {nota4}")
print (f"Média: {media}")

print("=== FIM ===")