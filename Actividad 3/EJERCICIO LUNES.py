# Ejercicio 1
# SALIDA - Bienvenida
print("=" * 45)
print("BIENVENIDO A GAME STORE")
print("=" * 45)
print()

# ENTRADA - Datos del cliente
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
# PROCESAMIENTO - Precios fijos de los juegos
precio_fifa = 899.00
precio_cod = 1299.00
precio_hello_kitty = 599.00

# SALIDA - Catálogo de productos
print("-------  CATÁLOGO DE PRODUCTOS -------")
print("1. FIFA 2025 - $" + str(precio_fifa))
print("2. Call ofnDuty - $" + str(precio_cod))
print("3. Hello Kitty Island Adventure - $" + str(precio_hello_kitty))
print()

# ENTRADA - Cantidad de cada juego
cantidad_fifa = float(input("¿Cuántos FIFA 2025 quieres?"))
cantidad_cod = float(input("¿Cuántos Call of Duty quieres?"))
cantidad_hello_kitty = float(input("¿Cuántos Hello Kitty Island Adventure quieres"))

# PROCESAMIENTO - Cálculos por juego
total_fifa = precio_fifa * cantidad_fifa
total_cod = precio_cod * cantidad_cod
total_hello_kitty = precio_hello_kitty * cantidad_hello_kitty

# PROCESAMIENTO - Cálculos totales
subtotal = total_fifa + total_cod + total_hello_kitty
iva = subtotal * 0.16
total = subtotal + iva

# PROCESAMIENTO - Cantidad total de juegos
cantidad_total = cantidad_fifa + cantidad_cod + cantidad_hello_kitty

# PROCESAMIENTO - Crear ticket
print("TICKET DE COMPRA")
print("=" * 45)
print("Cliente: " + nombre)
print("Edad: " + str(edad) + " años")
print("=" * 45)
print("DETALLE DE COMPRA:")
print("FIFA 2025:")
print("  Cantidad:  " + str(cantidad_fifa))
print("  Precio unitario: $" + str(precio_fifa))
print("  Total: $" + str(total_fifa))
print("Call of Duty:")
print("  Cantidad: " + str(cantidad_cod))
print("  Precio unitario: $" + str(precio_cod))
print("  Total: $" + str(total_cod))
print("Hello Kitty Island Adventure:")
print("  Cantidad: " + str(cantidad_hello_kitty))
print("  Precio unitario: $" + str(precio_hello_kitty))
print("  Total: $" + str(total_hello_kitty))
print("=" * 45)
print("Cantidad total de juegos: " + str(cantidad_total))
print("Subtotal: $" + str(subtotal))
print("IVA (16%): $" + str(iva))
print("=" * 45)
print("TOTAL A PAGAR: $" + str(total))
print()
# SALIDA - Mensaje de despedida
print("¡Gracias por tu compra, " + nombre + "!")