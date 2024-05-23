import os
from dataclasses import dataclass

os.system("cls || clear")

#CRIANDO A CLASS + ATIVIDADE
@dataclass
class biblioteca:
    nome: str
    autor: str
    categoria: str
    preco: float
cjlivros= []

#GUARDANDO A CLASS NUMA VARIAVEL + ADD VALORES
for i in range (3):
    livro= biblioteca(
        nome = input("Digite o nome do livro: "),
        autor = input("Digite o nome do autor: "),
        categoria = input("Digite a gategoria: "),
        preco = float(input("Preço do livro: ")),
    )
    
    os.system ("cls||clear")

    #Guardando os dados em uma lista
    cjlivros.append(livro)

#criando arquivos externos
arquivo = "categoria_livro.txt"

#Realizando comandos de escritas em um arquivo

def salvar(livros):
    with open(arquivo,"w")as arquivoDeLivro:
        for livro in livros:
            arquivoDeLivro.write(f"{livro.nome}\n{livro.autor}\n{livro.categoria}\n{livro.preco}\n\n")
            print("Dados da biblioteca")
salvar(cjlivros)