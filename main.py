from operator import truediv
import string

file = open("texto.txt", "r")

# variables = list(string.ascii_letters)
variables = ["a", "b", "c", "d"]
operadores = ["+", "-", "/", "*", "=", "^"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
tempText = ""
lenTempText = 0
stopCategoria = False
flag = False
cont = 1
listaValores = []

# Lee cada fila del archivo de texto
for line in file:
    #Saca cada palabra de la linea y la mete en una lista
    for word in line.split():
        listaValores.append(word)
    
    #Saca el número de comparaciones que el programa tendra que hacer para obtener el token del valor.
    for i in range (len(listaValores)):
        if stopCategoria == True:
            break
        #El valor de la lista dependiendo del índice lo mete a la variable tempText
        tempText = listaValores[i]
        #Regresa "flag" a su estado original para que categorize el valor
        flag = False
        for j in range(len(tempText)):

            #Revisa si es VARIABLE
            if flag == False:
                for k in range(len(variables)):
                    if tempText[j] == variables[k]:
                        print(tempText, ": Variables")
                        flag = True
                        cont += 1
                        break
            
            #Revisa si es OPERADOR
            if flag == False:
                for k in range(len(operadores)):
                    if tempText[j] == operadores[k]:
                        if tempText[j] == "+":
                            print(tempText, ": Suma")
                        elif tempText[j] == "*":
                            print(tempText, ": Multiplicación")
                        elif tempText[j] == "=":
                            print(tempText, ": Asignación")
                        elif tempText[j] == "^":
                            print(tempText, ": Potencia")
                        elif tempText[j] == "/":
                            try:
                                if tempText[j+1] == "/":
                                    r = i
                                    tempText = ""
                                    while r < len(listaValores):
                                        if tempText != "":
                                            tempText = tempText + " " + listaValores[r]
                                        else: 
                                            tempText = listaValores[r]
                                        r += 1
                                    print(tempText, ": Comentario")
                                    stopCategoria = True
                            except IndexError:
                                print(tempText, ": División")
                        elif tempText[j] == "-":
                            print(tempText, ": Resta")
                        flag = True
                        cont += 1
                        break

            if flag == False:
                for k in range(len(numeros)):
                    if tempText[j] == numeros[k]:
                        print(tempText, ": Enteros")
                        flag = True
                        cont += 1
                        break

    listaValores = []

# for line in file:
#     for character in line:
#         if check == False:
#             for i in range(len(variables)):
#                 if character == variables[i]:
#                     # if len(line) == cont and categoria == "Variable":
#                     #     tempText += character
#                     #     print(tempText, ": Variable")
#                     tempText += character
#                     categoria = "Variable"
#                     check = True
#                     break
#                 elif (character != variables[i] and len(variables)-1 == i and categoria == "Variable"):
#                     print(tempText, ": Variable")
#                     tempText = ""
#                     categoria = ""
#                     break
                
#         if check == False:
#             for i in range(len(operadores)):
#                 if character == operadores[i]:
#                     tempText += character
#                     print(tempText, ": Operador")
#                     tempText = ""
#                     check = True
#                     break

#         if check == False:
#             for i in range(len(numeros)):
#                 if character == numeros[i]:
#                     # if len(line) == cont and categoria == "Numero":
#                     #     tempText += character
#                     #     print(tempText, ": Entero")
#                     tempText += character
#                     categoria = "Numero"
#                     check = True
#                     break
#                 elif (character != numeros[i] and len(numeros)-1 == i and categoria == "Numero"):
#                     print(tempText, ": Entero")
#                     tempText = ""
#                     categoria = ""
#                     break

#         check = False
#         cont += 1
