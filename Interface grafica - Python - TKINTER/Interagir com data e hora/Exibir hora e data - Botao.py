from tkinter  import Tk, Button, Label, PhotoImage, BOTTOM
from tkinter.messagebox import showinfo
from time import strftime, localtime
def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime()) # "p" é sobre o periodo da tarde ou manaha...
    showinfo(message=time)


root = Tk()    # cria a janela principal
button = Button(root, text='Clique', command=clicked) # cria o botao com texto. Clicked foi definido acima.

photo = PhotoImage(file='giro.gif').subsample(5)
imagem = Label(master=root, image=photo)
imagem.pack(side=BOTTOM)

button.pack()  # empacota a janela com o botao
root.mainloop()  # exibe na tela o conteudo