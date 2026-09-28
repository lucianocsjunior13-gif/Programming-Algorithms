a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b == c:
        print("Resultado: EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("Resultado: ISÓSCELES")
    else:
        print("Resultado: ESCALENO")
else:
    print("Resultado: NÃO FORMA TRIÂNGULO")