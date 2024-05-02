import os
os.system

def calcular_imc(peso, altura):
  
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
  
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau 1"
    elif 35 <= imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def main():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    interpretacao = interpretar_imc(imc)

    print(f"Seu IMC é {imc:.2f}, o que indica que você está {interpretacao}.")

if __name__ == "__main__":
    main()