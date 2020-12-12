import ply.yacc as yacc
import re
import codecs
import os
from analizadorLEX import tokens

from sys import stdin

precedente = (
	('right','ID','CALL','BEGIN','IF','WHILE'),
	('right','PROCEDURE'),
	('right','VAR'),
	('right','ASSIGN'),
	('right','UPDATE'),
	('left','NE'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','ODD'),
	('left','LPARENT','RPARENT'),
	)


def p_program(p):
	''' program : block '''
	print "program"

def p_block(p):
	''' block : constDec1 varDec1 procDec1 statement '''
	print "block"

def p_constDec1(p):
	'''constDec1 : CONST constAssignmentList SEMMICOLON'''
	print "constDec1"

def p_constDec1Empty(p):
	'''constDec1 : empty'''
	#p[0] = Null()
	print "nulo"

def p_constAssignmentList1(p):
	'''constAssignmentList1 : ID ASSIGN NUMBER'''
	print "constAssignmentList 1"

def p_constAssignmentList2(p):
	'''constAssignmentList1 : constAssignmentList COMMA ID ASSIGN NUMBER'''
	print "constAssignmentList 2"

def p_varDec11(p):
	'''varDec1 : VAR identList SEMMICOLON'''
	print "varDec1"

def p_varDec1Empty(p):
	'''varDec1 : empty'''
	print "nulo"

def p_identList1(p):
	'''identList : ID'''
	print "identList 1"

def p_identList2(p):
	'''identList : identList COMMA ID'''
	print "identList 2"

def p_procDec11(p):
	'''procDec1 : procDec1 PROCEDURE ID SEMMICOLON block SEMMICOLON'''
	print "procDec1 1"

def p_procDec1Empty(p):
	'''procDec1 : empty'''
	print "nulo"

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	print "statement 1"

def p_statement2(p):
	'''statement : CALL ID'''
	print "statement 2"

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	print "statement 3"

def p_statement4(p):
	'''statement : IF condition THEN statement'''
	print "statement 4"

def p_statement5(p):
	'''statement : WHILE condition DO statement'''
	print "statement 5"

def p_statementEmpty(p):
	'''statement : empty'''
	print "nulo"

def p_statementList1(p):
	'''statementList : stratement'''
	print "statementList 1"

def p_statementList2(p):
	'''statementList : stratementList SEMMICOLON statement'''
	print "statementList 2"

def p_condition1(p):
	'''condition : ODD expression'''
	print "condition 1"

def p_condition2(p):
	'''condition : expression relation expression'''
	print "condition 2"

def p_relation1(p):
	'''relation : ASSIGN'''
	print "relation 1"

def p_relation2(p):
	'''relation : NE'''
	print "relation 2"

def p_relation3(p):
	'''relation : LT'''
	print "relation 3"

def p_relation4(p):
	'''relation : GT'''
	print "relation 4"

def p_relation5(p):
	'''relation : LTE'''
	print "relation 5"

def p_relation6(p):
	'''relation : GTE'''
	print "relation 6"

def p_expression1(p):
	'''expression : term'''
	print "expression 1"

def p_expression2(p):
	'''expression : addingOperator term'''
	print "expression 2"

def p_expression3(p):
	'''expression : expression addingOperator term'''
	print "expression 3"

def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	print "addingOperator 1"

def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	print "addingOperator 2"

def p_term1(p):
	'''term : factor'''
	print "term 1"

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print "term 2"

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	print "multiplyingOperator 1"

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	print "multiplyingOperator 2"

def p_factor1(p):
	'''factor : ID'''
	print "factor 1"

def p_factor2(p):
	'''factor : NUMBER'''
	print "factor 2"

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''
	print "factor 3"

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print "Error de sintaxis", p

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


directorio = 'C:/Users/Alejandro De Puy/Documents/ProyectodeLengajes/analizadorversion3/test/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print (result)
