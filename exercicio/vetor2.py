import os

os.system ("cls || clear")

notas = []
soma  = 0
contador = 0

for i in range (5):
    nota = float (input(f"Digite a sua nota {i+1}: "))
    notas.append(nota)
    contador += 1

soma += notas [i]
media = soma / contador 

if media > 7:
    print ("Aprovado!! ")
elif media >= 5 < 7:
    print ("Aprovado!!")
else:
    print ("Reprovado!! ")
