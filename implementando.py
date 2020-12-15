from tkinter import *
import time
from analizadorLEX import mensaje

raiz = Tk()


def introducir():
    global imprimir,raiz
    raiz.destroy()
    raiz=Tk()
    raiz.title("Introducir Números")

    raiz.geometry("900x600+200+30")
    imprimir= Label(text=mensaje(),font="Arial 16",bg="white",fg="black").place(x=300, y= 10)
    ingresa= Button(raiz,text="Ingresar", font="Arial 20", ).place(x=300,y=400)
    raiz.mainloop()
#Decidir

#presentación
def presentacion():
    print("semestral")
    raiz.title("Presentación")
    raiz.geometry("900x600+200+30")
    raiz.configure(bg="bisque")
    miLabel = Label(raiz,
                    text="Vamo a ve si funcionaxd chaval ",font="arial 12",bg="bisque",fg="purple4")
    miLabel.pack()
    botonInicio = Button(raiz, text="Comenzar",font="arial 15",command=introducir)
    botonInicio.pack()
    raiz.mainloop()
presentacion()


"""
tiempo=0.0001 #segundos
vel=0.9        #pixeles cuántos pixeles se moverán en cuántos segundos
final= False
ordenados=[]
#                 1       2       3       4       5       6       7       8       9       10      11      12
posiciones=   [100,300,150,300,200,300,250,300,300,300,350,300,400,300,450,300,500,300,550,300,600,300,650,300]
comparar=[]
string=""
índices=[]
pasos=[]
arr =    [12,14,5,2]       #100,64,20,101,70,1,90,3,5,12,33,19
numeros= [12,14,5,2]
distancia=[]
posicion=0
partida=0
pos=0
A=0.0
B=0.0
C=0.0


x=100
y=500
bol=False

x1=100
y1=500

x2=200
y2=350

x3=400
y3=500

A=0
B=0
C=0



def calc_parábola(x1, y1, x2, y2, x3, y3):
    global A, B, C
    denom = (x1 - x2) * (x1 - x3) * (x2 - x3)
    A = round((x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom,4)
    B = round((x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom,4)
    C = round((x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom,4)

def coordenadas(partida,dirder):
    global x,y,final,raiz,A,B,C,timpo,vel
    if dirder == True:
        x += vel
    else:
        x -=vel
    y = int(A * (x ** 2) + B * x + C)
    while y<=298:
        if dirder==True:
            x+=vel
        else :
            x-=vel
        y = int(A * (x ** 2) + B * x + C)
        print(x,y)
        posiciones[partida]=x
        posiciones[partida+1]=y
        animando()
        time.sleep(tiempo)

#               32      64      20      24      70      10
# #             0       1       2       3       4       5
#posiciones=[200,300,270,300,350,300,420,300,490,300,560,300] indice*2
#             0   1   2   3   4   5   6   7   8   9  10   11
#posicion=0 indice[0]=0
def fuc_antes():
    global x,y,x1,y1,x2,y2,x3,y3,posicion,final,partida,posiciones,raiz
    partida=índices[posicion]*2
    final=índices[posicion+1]*2
#   x=200 y=300
#  x3=420 y3=30
    x=posiciones[partida]
    y=posiciones[partida+1]
    x1=x
    y1=y
    x3=posiciones[final]
    y3=posiciones[final+1]
    x2=(x1+x3)/2
    y2 = 200
    calc_parábola(x1, y1, x2, y2, x3, y3)
    dir=False
    if x1<x3:
        dir=True
        coordenadas(partida, dir)
        dir=False
        coordenadas(final, dir)
    else:
        coordenadas(partida, dir)
        dir = True
        coordenadas(final, dir)
    guardar1 = posiciones[partida]
    guardar2 = posiciones[partida + 1]
    posiciones[partida] = x3
    posiciones[partida + 1] = y3
    posiciones[final] = x1
    posiciones[final + 1] = y1
    posicion=posicion+2
    raiz.destroy()
    raiz = Tk()
    raiz.title("Introducir Números")
    raiz.geometry("900x600+200+30")
    matrix = PhotoImage(file="shell.png")
    fondo = Label(raiz, image=matrix).place(x=0, y=0)
    animando()




def animando():
    global raiz,pos,pasos,final,vel
    if(final==True):
        matrix = PhotoImage(file="shell.png")
        fondo = Label(raiz, image=matrix).place(x=0, y=0)
    primero= Label(raiz,text=numeros[pos],font="Arial 14",bg="purple").place(x=posiciones[pos], y=posiciones[pos+1])
    if len(numeros) > 1:
        segundo = Label(raiz,text=numeros[pos+1], font="Arial 14", bg="green").place(x=posiciones[pos+2], y=posiciones[pos+3])
    if len(numeros) > 2:
        tercero = Label(raiz,text=numeros[pos+2], font="Arial 14", bg="blue").place(x=posiciones[pos+4], y=posiciones[pos+5])
    if len(numeros) > 3:
        cuarto = Label(raiz,text=numeros[pos+3], font="Arial 14", bg="gold").place(x=posiciones[pos+6], y=posiciones[pos+7])
    if len(numeros) > 4:
        quinto = Label(raiz,text=numeros[pos+4], font="Arial 14", bg="spring green").place(x=posiciones[pos+8], y=posiciones[pos+9])
    if len(numeros)>5:
        sexto = Label(raiz,text=numeros[pos+5], font="Arial 14", bg="goldenrod").place(x=posiciones[pos+10], y=posiciones[pos+11])
    if len(numeros) > 6:
        séptimo= Label(raiz,text=numeros[pos+6],font="Arial 14",bg="purple").place(x=posiciones[pos+12], y=posiciones[pos+13])
    if len(numeros) > 7:
        octavo = Label(raiz,text=numeros[pos+7], font="Arial 14", bg="green").place(x=posiciones[pos+14], y=posiciones[pos+15])
    if len(numeros) > 8:
        noveno = Label(raiz,text=numeros[pos+8], font="Arial 14", bg="blue").place(x=posiciones[pos+16], y=posiciones[pos+17])
    if len(numeros) > 9:
        décimo = Label(raiz,text=numeros[pos+9], font="Arial 14", bg="gold").place(x=posiciones[pos+18], y=posiciones[pos+19])
    if len(numeros) > 10:
        onceavo = Label(raiz,text=numeros[pos+10], font="Arial 14", bg="spring green").place(x=posiciones[pos+20], y=posiciones[pos+21])
    if len(numeros) > 11:
        doceavo= Label(raiz,text=numeros[pos+11], font="Arial 14", bg="goldenrod").place(x=posiciones[pos+22], y=posiciones[pos+23])
    raiz.update()
    if final==True:
        raiz.mainloop()
def ordenado():
    global raiz, pos, pasos,final,vel
    raiz.destroy()
    raiz = Tk()
    raiz.title("Introducir Números")
    raiz.geometry("900x600+200+30")
    if len(numeros)>=9:
        vel=1.5
    for vueltas in range (int(len(índices)/2)):
        matrix = PhotoImage(file="shell.png")
        fondo = Label(raiz, image=matrix).place(x=0, y=0)
        fuc_antes()
        raiz.update()
    final=True
    animando()


def ordenar():
    global arr,ordenados,pos,distancia
    boleano=True
    bol2=True
    pos1 = 0
    pos2 = 0
    n = len(arr)
    string=arr
    comparar.append(string)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                print(f"{arr[j-gap]} < a {temp}?")
                string = str(arr)
                comparar.append(arr)

                while boleano==True or bol2==True:
                    if temp==numeros[pos1] and boleano==True:
                        print(temp, numeros[pos1])
                        índices.append(pos1)
                        boleano=False

                    if arr[j-gap]==numeros[pos2] and bol2==True:
                        print(arr[j - gap], numeros[pos2])
                        índices.append(pos1)
                        bol2=False
                    pos1+=1
                    pos2+=1
                pos1=0
                pos2=0
                arr[j] = arr[j-gap]
                boleano = True
                bol2 = True
                j -= gap
            arr[j] = temp
        gap //= 2
    ordenado()

def meter(uno):
    global arr,numeros,raiz
    valor=uno.get()
    ingresar=int(valor)
    arr.append(ingresar)
    numeros.append(ingresar)
    imprimir = Label(text=numeros, font="Arial 20", bg="white", fg="black").place(x=300, y=140)
    raiz.update()"""

