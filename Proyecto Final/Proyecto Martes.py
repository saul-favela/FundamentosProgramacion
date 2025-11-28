import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog  # Dia 2 agregamos simpledialog
from datetime import datetime

# Inventario Inicial incluye 10 productos
inventario = [
    {"id": "001", "producto": "Set boceto", "marca": "Joyway",
     "precio": 860.0, "stock": 15, "descripcion": "Dibujo versátil"},
    {"id": "002", "producto": "Set grafito", "marca": "Castle Arts",
     "precio": 640.0, "stock": 3, "descripcion": "Sombras variadas"},
    {"id": "003", "producto": "Marcadores acuarela", "marca": "Colorbrush",
     "precio": 535.0, "stock": 17, "descripcion": "Trazo líquido"},
    {"id": "004", "producto": "Combo lápiz + acuarela", "marca": "Barrilito",
     "precio": 2100.0, "stock": 11, "descripcion": "Kit portátil"},
    {"id": "005", "producto": "Kit dibujo", "marca": "Artistas",
     "precio": 1200.0, "stock": 9, "descripcion": "Set completo"},
    {"id": "006", "producto": "Lápices acuarela pequeños", "marca": "Elseware",
     "precio": 890.0, "stock": 16, "descripcion": "Dibujo versátil"},
    {"id": "007", "producto": "Set acuarela de viaje", "marca": "Castle Arts",
     "precio": 370.0, "stock": 18, "descripcion": "Portable acuarela"},
    {"id": "008", "producto": "Lápices acuarela", "marca": "Artline",
     "precio": 28.0, "stock": 26, "descripcion": "Micropunta acuarela"},
    {"id": "009", "producto": "Lápices supracolor", "marca": "Caran d'Ache",
     "precio": 75.0, "stock": 29, "descripcion": "Color profesional"},
    {"id": "010", "producto": "Set pinturas + libro", "marca": "Crayola",
     "precio": 370.0, "stock": 15, "descripcion": "Creatividad infantil"},
]

