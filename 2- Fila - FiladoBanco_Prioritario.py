# Chamar 2 preferenciais e 1 não preferencial na fila.

class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):  # inserir
        self.data.append(x)

    def remover(self):  # remover
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:  # exibir sem remover
            return self.data.top(0)

    def vazio(self):  # verifica lista vazia
        return not len(self.data) > 0


fila_normal = Fila()
fila_normal.data = [20, 30, 45, 50, 18, 22, 32, 19, 46]

fila_preferencial = Fila()
fila_preferencial.data = [70, 67, 86, 77, 81, 60, 85, 93, 77]

while (len(fila_normal.data) + len(fila_preferencial.data)) > 0:

    for i in range(2):
        if not fila_preferencial.vazio():
            print(fila_preferencial.remover(), " preferencial")

    if not fila_normal.vazio():
        print(fila_normal.remover())