import string
import random

minusculas_ascii = string.ascii_lowercase
print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
print(mayusculas_ascii)

numeros = string.digits
print(numeros)

print("Contraseñas:\n")


def generarPassword(n):
    password = []
    for i in range(n):
        #Escoger entre las tres listas
        op = random.randint(1,3)
        #Escoger para cada lista
        if(op == 1):
            op = random.randint(0,25)
            password.append(minusculas_ascii[op])
        elif(op == 2):
            op = random.randint(0,25)
            password.append(mayusculas_ascii[op])
        else:
            op = random.randint(0,9)
            password.append(numeros[op])
    
    passFinal = "".join(password)
    return passFinal

for i in range(10, 20):
    print(i+1,"caracteres: ",generarPassword(i),"\n")