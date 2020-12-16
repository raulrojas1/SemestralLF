import ply.yacc as yacc
import os
import codecs
import re
from analizadorLEX import tokens,todoLEX

salidaSIN = []

def mensajeSIN():
    global salidaSIN
    return salidaSIN

def vaciarSIN():
    global salidaSIN
    del salidaSIN[:]
    return


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
	('left', 'PUNTOCOMA'),
	('left', 'SUMA', 'MENOS'),
    ('left', 'MULTI', 'DIVIDIR')
	)

id_names = {}

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
def p_constAssignmentList1(p):
	'''constAssignmentList : ID ACTUALI NUMERO'''
	print ("constAssigmentList1")
	salidaSIN.append("constAssignmentList1")
	salidaSIN.append("\n")
	id_names[p[1]] = p[3]

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMA constAssignmentList'''
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
	'''identList : ID ACTUALI NUMERO'''
	print ("identList 2")
	salidaSIN.append("identList 2")
	salidaSIN.append("\n")
	id_names[p[1]] = p[3]


def p_identList3(p):
	'''identList : identList COMA identList'''
	print ("identList 3")
	salidaSIN.append("identList 3")
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
	'''statement : HF statementList GG'''
	print ("statement inicio")
	salidaSIN.append("statement inicio")
	salidaSIN.append("\n")

def p_statement2(p):
	'''statement : ID ACTUALI expression PUNTOCOMA'''
	print ("statement actualizar")
	salidaSIN.append("statement actualizar")
	salidaSIN.append("\n")

def p_statement3(p):
	'''statement : KNT STRING PUNTOCOMA'''
	print ("statement IMPRIMIR " + str(p[2]))
	salidaSIN.append("statement IMPRIMIR " + str(p[2]))
	salidaSIN.append("\n")

def p_statementVars(p):
	'''statement : KNT ID PUNTOCOMA'''
	try:
		print ("Valor de ID {:2} es {:4}".format(str(p[2]), str(id_names[p[2]]) ))
		salidaSIN.append("Valor de ID {:2} es {:4}".format(str(p[2]),str(id_names[p[2]]) ))
		salidaSIN.append("\n")
	except LookupError:
		print("ID desconocido: ".format(str(p[2])))
		salidaSIN.append("ID desconocido: ".format(str(p[2])))
		salidaSIN.append("\n")

def p_statement4(p):
	'''statement : YF condition LLAVEI statement LLAVED'''
	print ("statement condicional si")
	salidaSIN.append("statement condicional si")
	salidaSIN.append("\n")


def p_statement5(p):
	'''statement : YF condition LLAVEI statement LLAVED WOLAN LLAVEI statement LLAVED'''
	print ("statement condicional if else")
	salidaSIN.append("statement condicional if else")
	salidaSIN.append("\n")


def p_statement6(p):
	'''statement : MIENTRAS condition LLAVEI statement LLAVED'''
	print ("statement condicional mientras")
	salidaSIN.append("statement condicional mientras")
	salidaSIN.append("\n")

#expresion usada para resultados matematicos
def p_statement7(p):
	'''statement : KNT expression PUNTOCOMA'''
	print("expresion matematica: ", str(p[2]))
	salidaSIN.append("expresion matematica "+ str(p[2]))
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
	'''statementList : statementList statementList'''
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
	salidaSIN.append("relation menor igual")
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
	salidaSIN.append("factor numero")
	salidaSIN.append("\n")
	p[0] = p[1]

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
	p[0] = p[1]

def p_subOperator(p):
	'''subOperator : MENOS'''
	print ("subOperator resta")
	salidaSIN.append("subOperator resta")
	salidaSIN.append("\n")
	p[0] = p[1]

def p_term1(p):
	'''term : factor'''
	print ("term 1")
	p[0] = p[1]
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
	print ("factor numero")
	p[0] = p[1]
	salidaSIN.append("factor numero")
	salidaSIN.append("\n")


def p_factor4(p):
	'''factor : STRING'''
	print ("factor string")
	salidaSIN.append("factor string")
	salidaSIN.append("\n")	

# matematicas
def p_add(p):
	'''expression : factor addingOperator factor'''
	p[0] = p[1] + p[3]



def p_sub(p):
	'''expression : factor subOperator factor'''
	p[0] = p[1] - p[3]

def p_mult_div(p):
	'''expression : factor MULTI factor
					| factor DIVIDIR factor'''
	if p[2] == '*':
		p[0] = p[1] * p[3]
	else:
		if p[3] == 0:
			print("No puedes dividir entre 0")
			raise ZeroDivisionError("division entre zero")
			salidaSIN.append("deivision entre cero")
			salidaSIN.append("\n")

		p[0] = p[1] / p[3]


def p_mult_div2(p):
	'''expression : expression MULTI expression
					| expression DIVIDIR expression'''
	if p[2] == '*':
		p[0] = p[1] * p[3]
	else:
		if p[3] == 0:
			print("No puedes dividir entre 0")
			raise ZeroDivisionError("division entre zero")
			salidaSIN.append("division entre zero")
			salidaSIN.append("\n")
		p[0] = p[1] / p[3]

#concatenate math expressions
def p_parens(p):
	'''expression : PARENTI expression PARENTD'''
	print ("expression parentesis")
	salidaSIN.append("expression parente")
	salidaSIN.append("\n")
	p[0] = p[2]

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	result = "Error sintactico de tipo {} en el valor {}".format(str(p.type),str(p.value))
	salidaSIN.append("Error de sintaxis")
	salidaSIN.append(p)
	salidaSIN.append("\n")
	print (result)

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
