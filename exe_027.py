a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("Resultado: FORMAM UM TRIÂNGULO")
else:
    print("Resultado: NÃO FORMAM")