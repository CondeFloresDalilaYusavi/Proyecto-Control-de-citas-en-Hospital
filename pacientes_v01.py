import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

paciente = {}
Trabajador = {}

contador = 1
contadorT = 1
def mostrar_mensaje_bienvenida():
    # Muestra un mensaje de bienvenida en el área dinámica.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="¡Bienvenido al sistema de control médico ", font=("Arial", 14)).pack(pady=10)
    

def mostrar_datos_paciente():
    # Muestra una interfaz para ingresar datos del alumno.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Información del Paciente", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre del Paciente:").pack()
    nombre_paciente = tk.Entry(area_dinamica)
    nombre_paciente.pack(pady=5)

    tk.Label(area_dinamica, text="Apellido paterno del Paciente:").pack()
    apellidoP_paciente = tk.Entry(area_dinamica)
    apellidoP_paciente.pack(pady=5)

    tk.Label(area_dinamica, text="Apellido materno del Paciente:").pack()
    apellidoM_paciente = tk.Entry(area_dinamica)
    apellidoM_paciente.pack(pady=5)

    tk.Label(area_dinamica, text="ID del Paciente:").pack()
    identificador_paciente = tk.Entry(area_dinamica)
    identificador_paciente.pack(pady=5)
    
    resultado = tk.Listbox(area_dinamica, width=80)
    resultado.pack(pady=10)    


    def guardar_datos():
        global contador
        nombre = nombre_paciente.get()
        apellidoP = apellidoP_paciente.get()
        apellidoM = apellidoM_paciente.get()
        identificador = identificador_paciente.get()

        if nombre and apellidoP and apellidoM and identificador:

            clave = f"est{contador}"
            paciente[clave] = {
                "nombre": nombre,
                "apellidoP": apellidoP,
                "apellidoM": apellidoM,
                "identificador": identificador
            }

            nombre_paciente.delete(0, tk.END)
            apellidoP_paciente.delete(0, tk.END)
            apellidoM_paciente.delete(0, tk.END)
            identificador_paciente.delete(0, tk.END)

            contador += 1

            if contador > 3:
                boton_guardar.config(state=tk.DISABLED)
                resultado.insert(tk.END, "Ya ingresaste 3 pacientes. Presiona 'Mostrar Paciente'.")

    def mostrar_datos():
        resultado.delete(0, tk.END)
        for i, est in enumerate(paciente.values(), start=1):
            texto = f"{i}. Nombre: {est['nombre']}\n Apellido Paterno: {est['apellidoP']}\n Apellido Materno: {est['apellidoM']}\n Identificador: {est['identificador']}"
            resultado.insert(tk.END, texto)

    tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datos).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar Datos", command=mostrar_datos).pack(pady=10)

 
    


