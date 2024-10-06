vetor=[int(input("Digite um númeor: "))for _ in range(15)]
vetor_unicos = []
for num in vetor:
    if num not in vetor_unicos:
        vetor_unicos.append(num)
        
print("Vetor sem repetidos: ",vetor_unicos) 