print("\nEjercicio 1\n")

# Escribe tu función aquí
def mostrar_perfil():
    print("Usuario: @taylorswift")
    print("Seguidores: 1.2b")
    print("Bio: Cantante")

# Pruébala (llámala 2 veces)
mostrar_perfil()
print()  # Línea en blanco para separar
mostrar_perfil()


print("\nEjercicio 2\n")

# Escribe tu función aquí
def calcular_horas_tiktok(minutos_por_dia):
    minutos_totales = minutos_por_dia * 7
    horas_totales = minutos_totales / 60
    return horas_totales

# Pruébala con diferentes valores
horas = calcular_horas_tiktok(30)  # 30 minutos por día
print(f"Ves {horas} horas de Tiktok a la semana")

horas2 = calcular_horas_tiktok(60)  # 60 minutos por día
print(f"Ves {horas2} horas de Tiktok a la semana")


print("\nEjercicio 3\n")

# Escribe tu función aquí
def puedo_comprar(dinero_que_tengo, precio_producto):
    if dinero_que_tengo >= precio_producto:
        return "Sí puedes comprobarlo"
    else:
        return "No te alcanza"
    
# Pruébala con diferentes casos
resultado1 = puedo_comprar(500, 300)  # Tengo $500, cuesta $300
print(f"Tenis nuevos: {resultado1}")

resultado2 = puedo_comprar(150, 800)  # Tengo $150, cuesta $800
print(f"Celular nuevo: {resultado2}")

resultado3 = puedo_comprar(100, 100)  # Tengo $100, cuesta $100
print(f"Aud+ifonos: {resultado3}")