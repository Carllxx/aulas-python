class Cliente: 
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

print("Solicitando dados para o usuário.")

Cliente1 = Cliente("Marta", 20)
Cliente2 = Cliente("Caio", 26)

print(f"Nome: {Cliente1.nome}")
print(f"Idade: {Cliente1.idade}")


print(f"Nome: {Cliente2.nome}")
print(f"Idade: {Cliente2.idade}")
