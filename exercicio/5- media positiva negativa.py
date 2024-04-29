import os

os.system("clear")

media = 0
positivos = float
negativos = float
soma = 0
contador = 0
nota = 0

print ("\n=== MENU ===\n")  
print("Calcular média aritmética.. ")
while True:
    nota  = float(input("\nInforme sua nota Positiva: "))
    
    if nota >0:

        soma += nota
        contador += 1
        media = soma / contador

    if nota <0:
        break
     
print (f"\nResultado da operação= {media} ")
    
   

    

