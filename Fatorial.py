num=eval(input("Digite um número fatorial: "))

fatorial=1
voltas=1
while voltas <= num:
    fatorial*=voltas
    print(fatorial)
    voltas+=1
