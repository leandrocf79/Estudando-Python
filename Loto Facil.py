import random
print("\n\n\tLOTO FACIL\n\n")
while True:
    entrar = str(input('\nPressione "ENTER" para escolher 15 números: '))
    if not entrar:
        break
i = 0
quant = 1
sorteio = []
while quant < 15:
    Sorteado = random.randint(1, 25)
    if Sorteado in sorteio:
        continue
    else:
        sorteio.append(Sorteado)
    quant = len(sorteio)

sorteio.sort()
print(f"\n {quant} NÚMEROS PARA JOGAR: ", sorteio)

while True:
    Saida = str(input('\nPressione "ENTER" para sair: '))
    if not Saida:
        exit()