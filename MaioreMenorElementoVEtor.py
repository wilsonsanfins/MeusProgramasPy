vetor=[int(input("Digite um número"))for _ in range (10)]
maior=vetor[0]
menor=vetor[0]

for num in vetor:
    if num>maior:
        maior=num
    if num<menor:
        menor=num
print(f"O maior númeor é : {maior}")
print(f"O menor número é: {menor}")