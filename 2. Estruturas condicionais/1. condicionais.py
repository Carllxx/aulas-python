import os 
os.system("cls || clear")

Idade : int 

Idade= int (input("Informe sua idade: "))

if Idade < 18 or Idade >= 65:
    print ("Não pode votar. ")

else:
    print ("Pode votar")    


print ("=== FIM ===")