salario = float(input("Salário atual: R$ "))

if salario <= 1500.00:
    pct, reajuste = 15, salario * 0.15
elif salario <= 3000.00:
    pct, reajuste = 10, salario * 0.10
else:
    pct, reajuste = 5, salario * 0.05

novo_salario = salario + reajuste
print(f"Percentual: {pct}%")
print(f"Aumento: R$ {reajuste:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")