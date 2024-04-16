import os

os.system("clear")
soma = 0

for i  in range (3):
    notas = float(input(f"digite a {i+1}ª nota: "))

    while (notas < 0 or notas > 10):
        print ("Informe uma nota valida entre 0 e 10. ")
        notas = float(input(f"Digite a {i+1}ªnota: "))
    
    soma += notas

media = soma / 3

print(f"Média: {media:.1f}")
if media > 7:
    print("Aprovado! ")
elif media > 5 or media > 9:
    print ("Recuperação! ")
else:
    print ("Reprovado! ")
