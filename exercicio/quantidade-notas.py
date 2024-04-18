import os

os.system("clear")

nota : float = -1
soma : float = 0
quantidadeNotas = 0

while True :
   
    print("=== MENU ===")
    print("S - Inserir uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular média aritmética")
   
    resposta = input("Deseja inserir uma nota: ")
    

    if  resposta == "S":

        nota = float(input("\nDigite uma nota: "))
        soma += nota
        quantidadeNotas += 1

    elif resposta == "P":

        if quantidadeNotas == 0:
            print("Não foram inseridas notas. \n")

        else:
            print(f"Quantidade de notas inseridas: {quantidadeNotas} \n")
           
    elif resposta == "N":

        if quantidadeNotas == 0:
             
             print("Não foram inseridas notas. \n")
        else:

            break
        
    else:
        print("Opção inválida... \n")

media  = soma / quantidadeNotas

print(f"Média: {media}"