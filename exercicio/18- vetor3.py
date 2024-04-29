import os
os.system

notas = []
soma = 0
contador = 0
QuantidadeNegativo= 0

for i in range (10):
    nota = float (input(f"Deseja inserir uma nota {i+1}: ")) 
    notas.append(nota)  
    contador += 1
    if nota < 0: 
        QuantidadeNegativo += 1 
    if nota >= 0:
        soma += nota
    
print (f"Soma positiva: {soma}")
print (f"quantidade de numeros negativos: {QuantidadeNegativo}")

 
