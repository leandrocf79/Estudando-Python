import random
print("*   leandrocf79@gmail.com   *")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("\t\n GERADOR DE JOGOS")
print("\t\n JOGOS DA LOTERICA\n\n ")
while True:

    while True:
        print(" [ 1 ] Lotomania\n"
              " [ 2 ] Loto Facil\n"
              " [ 3 ] Mega Sena\n"
              " [ 4 ] Dupla Sena\n"
              " [ 5 ] Quina\n")

        op = eval(input("\t Digite um número para continuar: "))
        if (op < 0 or op > 4):
            pass
        # ************

        if (op == 1):
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            print("\n\n\t*\tLOTOMANIA\t*\n\n")
            while True:
                entrar = str(input('\nPressione "ENTER" para escolher 50 números: '))
                if not entrar:
                    break
            i = 0
            quant1 = 1
            quant2 = 1
            quant3 = 1
            quant4 = 1
            quant5 = 1

            sorteio1 = []
            sorteio2 = []
            sorteio3 = []
            sorteio4 = []
            sorteio5 = []
            while quant1 < 10:
                Sorteado = random.randint(00, 99)
                if Sorteado in sorteio1:
                    continue
                else:
                    sorteio1.append(Sorteado)
                quant1 = len(sorteio1)  # Conferir contagem
            sorteio1.sort()

            while quant2 < 10:
                Sorteado = random.randint(00, 99)
                if Sorteado in sorteio1:
                    continue
                elif Sorteado in sorteio2:
                    continue
                else:
                    sorteio2.append(Sorteado)
                quant2 = len(sorteio2)
            sorteio2.sort()

            while quant3 < 10:
                Sorteado = random.randint(00, 99)
                if Sorteado in sorteio1:
                    continue
                elif Sorteado in sorteio2:
                    continue
                elif Sorteado in sorteio3:
                    continue
                else:
                    sorteio3.append(Sorteado)
                quant3 = len(sorteio3)  # Conferir contagem
            sorteio3.sort()

            while quant4 < 10:
                Sorteado = random.randint(00, 99)
                if Sorteado in sorteio1:
                    continue
                elif Sorteado in sorteio2:
                    continue
                elif Sorteado in sorteio3:
                    continue
                elif Sorteado in sorteio4:
                    continue
                else:
                    sorteio4.append(Sorteado)
                quant4 = len(sorteio4)
            sorteio4.sort()

            while quant5 < 10:
                Sorteado = random.randint(00, 99)
                if Sorteado in sorteio1:
                    continue
                elif Sorteado in sorteio2:
                    continue
                elif Sorteado in sorteio3:
                    continue
                elif Sorteado in sorteio4:
                    continue
                elif Sorteado in sorteio5:
                    continue
                else:
                    sorteio5.append(Sorteado)
                quant5 = len(sorteio5)
            sorteio5.sort()
            Quant_Total = quant1 + quant2 + quant3 + quant4 + quant5

            print(f" \n{Quant_Total} NÚMEROS PARA JOGAR:\n",
                    (sorteio1), "\n",
                    (sorteio2), "\n",
                    (sorteio3), "\n",
                    (sorteio4), "\n",
                    (sorteio5))

            Voltar_menu = str(input('\n\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n'
                                    'Fazer novo jogo?\n\n'
                                    '[  1  ] Para voltar ao menu\n'
                                    '[Enter] Para sair\n'))
            print("\n" * 5)
            if not Voltar_menu:
                exit()


        # ************

        elif (op == 2):
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            print("\n\n\t*\tLOTO FACIL\t*\n\n")
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
            print(f"\n {quant} NÚMEROS PARA JOGAR: \n", sorteio)


            Voltar_menu = str(input('\n\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n'
                                    'Fazer novo jogo?\n\n'
                                    '[  1  ] Para voltar ao menu\n'
                                    '[Enter] Para sair\n'))
            print("\n" * 5)
            if not Voltar_menu:
                exit()

        # ************

        elif (op == 3):
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            print("\n\n\t*\tMEGA SENA\t*\n\n")
            while True:
                entrar = str(input('\nPressione "ENTER" para escolher 6 números: '))
                if not entrar:
                    break
            i = 0
            quant = 1
            sorteio = []
            while quant < 6:
                Sorteado = random.randint(1, 60)
                if Sorteado in sorteio:
                    continue
                else:
                    sorteio.append(Sorteado)
                quant = len(sorteio)

            sorteio.sort()
            print(f"\n {quant} NÚMEROS PARA JOGAR: \n", sorteio)



            Voltar_menu = str(input('\n\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n'
                                    'Fazer novo jogo?\n\n'
                                    '[  1  ] Para voltar ao menu\n'
                                    '[Enter] Para sair\n'))
            print("\n" * 5)
            if not Voltar_menu:
                exit()


        # ************

        elif (op == 4):
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            print("\n\n\t*\tDUPLA SENA\t*\n\n")
            while True:
                entrar = str(input('\nPressione "ENTER" para escolher 6 números: '))
                if not entrar:
                    break
            i = 0
            quant = 1
            sorteio = []
            while quant < 6:
                Sorteado = random.randint(1, 50)
                if Sorteado in sorteio:
                    continue
                else:
                    sorteio.append(Sorteado)
                quant = len(sorteio)

            sorteio.sort()
            print(f"\n {quant} NÚMEROS PARA JOGAR: \n", sorteio)



            Voltar_menu = str(input('\n\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n'
                                    'Fazer novo jogo?\n\n'
                                    '[  1  ] Para voltar ao menu\n'
                                    '[Enter] Para sair\n'))
            print("\n" * 5)
            if not Voltar_menu:
                exit()

        # ************

        elif (op == 5):
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            print("\n\n\t\tQUINA\t\n\n")
            while True:
                entrar = str(input('\nPressione "ENTER" para escolher 5 números: '))
                if not entrar:
                    break
            i = 0
            quant = 1
            sorteio = []
            while quant < 5:
                Sorteado = random.randint(1, 80)
                if Sorteado in sorteio:
                    continue
                else:
                    sorteio.append(Sorteado)
                quant = len(sorteio)

            sorteio.sort()
            print(f"\n {quant} NÚMEROS PARA JOGAR: \n", sorteio)




            Voltar_menu = str(input('\n\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n'
                                    'Fazer novo jogo?\n\n'
                                    '[  1  ] Para voltar ao menu\n'
                                    '[Enter] Para sair\n'))
            print("\n" * 5)
            if not Voltar_menu:
                exit()
