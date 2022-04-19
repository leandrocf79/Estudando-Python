def simetrica (m):
    linhas=len(m)
    colunas=len(m[0])
    for i in range (linhas):
        for j in range(i+1, colunas):
            if m[i][j] !=[j][i]:
                return False
    return True

m =  [[1, 2, 3], [2, 5, 6], [3, 3, 2]]
print (simetrica (m))

#***********************

def potencia(base,expoente):
    resultado = 1
    for numero in range(1,expoente+1):
        resultado = resultado * base
        return resultado
numero = eval(input("Entre um número que quer calcular (base): "))
expoente = eval(input("Entre o expoente: "))
print( 'Potencia : ' ,potencia(numero,expoente))

#***********************

matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
for i in range(0, 3):
    for j in range(0, 3):matriz[i] [j]
    if matriz[i][j] > 0:
        print('O elemento é maior que zero,',matriz[i] [j])
    elif matriz[i][j] < 0:
        print('O elemento é menor que zero,',matriz[i] [j])
    else:
        print('O elemento é zero')
for x in range(0, 3):
    for y in range(0, 3):
        print(matriz[x] [y])

#***********************

matrizNumeros = [ [ 1, 2, 3, 4 ],
                  [ 1, 3, 5, 7 ],
                  [ 8, 6, 4, 2 ],
                  [ 7, 5, 3, 1 ] ]

for i in range(len(matrizNumeros)) :
    for j in range(len(matrizNumeros[i])) :
        print(matrizNumeros[i][j], end=" ")

#***********************

matriz = [ [3, 4, 5], [5, 6, 7], [7, 6, 5] ]
for i in range(0, 3):
    print(matriz[i])

#***********************

aluno1Notas = [7.5, 7.0, 8.7]
aluno2Notas = [8.0, 5.0, 9.0]

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
        media = soma / len(aluno)
        return media

media = calcula_media(aluno1Notas)
print("A média do aluno 1 é: {:.2f}".format(media))
media = calcula_media(aluno2Notas)
print("A média do aluno 2 é: {:.2f}".format(media))

#***********************    ou

alunosNotas = [[7.5, 7.0, 8.7], [8.0, 5.0, 9.0]]

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
        media = soma / len(aluno)
        return media

media = calcula_media(alunosNotas[0])
print("A média do aluno 1 é: {:.2f}".format(media))
media = calcula_media(alunosNotas[1])
print("A média do aluno 2 é: {:.2f}".format(media))




