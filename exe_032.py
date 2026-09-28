dias = {
    1: "SEGUNDA-FEIRA", 2: "TERÇA-FEIRA", 3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA", 5: "SEXTA-FEIRA", 6: "SÁBADO", 7: "DOMINGO"
}
opcao = int(input("Digite um número (1 a 7): "))
print(dias.get(opcao, "OPÇÃO INVÁLIDA"))