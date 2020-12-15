import ply.yacc as yacc
import os
import codecs
import re
from analizadorLEX import tokens

from sys import stdin
precedente = (
	('right','ID','COMA', 'KNT','HF','YF','MIENTRAS'),
	('left', 'WOLAN'),
	('right','MOP'),
	('right','METRO'),
	('right','IGUAL'),
	('right','ACTUALI'),
	('left','DISTINTO'),
	('right', 'NUMERAL'),
	('right', 'COMILLA'),
	('left','MENOR','MENORI','MAYOR','MAYORI'),
	('left','SUMA','MENOS'),
	('left','MULTI','DIVIDIR'),
	('right','IMPAR'),
	('left', 'LLAVEI', 'LLAVED'),
	('left','PARENTI','PARENTD'),
	('left', 'PUNTOCOMA')

	)


def p_program(p):
	'''program : block'''
	print ("program")

def p_block(p):
	'''block : constDec1 varDec1 procDec1 statement'''
	print ("block")

def p_constDec1(p):
	'''constDec1 : DR constAssignmentList PUNTOCOMA'''
	print ("constDec1")

def p_constDec1Empty(p):
	'''constDec1 : empty'''
	#p[0] = Null()
	print ("nulo")
def p_constAssignmentList1(p):
	'''constAssignmentList : ID ACTUALI NUMERO'''
	print ("constAssigmentList1")

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMA constAssignmentList'''
	print ("constAssignmentList 2")

def p_varDec1(p):
	'''varDec1 : METRO identList PUNTOCOMA'''
	print ("varDec1")

def p_varDec1Empty(p):
	'''varDec1 : empty'''
	print ("nulo")

def p_identList1(p):
	'''identList : ID'''
	print ("identList 1")

def p_identList2(p):
	'''identList : ID ACTUALI NUMERO'''
	print ("identList 2")


def p_identList3(p):
	'''identList : identList COMA identList'''
	print ("identList 3")

def p_procDec1(p):
	'''procDec1 : procDec1 MOP ID PUNTOCOMA block PUNTOCOMA'''
	print ("Ejecucion de proceso")

def p_procDec1Empty(p):
	'''procDec1 : empty'''
	print ("nulo procDec")

def p_statement1(p):
	'''statement : HF statementList GG'''
	print ("statement inicio")

def p_statement2(p):
	'''statement : ID ACTUALI expression PUNTOCOMA'''
	print ("statement actualizar")

def p_statement3(p):
	'''statement : KNT STRING PUNTOCOMA'''
	print ("statement IMPRIMIR " + str(p[2]))

def p_statement4(p):
	'''statement : YF condition LLAVEI statement LLAVED'''
	print ("statement condicional si")


def p_statement5(p):
	'''statement : YF condition LLAVEI statement LLAVED WOLAN LLAVEI statement LLAVED'''
	print ("statement condicional if else")


def p_statement6(p):
	'''statement : MIENTRAS condition LLAVEI statement LLAVED'''
	print ("statement condicional mientras")

def p_statementEmpty(p):
	'''statement : empty'''
	print ("nulo statement empty")


def p_statementList1(p):
	'''statementList : statement'''
	print ("statementList 1")

def p_statementList2(p):
	'''statementList : statementList statementList'''
	print ("statementList 2")




def p_condition1(p):
	'''condition : IMPAR expression'''
	print ("condition 1")

def p_condition2(p):
	'''condition : expression relation expression'''
	print ("condition 2")

def p_relation1(p):
	'''relation : IGUAL'''
	print ("relation IGUAL")

def p_relation2(p):
	'''relation : DISTINTO'''
	print ("relation DISTINTO")

def p_relation3(p):
	'''relation : MENOR'''
	print ("relation MENOR")

def p_relation4(p):
	'''relation : MAYOR'''
	print ("relation MAYOR")

def p_relation5(p):
	'''relation : MENORI'''
	print ("relation menor igual")

def p_relation6(p):
	'''relation : MAYORI'''
	print ("relation mayor igual")

def p_expression1(p):
	'''expression : term '''
	print ("expression 1")

def p_expression2(p):
	'''expression : addingOperator term'''
	print ("expression suma")

def p_expression3(p):
	'''expression : expression addingOperator term '''
	print ("expression 3")

def p_addingOperator1(p):
	'''addingOperator : SUMA'''
	print ("addingOperator suma")

def p_addingOperator2(p):
	'''addingOperator : MENOS'''
	print ("addingOperator resta")

def p_term1(p):
	'''term : factor'''
	print ("term 1")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print ("term 2")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : MULTI'''
	print ("multiplyingOperator multiplicar")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDIR'''
	print ("multiplyingOperator dividir")

def p_factor1(p):
	'''factor : ID'''
	print ("factor id")


def p_factor2(p):
	'''factor : NUMERO'''
	print ("factor numero")

def p_factor3(p):
	'''factor : PARENTI expression PARENTD'''
	print ("factor 3")


def p_factor4(p):
	'''factor : STRING'''
	print ("factor string")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	result = "Error sintactico de tipo {} en el valor {}".format(str(p.type),str(p.value))
	print (result)

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

parser = yacc.yacc()
result = parser.parse(cadena)



print (result)