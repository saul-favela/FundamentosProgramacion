print("\nEjercicio 7. Operadores de comparación")

print("¿He aprobado o no la materia?")
# MAYOR O IGUAL (>=): La calificación mínima para pasar es 70
calificacion = 70
resultados = calificacion >= 70
print ("¿Aprobé?", resultados)

# MAYOR (>): La calificación mínima para pasar es 70
resultado = calificacion > 70
print("¿Aprobé?", resultados)

# Vamos a comparar estos dos números
mi_edad = 17
edad_minima = 18

# IGUAL A (==): Pregunta: ¿Los números son iguales?
resultado1 = mi_edad == 17
print("\n¿Soy mayor de edad? (==):", resultado1)

# DIFERENTE DE (1-): Pregunta: ¿Los números son diferentes?
resultado2 = mi_edad != 20
print("¿Tengo 18 años? (!=):", resultado2)

# MENOR QUE (<): Pregunta: ¿El primer número es menor?
resultado3 = mi_edad < 18
print("¿Mi edad es menor que 18? (<):", resultado3)

# MENOR O IGUAL (<=): Pregunta: ¿Es menor o igual?
resultado4 = mi_edad <= 10
print("¿Mi edad es menor o igual a 10? (<=):", resultado4)


print("\nEjercicio 8. Operadores l+ogicos")
# Imaginemos que queremos entrar a un juego online
tengo_internet = True  # Sí tengo internet
tengo_cuenta = True    # Sí tengo cuenta

# AND (y): Las DOS condiciones deben ser verdaderas
puedo_jugar = tengo_internet and tengo_cuenta
print("¿Puedo jugar? (ambas True):", puedo_jugar)

# Probemos cuando falta algo
tengo_internet2 = True
tengo_cuenta2 = False
puedo_jugar2 = tengo_internet2 and tengo_cuenta2
print("¿Puedo jugar? (una es False):", puedo_jugar2)

# OR (o): Al menos UNA condición debe ser verdadera
tengo_celular = True
tengo_tablet = False
tengo_dispositivo = tengo_celular or tengo_tablet
print("¿Tengo dispositivo? (al menos una True):", tengo_dispositivo)

# NOT (no): Invierte el valor: True se vuelve False y viceversa
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir? (NOT False = True):", puedo_salir)