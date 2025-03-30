mi_lista = ["data", "machine learning", "stats", "ia"]
print(mi_lista[1:3])
print(mi_lista[1:3:2])
mi_lista.append("ids")
print(mi_lista)
mi_lista.remove("ids")
mi_lista_copia = mi_lista
mi_lista[0]="CAMBIO"
print(mi_lista)
print(mi_lista_copia)
mi_lista = ["data", "machine learning", "stats", "ia"]
mi_lista_copia2 = mi_lista.copy()
mi_lista[0]="CAMBIO"
print(mi_lista)
print(mi_lista_copia2)


personas = {
    "Antonio" :23,
    "Kayne West" : 88
}
for nombre,edad in personas.items():
    print(f"{nombre} tiene {edad} años")

for nombre in personas.keys():
    print(nombre)

for edad in personas.values():
    print(edad)