#Primer script test
# ayn 10/02/2025

print("Hello world!")

x = 3.2
print(type(x))

y = (x > 3)
print(type(y))

#Coleciones de elementos: listas,tuplas...
x = [2.31, True, 4, "Sexo nigga"]
print(x)
print(x[0])
print(x[3])
print(x[-1])

print("Cambiamos elemento 1 de la lista!")
x[1] = False
print(x[1])

x = (2.31, True, 4, "Sexo nigga")
print(x)
print(x[0])
print(x[3])
print(x[-1])

print("Cambiamos elemento 1 de la tupla! = ERROR, NO es mutable (alterable) una tupla")
# x[1] = False
print(x[1])

A = {2, 4, 6} #Elms unicos, no duplicados
B = {3, 4, 5, 6}
S = {1, 2, 3, 4, 5, 6}

print(A | B)
print(A & B)
print(S - B)
#Metodos
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.add(7))
print(A)
print(A.pop())
print(A)

primer_elemento = A.pop()
print(primer_elemento)
#Diccionarios, CLAVE: VALOR

dict = {
    "Nigga": 69,
    "Balls": 420,
    "Kayne West": {
        "twitter": "hitler",
        "number": 88
    }
}
print(dict)
print(dict["Kayne West"]["number"])

mi_cadena = "HELLO"
print(mi_cadena)
mi_cadena = "hello"
print(mi_cadena)
mi_cadena = ''' hello, esto es una cadena
que recorre varias lineas porque es mu larga illo'''
print(mi_cadena)


#I/O

n = input("Numero de casos")
print(n)
print(type(n))
n = int(n)
print(n+10)

x = [2.31, True, 4, "Sexo nigga"]
for element in x:
    print (element, end=" ")

for i in (0, 1, 2, 3, 4, 5, 6):
    j = 2 * i
    suma = suma + j
print(suma)
for i in range(7):
    j = 2 * i
    suma += j
print("la suma es:"+str(suma))
print(f"El resultado es {suma}") #<-- La forma más comoda de poder hacer print sobre variables ya que no hay que usar el signo