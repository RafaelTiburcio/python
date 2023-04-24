a: int
b: int
c: int

a = int(input("Informe um numero: "))
b = int(input("Informe mais um numero: "))
c = int(input("Informe mais um numero "))

if a < b and a < c:
    print(f"MENOR VALOR = {a}")
elif b < c:
    print(f"MENOR VALOR = {b}")
else:
    print(f"MENOR VALOR = {c}")