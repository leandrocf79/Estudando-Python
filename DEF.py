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
