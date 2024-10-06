vetor=map(int,input("Digite seu número: ").split())
pares=0
impares=0

for num in vetor:
    if num %2 ==0:
       pares+=1
    else:
        impares+=1
print(f"Qauntidade de numeros pares: {pares}")
print(f"Quantidade de números : {impares}")