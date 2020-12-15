import ply.yacc as yacc
import os
import codecs
import re
from analizadorLEX import tokens,todoLEX

from sys import stdin

salidaSIN = []

def mensajeSIN():
    global salidaSIN
    return salidaSIN

def vaciarSIN():
    global salidaSIN
    del salidaSIN[:]
    return

precedente = (
	('right','ID','COMA', 'KNT','HF','YF','MIENTRAS'),
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
	salidaSIN.append("program")
	salidaSIN.append("\n")

def p_block(p):
	'''block : constDec1 varDec1 procDec1 statement'''
	print ("block")
	salidaSIN.append("block")
	salidaSIN.append("\n")

def p_constDec1(p):
	'''constDec1 : DR constAssignmentList PUNTOCOMA'''
	print ("constDec1")
	salidaSIN.append("constDec1")
	salidaSIN.append("\n")

def p_constDec1Empty(p):
	'''constDec1 : empty'''
	#p[0] = Null()
	print ("nulo")
	salidaSIN.append("nulo")
	salidaSIN.append("\n")

def p_constAssignmentList1(p):
	'''constAssignmentList : ID ACTUALI NUMERO'''
	print ("constAssigmentList1")
	salidaSIN.append("constAssigmentList1")
	salidaSIN.append("\n")

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMA ID ACTUALI NUMERO'''
	print ("constAssignmentList 2")
	salidaSIN.append("constAssignmentList 2")
	salidaSIN.append("\n")

def p_varDec1(p):
	'''varDec1 : METRO identList PUNTOCOMA'''
	print ("varDec1")
	salidaSIN.append("varDec1")
	salidaSIN.append("\n")

def p_varDec1Empty(p):
	'''varDec1 : empty'''
	print ("nulo")
	salidaSIN.append("nulo")
	salidaSIN.append("\n")

def p_identList1(p):
	'''identList : ID'''
	print ("identList 1")
	salidaSIN.append("identList 1")
	salidaSIN.append("\n")

def p_identList2(p):
	'''identList : identList COMA ID'''
	print ("identList 2")
	salidaSIN.append("identList 2")
	salidaSIN.append("\n")

def p_procDec1(p):
	'''procDec1 : procDec1 MOP ID PUNTOCOMA block PUNTOCOMA'''
	print ("Ejecucion de proceso")
	salidaSIN.append("Ejecucion de proceso")
	salidaSIN.append("\n")

def p_procDec1Empty(p):
	'''procDec1 : empty'''
	print ("nulo procDec")
	salidaSIN.append("nulo procDec")
	salidaSIN.append("\n")

def p_statement1(p):
	'''statement : ID ACTUALI expression'''
	print ("statement actualizar")
	salidaSIN.append("statement actualizar")
	salidaSIN.append("\n")

def p_statement2(p):
	'''statement : KNT ID'''
	print ("statement llamada")
	salidaSIN.append("statement llamada")
	salidaSIN.append("\n")

def p_statement3(p):
	'''statement : HF statementList GG'''
	print ("statement inicio")
	salidaSIN.append("statement inicio")
	salidaSIN.append("\n")

def p_statement4(p):
	'''statement : YF condition LLAVEI statement LLAVED'''
	print ("statement condicional si")
	salidaSIN.append("statement condicional si")
	salidaSIN.append("\n")

def p_statement5(p):
	'''statement : MIENTRAS condition LLAVEI statement LLAVED'''
	print ("statement condicional mientras")
	salidaSIN.append("statement condicional mientras")
	salidaSIN.append("\n")

def p_statementEmpty(p):
	'''statement : empty'''
	print ("nulo statement empty")
	salidaSIN.append("nulo statement empty")
	salidaSIN.append("\n")

def p_statementList1(p):
	'''statementList : statement'''
	print ("statementList 1")
	salidaSIN.append("statementList 1")
	salidaSIN.append("\n")

def p_statementList2(p):
	'''statementList : statementList PUNTOCOMA statement'''
	print ("statementList 2")
	salidaSIN.append("statementList 2")
	salidaSIN.append("\n")

def p_condition1(p):
	'''condition : IMPAR expression'''
	print ("condition 1")
	salidaSIN.append("condition 1")
	salidaSIN.append("\n")

def p_condition2(p):
	'''condition : expression relation expression'''
	print ("condition 2")
	salidaSIN.append("condition 2")
	salidaSIN.append("\n")

def p_relation1(p):
	'''relation : IGUAL'''
	print ("relation IGUAL")
	salidaSIN.append("relation IGUAL")
	salidaSIN.append("\n")

def p_relation2(p):
	'''relation : DISTINTO'''
	print ("relation DISTINTO")
	salidaSIN.append("relation DISTINTO")
	salidaSIN.append("\n")

def p_relation3(p):
	'''relation : MENOR'''
	print ("relation MENOR")
	salidaSIN.append("relation MENOR")
	salidaSIN.append("\n")

def p_relation4(p):
	'''relation : MAYOR'''
	print ("relation MAYOR")
	salidaSIN.append("relation MAYOR")
	salidaSIN.append("\n")

def p_relation5(p):
	'''relation : MENORI'''
	print ("relation menor igual")
	salidaSIN.append("relation menor igual")
	salidaSIN.append("\n")

def p_relation6(p):
	'''relation : MAYORI'''
	print ("relation mayor igual")
	salidaSIN.append("relation mayor igual")
	salidaSIN.append("\n")

def p_expression1(p):
	'''expression : term '''
	print ("expression 1")
	salidaSIN.append("expression 1")
	salidaSIN.append("\n")

def p_expression2(p):
	'''expression : addingOperator term'''
	print ("expression suma")
	salidaSIN.append("expression suma")
	salidaSIN.append("\n")

def p_expression3(p):
	'''expression : expression addingOperator term '''
	print ("expression 3")
	salidaSIN.append("expression 3")
	salidaSIN.append("\n")

def p_addingOperator1(p):
	'''addingOperator : SUMA'''
	print ("addingOperator suma")
	salidaSIN.append("addingOperator suma")
	salidaSIN.append("\n")

def p_addingOperator2(p):
	'''addingOperator : MENOS'''
	print ("addingOperator resta")
	salidaSIN.append("addingOperator resta")
	salidaSIN.append("\n")

def p_term1(p):
	'''term : factor'''
	print ("term 1")
	salidaSIN.append("term 1")
	salidaSIN.append("\n")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print ("term 2")
	salidaSIN.append("term 2")
	salidaSIN.append("\n")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : MULTI'''
	print ("multiplyingOperator multiplicar")
	salidaSIN.append("multiplyingOperator multiplicar")
	salidaSIN.append("\n")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDIR'''
	print ("multiplyingOperator dividir")
	salidaSIN.append("multiplyingOperator dividir")
	salidaSIN.append("\n")

def p_factor1(p):
	'''factor : ID'''
	print ("factor id")
	salidaSIN.append("factor id")
	salidaSIN.append("\n")

def p_factor2(p):
	'''factor : NUMERO'''
	print ("factor 2")
	salidaSIN.append("factor 2")
	salidaSIN.append("\n")

def p_factor3(p):
	'''factor : PARENTI expression PARENTD'''
	print ("factor 3")
	salidaSIN.append("factor 3")
	salidaSIN.append("\n")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print ("Error de sintaxis", p)
	salidaSIN.append("Error de sintaxis")
	salidaSIN.append(p)
	salidaSIN.append("\n")

def buscarFicheros(directorio,numero):
    todoLEX(1)
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
        numArchivo = numero
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    print("Usted ha seleccionado el archivo:  \"%s\" \n" % files[int(numArchivo) - 1])
    return files[int(numArchivo) - 1]

def todoSIN(numero):
	directorio = './test/'
	archivo = buscarFicheros(directorio,numero)
	test = directorio + archivo
	fp = codecs.open(test, "r", "utf-8")
	cadena = fp.read()
	fp.close()

	parser = yacc.yacc()
	result = parser.parse(cadena)
	print (result)
