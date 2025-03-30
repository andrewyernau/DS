import matplotlib.pyplot as plt

# Datos simulados
marcas = ["Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Honor", "Realme", "POCO", "Motorola", "Nokia"]
precio_medio = [1000, 750, 550, 600, 350, 400, 350, 320, 400, 250]  # en euros
felicidad = [8.5, 8.0, 8.7, 8.2, 9.0, 8.1, 8.5, 8.3, 7.5, 7.0]  # escala 0-10

plt.figure(figsize=(10,6))
plt.scatter(precio_medio, felicidad, color='blue')

# Añadimos la etiqueta de cada marca en el gráfico
for i, marca in enumerate(marcas):
    plt.text(precio_medio[i] + 10, felicidad[i], marca, fontsize=9)

plt.xlabel("Precio medio (€)")
plt.ylabel("Valoración (Felicidad de usuarios)")
plt.title("Relación entre Precio medio y Felicidad por Marca de Teléfonos Móviles")
plt.grid(True)
plt.show()
