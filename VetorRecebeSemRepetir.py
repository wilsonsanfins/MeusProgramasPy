
vet1=[int(input("Digite um númeor: "))for _ in range(3)]
vet2=[int(input("Digite um númeor: "))for _ in range(3)]
vet3=[]
for num in vet1 + vet2:
    if num not in vet3:
        vet3.append(num)
print(f"O vetor inbuindo os 2 outros sem repetição ficou : {vet3}") 