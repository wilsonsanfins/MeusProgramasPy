# Dada duas listas de números inteiros,
#calcule o produto de cada elemento das listas,
#onde cada posição i de uma lista é multiplicada pela posição i da outra lista.

lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
produto = [a * b for a, b in zip(lista1, lista2)]
print(produto)