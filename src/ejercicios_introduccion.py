# Andre 10/02/2025
import math
n_stg = input("Introduce un numero entero: ")
i = int(n_stg)
lista = []
sum = 0

print(f"-------------------SUCESSIÓN CON {i}---------------------")
for count in range(i) :
    op = 4 * (math.pow(-1,count))/(2 * count + 1)
    count = count + 1
    sum = sum + op  
    lista.append(op)
    count = count + 1

print(f"El resultado final de la sucesión es {lista} y su suma es {sum}")
print(f"-------------------LA TABLA DE MULTIPLICACIÓN DEL NÚMERO {i}---------------------")
for count in range(11):
    print(f"-> {i} * {count} = {i*count}")
print(f"-------------------PATRÓN TRIÁNGULO {i}---------------------")
out_str = ""
for count in range(i):
    i_strg = str(count + 1)
    out_str += " "
    out_str += i_strg
    print(out_str)

print(f"-------------------COMPROBAR PRIMO {i}---------------------")
nums = 0
for count in range(2,i):
    if nums > 0:
        print(f"No es primo {i}")
        break;
    if (i % (count+1) == 0):
        nums =+ 1

    else:
        print(f"Es primo {i}")
      

print(f"-------------------COMPROBAR PRIMO CON FUNCIÓN {i}---------------------")

def prime_checker(integer):
    if integer <= 1:
        return False 
    for i in range(2, int(integer**0.5) + 1):
        if integer % i == 0:
            return False
    return True
print(f"El numero {i} es primo: {prime_checker(i)}")

print(f"-------------------LISTA DE PRIMOS CON FUNCIÓN HASTA{i}---------------------")

def prime_list_i(integer):
    prime_list = []
    for i in range(integer-1):
        i_bool = prime_checker(i)
        if i_bool:
            prime_list.append(i)
    return prime_list
print(f"El numero {i} contiene los siguientes primos: {prime_list_i(i)}")

print("-------------------CONSTRUIR ESPERANZA DE VIDA---------------------")
personas = {
    'Pedro': 28,
    'María': 21,
    'Marta': 22
}

esperanza_adicional = {
    28: 53.4,
    21: 65.6,
    22: 64.5
}

nueva_esperanza = {nombre: (edad + esperanza_adicional.get(edad)) for nombre, edad in personas.items()}

print(nueva_esperanza)