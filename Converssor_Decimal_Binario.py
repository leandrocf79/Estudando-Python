class Pilha():
    def __init__(self):
        self.data=[]

    def push(self, x):    #insere elementos
        self.data.append(x)

    def pop(self):      # remove um elemento da pilha
        if len(self.data) >0:
            return self.data.pop(-1) # O -1 REMOVE o último elemento da lista

    def top(self):          # vai verificar se tem pelo menos um elemento inserido
        if len(self.data) > 0:
            return self.data[-1] # O -1 está consultando o último elemento da lista

    def empty(self):  # Verifica se a pilha está vazia
        return not len(self.data) >0

p=Pilha()
num= int(input("Digite um número decimal para converter para binário: "))
while num > 0:
    resto=num %2
    num=num//2
    p.push(resto)

# desemplilhar
while not p.empty():
    print(p.pop())



