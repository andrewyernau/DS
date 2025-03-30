def calculate_discount(price, reduction):
    discounted_price = price * (1 - reduction)
    return discounted_price

ejemplo_descuento = calculate_discount(120,0.2)
print(f"El precio despues del desucento es {ejemplo_descuento}")

import numpy as np

x =  np.arange(10)
print(x)
print(type(x))

lst=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"La media de {lst} no se puede hacer, pero con numpy, sí y es: {x.mean()}")
print(f"Algunos de sus atributos pueden ser size {x.size} o directorio {dir(x)} o el cumsum {x.cumsum}...")