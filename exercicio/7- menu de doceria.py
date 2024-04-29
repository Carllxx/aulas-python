import os
os.system("cls || clear")

contador = int(1);

def menu():
    print("Nº pedido | Pratos               | Valores")
    print("-=" * 30)
    print("1         | Bolo                 | R$ 30.00")
    print("2         | torta                | R$ 20.00")
    print("3         | cupcake              | R$ 5.40")
    print("4         | bombom               | R$ 5.50")
    print("5         | trufa                | R$ 5.00")
    print("6         | copo da felicidade   | R$ 15.00")
    print("7         | muosse               | R$ 18.00")
    print("0 | Para sair")
    opcao = int(input(f"Digite {contador}º número do pedido: "))
    
    return opcao;
    
opcao = menu()
preco = []
precoTotal = sum(preco)

def escolha (opcao):
    if(opcao == 1):
        print("1- Bolo             | R$ 30.00")
        preco.append(30.00)
    elif opcao == 2:
        print("2- torta            | R$ 20.00")
        preco.append(20.00)
    elif opcao == 3:
        print("3- cupcake          | R$ 5.40")
        preco.append(5.40)
    elif opcao == 4:
        print("4- bombom  | R$ 5.50")
        preco.append(5.50)
    elif opcao == 5:
        print("5- trufa            | R$ 5.00")
        preco.append(5.00)
    elif opcao == 6:
        print("6- copo da felicidade| R$ 15.00")
        preco.append(15.00)
    elif opcao == 7:
        print("7- muosse            | R$ 18.00")
        preco.append(18.00)
    elif opcao == 0:
        print("Saindo...")
        
while opcao != 0:
    desejaMaisUmPrato = str(input("Deseja fazer mais um pedido? ")).upper()
    
    if desejaMaisUmPrato == 'S':
        opcao = menu()
    else:
        break
