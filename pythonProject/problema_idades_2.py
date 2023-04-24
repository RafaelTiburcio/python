N: int
N = int(input("Quantas pessoas serao cadastradas: "))
soma: int
media: float

nomes: [str] = [0 for x in range(N)]
idades: [int] = [0 for x in range(N)]

for i in range(0, N):
    print(f"DADOS DA {i + 1}a pessoa: ")
    nomes[i] = input("Nome: ")
    idades[i] = int(input("Idade: "))
print()

print("PESSOAS CADASTRADAS:")
for i in range(0, N):
    print(f"{nomes[i]}, ", end="")
    print(f"{idades[i]} anos")
print()

soma = 0
for i in range(0, N):
    soma = soma + idades[i]

media = soma / N
print(f"Media de idade: {media} anos.")