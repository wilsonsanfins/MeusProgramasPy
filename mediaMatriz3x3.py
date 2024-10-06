# Solução
matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(num)
        soma += num
    matriz.append(linha)

media = soma / 9
print("A média dos elementos da matriz é:", media)
