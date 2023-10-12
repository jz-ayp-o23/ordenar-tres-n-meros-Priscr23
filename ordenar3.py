"""
Diseña un programa para ordenar tres números de mayor a menor.
750722
"""

#Entradas
n_1 = input("Introduzca un número: ")
n_2 = input("Introduzca un segundo número: ")
n_3 = input("Introduzca un tercer número: ")

#Procesos
numeros = [n_1, n_2, n_3]
numeros.sort(reverse=True)

#Salida
print("Números ordenados:", numeros)



