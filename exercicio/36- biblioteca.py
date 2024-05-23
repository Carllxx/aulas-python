import os

def cabecalho():
    print("-=" * 18)
    print("SEJA BEM VINDO A BIBLIOTECA ONLINE!")

def main():
    os.system("cls || clear")
    cabecalho()
    # Primeira funcionalidade menu com os livros.
    menu = {
        1: ("Malala, a menina que queria ir para a escola", 25.60),
        2: ("A paciente silenciosa", 27.54),
        3: ("O menino do dedo verde", 39.80),  
        4: ("Desperte o seu gigante interior", 43.90),    
        5: ("O livro que você gostaria que seus pais tivessem lido", 31.92), 
        6: ("Até o verão terminar", 39.90),
        7: ("Diário estoico", 64.43),
        8: ("O milagre da manhã", 18.91),
        9: ("A arte de dar feedback (Um guia acima da média - HBR)", 24.89), 
        10: ("Pacote SpiceRack Book", 1000.21)
    }

    pedidos = []
    subtotal = 0.0
    while True:
        # Segunda funcionalidade memorizando os pedidos, valores e etc...
        print("\nMenu da Biblioteca: ")
        for codigo, (nome, preco) in menu.items():
            print(f"{codigo}: {nome} - R$ {preco:.2f}")
        try:
            codigo = int(input("\nDigite o código do livro desejado ou 0 para finalizar: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        if codigo == 0:
            break
        
        if codigo in menu:
            pedidos.append((codigo, menu[codigo][0], menu[codigo][1]))
            subtotal += menu[codigo][1]
            print(f"Você adicionou {menu[codigo][0]} ao seu pedido.")
        else:
            print("Código inválido, tente novamente.")
        # Terceira funcionalidade adicionar mais pedidos em vez de reiniciar o codigo.
        continuar = input("Deseja fazer mais um pedido? (s/n): ").lower()
        os.system("cls || clear")
        if continuar != 's':
            break

    if pedidos:
        print("\nResumo do Pedido: ")
        for codigo, nome, preco in pedidos:
           print(f"Código: {codigo}, Livro: {nome}, Preço: R${preco:.2f}")

        print(f"\nSubtotal: R${subtotal:.2f}")
        # Quarta funcionalidade forma de pagamento com  à vista ou credito afetando o pagamento.
        forma_pagamento = input("Digite a forma de pagamento ('vista' para à vista com desconto ou 'credito' para com cartão com acréscimo): ")
        if forma_pagamento == "vista":
            desconto_acrescimo = subtotal * 0.10
            total = subtotal - desconto_acrescimo
            print(f"Desconto: R${desconto_acrescimo:.2f}")
        elif forma_pagamento == "credito":
            desconto_acrescimo = subtotal * 0.10
            total = subtotal + desconto_acrescimo
            print(f"Acréscimo: R${desconto_acrescimo:.2f}")
        else:
            print("Forma de pagamento inválida. Calculando como pagar à vista")
            desconto_acrescimo = subtotal * 0.10
            total = subtotal - desconto_acrescimo
            forma_pagamento = 'vista'
            print(f"Desconto: R${desconto_acrescimo:.2f}")
        os.system("cls || clear")    
        print(f"Total a pagar: R${total:.2f}")
        print(f"Forma de pagamento escolhida: {forma_pagamento}")
        print(f"Obrigado pela compra, volte sempre!")
    else:
        print("Nenhum livro foi selecionado.")
            
if __name__ == "__main__":
    main()