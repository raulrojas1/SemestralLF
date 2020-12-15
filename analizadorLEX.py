import ply.lex as lex
import re
import codecs
import os
import sys

pos=0
salida = []

def mensaje():
    global salida
    return salida

reservadas = ['HF', 'GG', 'YF', 'MIENTRAS', 'KNT', 'DR', 'METRO', 'MOP', 'PARKING']

tokens = reservadas+['ID', 'NUMERO','SUMA','MENOS','MULTI','DIVIDIR','IMPAR','IGUAL','DISTINTO','MENOR','MENORI','MAYOR','MAYORI'
			,'PARENTI','PARENTD','COMA','PUNTOCOMA','ACTUALI', 'ESPACIO',  'NUMERAL', 'LLAVED',
                      'LLAVEI', 'COMILLA']

t_ignore = '  \t'
t_SUMA = r'\+'
t_MENOS = r'\-'
t_MULTI = r'\*'
t_DIVIDIR = r'/'
t_IMPAR = r'ODD'
t_IGUAL = r'='
t_DISTINTO = r'<>'
t_MENOR = r'<'
t_MENORI = r'<='
t_MAYOR = r'>'
t_MAYORI = r'>='
t_PARENTI = r'\('
t_PARENTD = r'\)'
t_COMA = r', '
t_PUNTOCOMA = r';'
t_ACTUALI = r'\:='
t_NUMERAL = r'\#'
t_LLAVED = r'\}'
t_LLAVEI= r'\{'
t_COMILLA = r'\"'




def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def COMMENT(t):
    r'\#.*'


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)


def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1

    while respuesta == False:
        numArchivo = input('\n Numero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    print("Usted ha seleccionado el archivo:  \"%s\" \n" % files[int(numArchivo) - 1])
    return files[int(numArchivo) - 1]


directorio = './test/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)
while True:
    tok = analizador.token()
    if not tok: break
    print(tok)
    salida.append(tok)
    salida.append("\n")
    pos+=1

