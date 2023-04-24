import math

base: float
altura: float
area: float
perimetro: float
diagonal: float

base = float(input("Qual a base do retangulo? "))
altura = float(input("Qual a altura do retangulo? "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"Area do retangulo: {area:.4f}")
print(f"Perimetro do retangulo: {perimetro:.4f}")
print(f"Diagonal do retangulo: {diagonal:.4f}")