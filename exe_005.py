preco = float(input("Preço do produto: R$ "))
desconto = preco * 0.10
preco_final = preco - desconto
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")