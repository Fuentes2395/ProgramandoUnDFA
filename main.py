from enum import Flag
import string
from this import d

file = open("texto.txt", "r")

# variables = list(string.ascii_letters)
variables = ["a", "b", "c"]
operadores = ["+", "-", "/", "*", "=", "^"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
tempText = ""
flag = False
check = False
diccionario = {}
listaKeys = []
cont = 0

for line in file:
    for character in line:
        if check == False:
            for i in range(len(variables)):
                if character == variables[i]:
                    tempText += character
                    flag = True
                    check = True
                    break
                elif character != variables[i] and len(variables)-1 == i and flag == True:
                    print(tempText, ": Variable")
                    tempText = ""
                    flag = False
                    break
                
        if check == False:
            for i in range(len(operadores)):
                if character == operadores[i]:
                    tempText += character
                    print(tempText, ": Operador")
                    tempText = ""
                    check = True
                    break

        if check == False:
            for i in range(len(numeros)):
                if character == numeros[i]:
                    tempText += character
                    print(tempText, ": Entero")
                    i = 0
                    flag = True
                    check = True
                    break
                elif character != numeros[i] and len(numeros)-1 == i and flag == True:
                    print(tempText, ": Entero")
                    tempText = ""
                    flag = False
                    break

        check = False