historial_ventas = []
STOCK_MINIMO = 3
# dia 1
def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida con estadísticas rápidas"""
    global boton_activado
    texto.delete(1.0, tk.END)
    activar_boton(btn_home)

    total_modelos = len(inventario)
    total_pares = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(1 for v in historial_ventas if datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M").date() == datetime.now().date())
    productos_stock_bajo = sum(1 for t in inventario if t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "------------------------------------------------\n\n")
    texto.insert(tk.END, "   Bienvenido a Creative Hub Store   \n\n")
    texto.insert(tk.END, "------------------------------------------------\n\n")

    texto.insert(tk.END, "RESUMEN RÁPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"Modelos Únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total de productos en Stock: {total_pares}\n")
    texto.insert(tk.END, f"Ventas Registradas (Hoy): {ventas_hoy}\n")

    if productos_stock_bajo > 0:
        texto.insert(tk.END, f"¡ALERTA DE STOCK BAJO!: {productos_stock_bajo} productos necesitan reabastecimiento\n", "alerta")
    else:
        texto.insert(tk.END, "¡Inventario en buen estado!\n")

    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")

# dia 2
def validar_numero_positivo(valor, nombre_campo):
    """Valida que el valor sea un número positivo."""
    try:
        num = float(valor)
        if num < 0:
            messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' no puede ser negativo.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' debe ser un número válido.")
        return None
    
# dia 2
def generar_nuevo_id():
    """Generar un nuevo ID consecutivo basado en el ID númerico más alto actual."""
    if not inventario:
        return "001"
    
    max_id = 0
    for productos in inventario:
        try:
            num_id = int(productos['id'])
            if num_id > max_id:
                max_id = num_id
        except ValueError:
            continue

    return str(max_id + 1).zfill(3)

# dia 2
def mostrar_inventario():
    """Muestra el listado completo del inventario."""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "= INVENTARIO COMPLETO =\n\n")
    activar_boton(btn1)

    if not inventario:
        texto.insert(tk.END, "X No hay productos en el inventario\n")
    else:
        texto.insert(tk.END, f"{'ID':<4} | {'PRODUCTO':<25} | {'PRECIO':<10} | {'MARCA':<10} | {'STOCK':<5}\n")
        texto.insert(tk.END, "-"*70 + "\n")

        for productos in inventario:
            linea = f"{productos['id']:<4} | {productos['producto']:<25} | ${productos['precio']:<9,.0f} | {productos['marca']:<10} | {productos['stock']:<5}"
            texto.insert(tk.END, linea)

            if productos['stock'] > 0 and productos['stock'] <= STOCK_MINIMO:
                texto.insert(tk.END, "STOCK BAJO", "alerta")
            elif productos['stock'] == 0:
                texto.insert(tk.END, "AGOTADO", "agotado")

            texto.insert(tk.END, "\n")

        texto.insrt(tk.END, "\nUsa el botón 'AGREGAR' para incorporar nuevos productos.\n")

# dia 2
def agregar_productos():
    """Agregar un nuevo producto al inventario."""
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    producto = simpledialog.askstring("Agregar Productos", "1. Nombre del producto (Obligatorio):", parent=ventana)
    if not producto: return

    marca = simpledialog.askstring("Agregar Productoss", "2. Marca/Categoría (Obligatorio):", parent=ventana)
    if not marca: return

    precio_str = simpledialog.askstring("Agregar Productos", "3. Precio unitario (Obligatorio)", parent=ventana)
    if not precio_str: return
    precio_validado = validar_numero_positivo(precio_str, "Precio")
    if precio_validado is None: return

    stock_str = simpledialog.askstring("Agregar Productos", "4. Cantidad inicial (Stock) (Obligatorio):", parent=ventana)
    if not stock_str: return
    stock_validado = validar_numero_positivo(stock_str, "Cantidad inicial")
    if stock_validado is None: return

    descripcion = simpledialog.askstring("Agregar Productos", "5. Descripción adicional (Opcional):", parent=ventana)

    nuevos_productos = {
        "id": new_id,
        "producto": producto,
        "marca": marca,
        "precio": float(precio_validado),
        "stock": int(stock_validado),
        "descripción": descripcion if descripcion else "Sin descripción"
    }

    inventario.append(nuevos_productos)

    messagebox.showinfo("Éxito", f"'{producto}' agregado con ID {new_id} al inventario.")
    mostrar_inventario()

def activar_boton(boton):
    """Actualiza el color del botón activo"""
    global boton_activo

    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg="#060270")

    if boton:
        boton.config(bg="#3832D6")
        boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg="#3832D6")

def on_leave(e, boton):
    if boton != boton_activo:
        boton.config(bg="#060270")

#Parte grafica
ventana = tk.Tk()
ventana.title(" Creative Hub Store ")
ventana.geometry("1200x800")
ventana.configure(bg="#f5f5f5")

boton_activo = None

titulo = tk.Label(ventana, text="🎨CREATIVE HUB STORE🎨",
                  font=("Helvetica", 32, "bold"), bg="#f5f5f5", fg="#060270")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS",
                     font=("Helvetica", 12), bg="#f5f5f5", fg="#666666")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)

btn_style = {"font": ("Albert Sans", 11, "bold"), "bg": "#000000", "fg": "white",
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

# dia 2
btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)

# dia 2
btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn1.grid(row=0, column=1, padx=8)

# dia 2
btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_productos, **btn_style)
btn2.grid(row=0, column=2, padx=8)

btn3 = tk.Button(frame_botones, text="VENDER", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 3 (Miércoles)"), **btn_style)
btn3.grid(row=0, column=3, padx=8)
btn4 = tk.Button(frame_botones, text="BUSCAR", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 3 (Miércoles)"), **btn_style)
btn4.grid(row=0, column=4, padx=8)

for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

texto = scrolledtext.ScrolledText(ventana,
                                      font=("Open Sans", 11),
                                      bg="#ffffff", fg="#060270",
                                      height=18,
                                      padx=20, pady=20,
                                      relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground="#060270")
texto.tag_config("alerta", background="#ffe5e5", foreground="#E25556", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", background="#fddede", foreground="#E23436", font=("Open Sans", 11, "bold"))

# dia 2
footer = tk.Label(ventana, text="© 2025 Creative Hub Store | DÍA 2 (MARTES) - Boton Inventario y Agregar Productos",
                  font=("Helvetica", 10), bg="#f5f5f5", fg="#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()