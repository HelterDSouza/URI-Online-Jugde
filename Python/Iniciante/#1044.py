valores = input().split()


a = int(valores[0])
b = int(valores[1])

if b > a:
    a, b = b, a

if a % b == 0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
