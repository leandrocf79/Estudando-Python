from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM
#from tkinter import *

root = Tk ()

photo = PhotoImage(file = 'Dori.gif').subsample(2)  #subsample: a cada 3px vai pegar 1px da
                                                   # imagem origial. Serve para diminir o tamanho
hello = Label( master = root, image=photo, width=500, height=370)
imagem =Label (master = root, image = photo)
imagem.pack(side=TOP) # local onde deve ser inserida a imagem

texto = Label(master=root, font= ("Cooper Black", 18), text = "Olá pessoal!") # Label adiciona texto
# hello = Label( master = root, text= "Olá pessoal!")
# hello.pack()
texto.pack(side = BOTTOM)

root.mainloop()