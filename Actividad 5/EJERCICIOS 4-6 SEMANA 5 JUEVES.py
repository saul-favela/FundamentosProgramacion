print("\nEjercicios 1")

def calcular_likes_totales(likes_foto1, likes_foto2, likes_foto3):
    total = likes_foto1 + likes_foto2 + likes_foto3
    return total

total = calcular_likes_totales(150, 230, 89)
print(f"Tienes {total} likes en total")

total2 = calcular_likes_totales(800, 429, 300)
print(f"Tienes {total2} likes en total")


print("\nEjercicio 2\n")

def aplicar_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * porcentaje_descuento / 100
    precio_final = precio_original - descuento
    return precio_final

precio_final = aplicar_descuento(1000, 20)  #$1000 con 20% de descuento
print(f"Precio final: ${precio_final}")

precio_final2 = aplicar_descuento(500, 10)  # $500 con 10% de descuento
print(f"Precio final: ${precio_final2}")


print("\nEjercicio 3\n")

def calcular_promedio(cal1, cal2, cal3):
    suma = cal1 + cal2 + cal3
    promedio = suma / 3
    return promedio

promedio = calcular_promedio(85, 90, 78)
print(f"Tu promedio es: {promedio}")

promedio2 = calcular_promedio(100, 95, 88)
print(f"Tu promedio es: {promedio2}")