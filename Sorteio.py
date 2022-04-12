import random

Sorteado = random.randint(0, 10)

Tentativa = 0
while Tentativa < 5:
    Escolha = eval(input("Escolha um número de 0 a 10: "))
    if Escolha < 0 or Escolha > 10:
        continue
    else:
        Tentativa += 1

    if Escolha == Sorteado:
        print("\n\t *** *** *** *** *** ***\n")
        print("\t*   SORTUDO! ACERTOU!!   *")
        print("\n\t *** *** *** *** *** ***")
        break
    elif Escolha < Sorteado:
        print("\nEscolheu um número menor que o sortedo.")
    else:
        print("\nEscolheu um número maior que o sortedo.")

    print("Tentativa ", Tentativa)

print("\nNÚMERO SORTEADO: ", Sorteado)

while True:
    Saida = str(input('\nPressione "ENTER" para sair: '))
    if not Saida:
        exit()