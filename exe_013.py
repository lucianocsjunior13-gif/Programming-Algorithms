preco_unitario = float(input("Preço unitário do produto: R$ "))
quantidade = int(input("Quantidade comprada: "))
frete = float(input("Valor do frete: R$ "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Custo total final: R$ {total:.2f}")