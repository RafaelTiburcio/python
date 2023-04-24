M: int
N: int
cont: int

M = int(input("Quantas linhas vai ter a matriz? "))
N = int(input("Quantas colunas vai ter a matriz? "))

mat: [[int]] = [[0 for x in range(M)] for x in range(N)]

for i in range(M):
    for j in range(N):
        mat[i][j] = int(input(f"ELEMENTO [{i}, {j}]: "))

print()
print("DIAGONAL PRINCIPAL: ")

for i in range(M):
        print(f"{mat[i][i]}  ", end="")

print()
print("QUANTIDADE DE NEGATIVOS: ", end="")

cont = 0
for i in range(M):
    for j in range(N):
        if mat[i][j] < 0:
            cont = cont + 1
print(cont)



