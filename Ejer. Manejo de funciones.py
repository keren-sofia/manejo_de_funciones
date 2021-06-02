'''
Realizar una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares
Para la solución de este problema, se requiere que el usuario 
escriba un script y defina una función llamada separar(). 
Como parámetro de entrada recibe una lista de numero de enteros. 
La lista debe crearla como lista=[1,2,3,4]. La función devuelve 
dos listas de la forma: lista1=[Numeros pares], 
lista2=[numeros impares]
'''
num = [-12, 84, 13, 20, -33, 101, 9]
def separar(lista): #Establecer la función
    num.sort() # Función Sort organiza
    pares = []
    impares = []
    for n in num:
        if n%2 == 0:
            pares.append(n) # Función Append agrega al final de la lista 
        else:
            impares.append(n) 
    return pares, impares

pares, impares = separar(num)
print(pares)
print(impares)