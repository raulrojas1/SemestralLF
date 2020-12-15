from tkinter import *
import time
from analizadorLEX import *
from analizadorSIN import *

raiz = Tk()


def mostrartest(opcion,test):
    global imprimir,raiz
    raiz.destroy()
    raiz = Tk()
    raiz.geometry("900x700+200+30")
    # --- canvas creado con scroll ---

    canvas = Canvas(raiz,width=800,height=600)
    canvas.pack(side=LEFT)

    scrollbar = Scrollbar(raiz, command=canvas.yview)
    scrollbar.pack(side=LEFT, fill='y')

    canvas.configure(yscrollcommand = scrollbar.set)

    frame = Frame(canvas)
    canvas.create_window((100,0), window=frame, anchor='nw')


    # --- Se introduce label al framde del canvas ---
    if opcion=="lex":
        todoLEX(test)
        le = Label(frame, text=mensajeLEX(), font="size 16")
        le.pack()
        vaciarLEX()

    elif opcion=="sin":
        todoSIN(test)
        ls = Label(frame, text=mensajeSIN(), font="size 16")
        ls.pack()
        vaciarSIN()


    t1 = Button(raiz, text="Test 1",font="arial 15",command=lambda: mostrartest(opcion,1))
    t1.pack()

    t2 = Button(raiz, text="Test 2",font="arial 15",command=lambda: mostrartest(opcion,2))
    t2.pack()

    t3 = Button(raiz, text="Test 3",font="arial 15",command=lambda: mostrartest(opcion,3))
    t3.pack()

    t4 = Button(raiz, text="Test 4",font="arial 15",command=lambda: mostrartest(opcion,4))
    t4.pack()

    volver = Button(raiz, text="Volver",font="arial 15",command=presentacion)
    volver.pack()


    # --- inicia y actualiza ventana ---
    raiz.update()
    canvas.configure(scrollregion=canvas.bbox('all'))
    raiz.mainloop()





def elegirTest(opcion):
    global imprimir,raiz
    raiz.destroy()
    raiz = Tk()
    raiz.geometry("900x700+200+30")
    # --- canvas creado con scroll ---

    mensaje= Label(raiz, text="Haga clic en el teste que desea abrir",font="arial 20").place(x=300,y=90)
    t1 = Button(raiz, text="Test 1",font="arial 18",command=lambda: mostrartest(opcion,1)).place(x=400,y=200)
    t2 = Button(raiz, text="Test 2",font="arial 18",command=lambda: mostrartest(opcion,2)).place(x=400,y=300)

    t3 = Button(raiz, text="Test 3",font="arial 18",command=lambda: mostrartest(opcion,3)).place(x=400,y=400)
    t4 = Button(raiz, text="Test 4",font="arial 18",command=lambda: mostrartest(opcion,4)).place(x=400,y=500)

    # --- inicia y actualiza ventana ---
    raiz.update()
    raiz.mainloop()
#Decidir




#elegir lex o sin


#presentación
def presentacion():
    global raiz
    raiz.destroy()
    raiz = Tk()
    print("Semestral de LF")
    raiz.title("Presentación")
    raiz.geometry("900x600+200+30")
    raiz.configure(bg="bisque")
    miLabel = Label(raiz,text="Analizador Lexico ",font="arial 12",bg="bisque",fg="purple4")
    miLabel.pack()
    opc1 = Button(raiz, text="Lexico",font="arial 15",command=lambda: elegirTest("lex")).place(x=300,y=300)

    opc2 = Button(raiz, text="Sintactico",font="arial 15",command=lambda: elegirTest("sin")).place(x=500,y=300)
    raiz.mainloop()
presentacion()