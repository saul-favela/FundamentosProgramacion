#Librerias
import tkinter as tk
from tkinter import scrolledtext, messagebox
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

#Funciones
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

#Botones
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

# Botones del Menu
btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)
btn1 = tk.Button(frame_botones, text="INVENTARIO", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 2 (Martes)"), **btn_style)
btn1.grid(row=0, column=1, padx=8)
btn2 = tk.Button(frame_botones, text="AGREGAR", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 2 (Martes)"), **btn_style)
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

footer = tk.Label(ventana, text="© 2025 Creative Hub Store | DÍA 1 (LUNES) - Interfaz Base y HOME",
                  font=("Helvetica", 10), bg="#f5f5f5", fg="#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()