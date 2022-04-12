import time
Num= eval(input("Digite um número fatorial: "))
while (Num<=0 or Num>10):                          # limitar exageros dos usuários
    Num = eval(input("Digite um número fatorial: "))

Fatorial = 1
Voltas = 1
while Voltas <= Num:
    Fatorial *= Voltas
    #print(Fatorial) # imprime todos os resultados na tela
    #time.sleep(0.5) # apenas para teste de aprendizagem do programador
    Voltas += 1

    if Voltas == Num:  # vai imprimir na tela apenas o resultado final
        print(Fatorial)

while True:
    Saida = str(input('\nPressione "ENTER" para sair '))
    if not Saida:
        exit()
