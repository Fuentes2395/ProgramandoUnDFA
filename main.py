import string

file = open("texto.txt", "r")

variables = list(string.ascii_letters)
operadores = ["+", "-", "/", "*", "=", "^"]
tempText = ""
flag = False
diccionarioImpreso = {}


# for line in file:
#     text = line
#     for i in range(len(text)):
#         for j in range(len(variables)):
#             if text[i] == variables[j]:
#                 print(text[i])
#                 flag = True
#                 break
#             else:
#                 continue
#         for k in range(len(operadores)):
#             if text[i] == operadores[j]:
#                 print(text[i])
#             else:
#                 continue

for line in file:
    for character in line:
        for i in range(len(variables)):
            if character == variables[i]:
                tempText += character
                
                

                flag = True
                break

        if flag == False:
            for i in range(len(operadores)):
                if character == operadores[i]:
                    tempText += character
                    break
        flag = False
        print(tempText)




# print(text)