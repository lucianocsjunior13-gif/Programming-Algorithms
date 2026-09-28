idade = int(input("Idade: "))

if idade < 16:
    print("NÃO PODE VOTAR")
elif idade in (16, 17) or idade >= 70:
    print("VOTO OPCIONAL")
else:
    print("VOTO OBRIGATÓRIO")