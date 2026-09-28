salario_fixo = float(input("Salário fixo: R$ "))
vendas = float(input("Total em vendas: R$ "))
comissao = vendas * 0.04
total = salario_fixo + comissao
print(f"Comissão (4%): R$ {comissao:.2f}")
print(f"Salário total: R$ {total:.2f}")