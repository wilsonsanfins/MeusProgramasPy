# Solução
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        num = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

print("Elementos da diagonal principal:")
for i in range(4):
    print(matriz[i][i])
