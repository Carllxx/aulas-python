def calcular_inss(salario_base):
    faixas = [(1100, 0.075), (2203.48, 0.09), (3305.22, 0.12), (6433.57, 0.14)]
    max_desconto = 854.36
    for faixa, taxa in faixas:
        if salario_base <= faixa:
            return min(salario_base * taxa, max_desconto)
    return max_desconto

def calcular_irrf(salario_base, dependentes):
    faixas = [(2259.20, 0, 0), (2826.65, 0.075, 142.80), (3751.05, 0.15, 354.80),
              (4664.68, 0.225, 636.13), (float('inf'), 0.275, 869.36)]
    deducao_dependente = 189.59 * dependentes
    salario_com_desconto_inss = salario_base - calcular_inss(salario_base)
    for faixa, taxa, deducao in faixas:
        if salario_com_desconto_inss <= faixa:
            return max(0, (salario_com_desconto_inss * taxa) - deducao_dependente - deducao)
    return 0

def desconto_vale_transporte(salario_base):
    return salario_base * 0.06

def desconto_vale_refeicao(valor_vale_refeicao):
    return valor_vale_refeicao * 0.2

def desconto_plano_saude():
    return 150.00

def calcular_salario_liquido(matricula, senha, salario_base, vale_transporte, valor_vale_refeicao):
    # Verificar matrícula e senha (não implementado nesta versão)
    dependentes = 1  # Supondo apenas um dependente
    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base, dependentes)
    desconto_vt = desconto_vale_transporte(salario_base) if vale_transporte == 's' else 0
    desconto_vr = desconto_vale_refeicao(valor_vale_refeicao)
    desconto_saude = desconto_plano_saude()

    salario_liquido = salario_base - desconto_inss - desconto_irrf - desconto_vt - desconto_vr - desconto_saude

    return salario_liquido

def main():
    matricula = input("Digite a matrícula do funcionário: ")
    senha = input("Digite a senha: ")  # Não implementado nesta versão
    salario_base = float(input("Digite o salário base do funcionário: "))
    vale_transporte = input("O funcionário deseja receber vale transporte? (s/n): ")
    valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa: "))

    salario_liquido = calcular_salario_liquido(matricula, senha, salario_base, vale_transporte, valor_vale_refeicao)

    print(f"O salário líquido do funcionário é: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()