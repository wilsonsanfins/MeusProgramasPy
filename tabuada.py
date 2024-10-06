n=int(input(("Entre com um numero : ")))
t=int(input(("Entre com um numero da tabuada : ")))
print(f"Tabuada de {n} até {t}:")
for i in range(0, t+1):
    r = n * i
    print(f"{n} x {i} = {r}")