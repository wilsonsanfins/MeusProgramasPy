vetor= [int(input("Digite um número: "))for _ in range(10)]
count = 0
for num in vetor:
    if num > 10:
     count+=1
print("Quant de números maiores que 10: ",count)