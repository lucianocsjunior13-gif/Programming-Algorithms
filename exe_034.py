idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").strip().upper()

if idade < 12 or estudante == "SIM" or idade >= 60:
    valor = 15.00
else:
    valor = 30.00

print(f"Valor do ingresso: R$ {valor:.2f}")