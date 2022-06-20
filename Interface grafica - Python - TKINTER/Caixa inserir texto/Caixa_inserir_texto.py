from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime
def compute():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was on {}'.format(date, weekday))
root = Tk()
label = Label(root, text= 'Digite uma data no modelo em inglês,\n exemplo( oct 2, 1979 ): \n\n')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Clique aqui', command=compute)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()