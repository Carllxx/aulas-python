import os
from dataclasses import dataclass

os.system("cls|clear")

@dataclass
class informacoes:
    nome: str
    dataDeNascimento: str
    RG: float
    CPF: float

#criando arquivos externos
arquivo = "categoria_dados.txt"

#Realizando comandos de escritas em um arquivo
def salvar(dados):
    with open(arquivo,"w")as arquivoDeDados:
        for informacao in dados:
            arquivoDeDados.write(f"{informacao.nome}\n{informacao.dataDeNascimento}\n{informacao.RG}\n{informacao.CPF}\n\n")
            print("Dados das informações")

Informacao= []

#GUARDANDO A CLASS NUMA VARIAVEL + ADD VALORES
for i in range (5):
    dados= informacoes (
        nome = input("Informe seu nome: "),
        dataDeNascimento= input("Informe seu nome de nascimento: "),
        RG = input("Informe seu RG: "),
        CPF = input("Informe seu CPF: "), 
    )

    os.system("cls||clear")

 #Guardando os dados em uma lista
    Informacao.append(dados)


salvar(Informacao)