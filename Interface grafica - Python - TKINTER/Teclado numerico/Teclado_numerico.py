from tkinter import Tk, Label, RAISED


root = Tk()
labels = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]
for r in range(4):
    for c in range(3):
        label = Label(root, relief=RAISED, padx=40, pady=20, text=labels[r][c], font=("Arial", 20))
        label.grid(row=r, column=c)

root.mainloop()