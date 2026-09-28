valor = float(input("Valor original da prestação: R$ "))
taxa = float(input("Taxa de juros (% por período): "))
tempo = int(input("Tempo de atraso (períodos): "))

prestacao = valor + (valor * (taxa / 100) * tempo)
print(f"Valor da prestação com juros: R$ {prestacao:.2f}")