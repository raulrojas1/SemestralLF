from tkinter import *
from analizadorLEX import mensaje


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


raiz = Tk()
raiz.geometry("800x600")
# --- create canvas with scrollbar ---

canvas = Canvas(raiz,width=800,height=600)
canvas.pack(side=LEFT)

scrollbar = Scrollbar(raiz, command=canvas.yview)
scrollbar.pack(side=LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---


l = Label(frame, text=mensaje(), font="size 16")
l.pack()

# --- start program ---

raiz.mainloop()