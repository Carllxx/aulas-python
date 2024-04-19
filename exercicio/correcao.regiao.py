import os

os.system ("clear")
 
notas = []

for i in range (3):
    nota = float (input(f"Digite a nota {i+1}: "))
    notas.append(nota)

for i in range (len (notas)):
  print(f"{i+1}ª nota: {notas [i]}")