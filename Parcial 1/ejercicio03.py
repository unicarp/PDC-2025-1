# Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
# inserte en un alista los pares y en otr alos impares
# Imprimir ambas listas y el tamaño de las mismas

import random

# Generar 100 números aleatorios entre 1 y 1000
numeros = [random.randint(1, 1000) for _ in range(100)]

# Listas para pares e impares
pares = []
impares = []

# Separar los números en pares e impares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Imprimir las listas y sus tamaños
print("Hay", len(pares), "números pares:")
print(pares)

print("\nHay", len(impares), "números impares:")
print(impares)

