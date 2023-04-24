x: int
y: int

x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))

while x != y:
    if x < y:
        print("Crescente!")
    else:
        print("Decrescente!")
    x = int(input("Informe o valor de x: "))
    y = int(input("Informe o valor de y: "))
