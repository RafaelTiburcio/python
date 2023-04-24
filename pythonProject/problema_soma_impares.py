x: int
y: int
soma: int
troca: int

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

soma = 0
while x != y:
    if x > y:
        troca = x
        x = y
        y = troca
    for i in range(x+1, y):
        if i % 2 != 0:
            soma = soma + i
    print("SOMA DOS IMPARES = ", soma)
    soma = 0
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

