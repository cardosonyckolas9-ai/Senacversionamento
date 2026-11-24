a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))

valores = sorted([a,b,c])

print(f"menor valor: {valores[0]}")
print(f"valor do meio: {valores[1]}")
print(f"maior valor: {valores[2]}")