def mostrar_datos_trabajador():
    # Muestra una interfaz para ingresar datos del alumno.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Información del Trabajador", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre del Trabajador:").pack()
    nombre_trabajador = tk.Entry(area_dinamica)
    nombre_trabajador.pack(pady=5)

    tk.Label(area_dinamica, text="Apellido paterno del Trabajador:").pack()
    apellidoP_trabajador = tk.Entry(area_dinamica)
    apellidoP_trabajador.pack(pady=5)

    tk.Label(area_dinamica, text="Apellido materno del Trabajador:").pack()
    apellidoM_trabajador = tk.Entry(area_dinamica)
    apellidoM_trabajador.pack(pady=5)

    tk.Label(area_dinamica, text="ID del Trabajador:").pack()
    identificador_trabajador = tk.Entry(area_dinamica)
    identificador_trabajador.pack(pady=5)

    tk.Label(area_dinamica, text="Selección rol:").pack()
    opcion_elegida = tk.StringVar(value="Médico")
    tk.Radiobutton(area_dinamica, text="Médico", variable=opcion_elegida, value="Médico").pack()
    tk.Radiobutton(area_dinamica, text="Enfermera", variable=opcion_elegida, value="Enfermera").pack()

    tk.Label(area_dinamica, text="Selección el tipo de area:").pack()
    opcion_area = tk.StringVar(value="Urgencias")
    tk.Radiobutton(area_dinamica, text="Urgencias", variable=opcion_area, value="Urgencias").pack()
    tk.Radiobutton(area_dinamica, text="Hospitalización", variable=opcion_area, value="Hospitalización").pack()
    tk.Radiobutton(area_dinamica, text="Unidad de cuidados intensivos", variable=opcion_area, value="Unidad de cuidados intensivos").pack()

    resultado = tk.Listbox(area_dinamica, width=40, height=5)
    resultado.pack(pady=5)    

    def guardar_datosT():
        global contadorT
        nombreT = nombre_trabajador.get()
        apellidoPT = apellidoP_trabajador.get()
        apellidoMT = apellidoM_trabajador.get()
        identificadorT = identificador_trabajador.get()
        rolT = opcion_elegida.get()
        areaT = opcion_area.get()

        if nombreT and apellidoPT and apellidoMT and identificadorT and rolT and areaT:

            claveT = f"est{contadorT}"
            Trabajador[claveT] = {
                "nombreT": nombreT,
                "apellidoPT": apellidoPT,
                "apellidoMT": apellidoMT,
                "identificadorT": identificadorT,
                "rolT": rolT,
                "areaT": areaT
            }

            nombre_trabajador.delete(0, tk.END)
            apellidoP_trabajador.delete(0, tk.END)
            apellidoM_trabajador.delete(0, tk.END)
            identificador_trabajador.delete(0, tk.END)
            
            contadorT += 1

            if contadorT > 3:
                boton_guardar.config(state=tk.DISABLED)
                resultado.insert(tk.END, "Ya ingresaste 3 -Trabajadores. Presiona 'Mostrar Trabajador'.")

    def mostrar_datosT():
        resultado.delete(0, tk.END)
        for i, est in enumerate(Trabajador.values(), start=1):
            texto = f"{i}. Nombre: {est['nombreT']}\n Apellido Paterno: {est['apellidoPT']}\n Apellido Materno: {est['apellidoMT']}\n Identificador: {est['identificadorT']}\n Rol: {est['rolT']}\n Area: {est['areaT']}"
            resultado.insert(tk.END, texto)

    tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datosT).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar Datos", command=mostrar_datosT).pack(pady=10)



def mostrar_areas():
    # Muestra una interfaz para ingresar datos del alumno.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Tipos de areas", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Selección el tipo de area:").pack()
    opcion_elegida = tk.StringVar(value="Urgencias")
    tk.Radiobutton(area_dinamica, text="Urgencias", variable=opcion_elegida, value="Urgencias").pack()
    tk.Radiobutton(area_dinamica, text="Hospitalización", variable=opcion_elegida, value="Hospitalización").pack()
    tk.Radiobutton(area_dinamica, text="Unidad de cuidados intensivos", variable=opcion_elegida, value="Unidad de cuidados intensivos").pack()


    def guardar_datos():
        try:
            nombre = nombre_alumno.get()
            if not nombre:
                raise ValueError("El campo de nombre no puede estar vacío.")
            messagebox.showinfo("Revisión", f"Nombre: {nombre}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datos).pack(pady=10)

def mostrar_ayuda():
    # Muestra una sección de ayuda para el usuario.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="preguntas", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)


def limpiar_area_dinamica():
     # Limpia el área dinámica para mostrar una nueva interfaz.
    for widget in area_dinamica.winfo_children():
        widget.destroy()


# Creación de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para Prácticas")
ventana_principal.geometry("500x600")
ventana_principal.config(bg="lightblue")

# Creación del menú lateral
menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

# Creación del área dinámica
area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")


# Botones del menú lateral
tk.Button(menu_lateral, text="Inicio", command=mostrar_mensaje_bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos Paciente", command=mostrar_datos_paciente, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos Empleado", command=mostrar_datos_trabajador, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Areas", command=mostrar_areas, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda", command=mostrar_ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

# Mostrar la pantalla inicial
mostrar_mensaje_bienvenida()

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()
