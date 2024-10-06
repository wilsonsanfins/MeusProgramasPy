vet=map(int,input("Digite 6 numeros:").split())

vetImpar=[]
vetPar=[]
for num in vet:
    if num%2 ==0:
        vetPar.append(num)
    else:
        vetImpar.append(num)
print(f"Os números pares são : {vetPar}")
print(f"Os números impares são: {vetImpar}")
        