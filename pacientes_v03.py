import tkinter as tk
from tkinter import messagebox

class Personal:
    def _init_(self, nombre, apellidoP, apellidoM, identificador):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.identificador = identificador

CONTRASENA_CORRECTA = "admin123"
paciente = {}
Trabajador = {}
contador = 1
contadorT = 1
usuario_activo = ""

def mostrar_ventana_login():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")
    login_window.config(bg="lightgray")

    tk.Label(login_window, text="Usuario:").pack(pady=5)
    entrada_usuario = tk.Entry(login_window)
    entrada_usuario.pack(pady=5)

    tk.Label(login_window, text="Contraseña:").pack(pady=5)
    entrada_contrasena = tk.Entry(login_window, show="*")
    entrada_contrasena.pack(pady=5)

    def validar_login():
        global usuario_activo
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()
        if contrasena == CONTRASENA_CORRECTA:
            usuario_activo = usuario
            login_window.destroy()
            mostrar_ventana_principal()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    tk.Button(login_window, text="Ingresar", command=validar_login).pack(pady=10)
    login_window.mainloop()

def mostrar_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Control de Citas")
    ventana_principal.geometry("500x600")
    ventana_principal.config(bg="lightblue")

    menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
    menu_lateral.pack(side="left", fill="y")

    area_dinamica = tk.Frame(ventana_principal, bg="white")
    area_dinamica.pack(side="right", expand=True, fill="both")

    def limpiar_area_dinamica():
        for widget in area_dinamica.winfo_children():
            widget.destroy()

    def mostrar_mensaje_bienvenida():
        limpiar_area_dinamica()
        tk.Label(area_dinamica, text=f"¡Bienvenido, {usuario_activo}!", font=("Arial", 14)).pack(pady=10)

    def mostrar_datos_paciente():
        global contador
        limpiar_area_dinamica()
        tk.Label(area_dinamica, text="Información del Paciente", font=("Arial", 14)).pack(pady=10)

        nombre_paciente = tk.Entry(area_dinamica)
        apellidoP_paciente = tk.Entry(area_dinamica)
        apellidoM_paciente = tk.Entry(area_dinamica)
        identificador_paciente = tk.Entry(area_dinamica)
        cama_paciente = tk.Entry(area_dinamica)

        for texto, entry in [
            ("Nombre del Paciente:", nombre_paciente),
            ("Apellido paterno del Paciente:", apellidoP_paciente),
            ("Apellido materno del Paciente:", apellidoM_paciente),
            ("ID del Paciente:", identificador_paciente),
            ("Cama:", cama_paciente)
        ]:
            tk.Label(area_dinamica, text=texto).pack()
            entry.pack(pady=5)

        resultado = tk.Listbox(area_dinamica, width=60, height=5)
        resultado.pack(pady=10)

        def guardar_datos():
            global contador
            nombre = nombre_paciente.get()
            apellidoP = apellidoP_paciente.get()
            apellidoM = apellidoM_paciente.get()
            identificador = identificador_paciente.get()
            cama = cama_paciente.get()

            if nombre and apellidoP and apellidoM and identificador and cama:
                clave = f"est{contador}"
                paciente[clave] = {
                    "nombre": nombre,
                    "apellidoP": apellidoP,
                    "apellidoM": apellidoM,
                    "identificador": identificador,
                    "cama": cama
                }

                for e in [nombre_paciente, apellidoP_paciente, apellidoM_paciente, identificador_paciente, cama_paciente]:
                    e.delete(0, tk.END)

                contador += 1

                if contador > 3:
                    boton_guardar.config(state=tk.DISABLED)
                    resultado.insert(tk.END, "Ya ingresaste 3 pacientes. Presiona 'Mostrar Datos'.")

        def mostrar_datos():
            resultado.delete(0, tk.END)
            for i, est in enumerate(paciente.values(), start=1):
                texto = f"{i}. Nombre: {est['nombre']}\nApellido Paterno: {est['apellidoP']}\nApellido Materno: {est['apellidoM']}\nIdentificador: {est['identificador']}\nCama: {est['cama']}"
                resultado.insert(tk.END, texto)

        boton_guardar = tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datos)
        boton_guardar.pack(pady=10)
        tk.Button(area_dinamica, text="Mostrar Datos", command=mostrar_datos).pack(pady=10)

    def mostrar_datos_trabajador():
        global contadorT
        limpiar_area_dinamica()
        tk.Label(area_dinamica, text="Información del Trabajador", font=("Arial", 14)).pack(pady=10)

        nombre_trabajador = tk.Entry(area_dinamica)
        apellidoP_trabajador = tk.Entry(area_dinamica)
        apellidoM_trabajador = tk.Entry(area_dinamica)
        identificador_trabajador = tk.Entry(area_dinamica)

        for texto, entry in [
            ("Nombre del Trabajador:", nombre_trabajador),
            ("Apellido paterno del Trabajador:", apellidoP_trabajador),
            ("Apellido materno del Trabajador:", apellidoM_trabajador),
            ("ID del Trabajador:", identificador_trabajador)
        ]:
            tk.Label(area_dinamica, text=texto).pack()
            entry.pack(pady=5)

        tk.Label(area_dinamica, text="Selección rol:").pack()
        opcion_elegida = tk.StringVar(value="Médico")
        tk.Radiobutton(area_dinamica, text="Médico", variable=opcion_elegida, value="Médico").pack()
        tk.Radiobutton(area_dinamica, text="Enfermera", variable=opcion_elegida, value="Enfermera").pack()

        tk.Label(area_dinamica, text="Selección el tipo de área:").pack()
        opcion_area = tk.StringVar(value="Urgencias")
        for area in ["Urgencias", "Hospitalización", "Unidad de cuidados intensivos"]:
            tk.Radiobutton(area_dinamica, text=area, variable=opcion_area, value=area).pack()

        resultado = tk.Listbox(area_dinamica, width=60, height=5)
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

                for e in [nombre_trabajador, apellidoP_trabajador, apellidoM_trabajador, identificador_trabajador]:
                    e.delete(0, tk.END)

                contadorT += 1

                if contadorT > 3:
                    boton_guardar.config(state=tk.DISABLED)
                    resultado.insert(tk.END, "Ya ingresaste 3 Trabajadores. Presiona 'Mostrar Datos'.")

        def mostrar_datosT():
            resultado.delete(0, tk.END)
            for i, est in enumerate(Trabajador.values(), start=1):
                texto = f"{i}. Nombre: {est['nombreT']}\nApellido Paterno: {est['apellidoPT']}\nApellido Materno: {est['apellidoMT']}\nIdentificador: {est['identificadorT']}\nRol: {est['rolT']}\nÁrea: {est['areaT']}"
                resultado.insert(tk.END, texto)

        boton_guardar = tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datosT)
        boton_guardar.pack(pady=10)
        tk.Button(area_dinamica, text="Mostrar Datos", command=mostrar_datosT).pack(pady=10)

    def mostrar_areas():
        limpiar_area_dinamica()
        tk.Label(area_dinamica, text="Tipos de áreas", font=("Arial", 14)).pack(pady=10)

        tk.Label(area_dinamica, text="Seleccione el tipo de área:").pack()
        opcion_elegidaA = tk.StringVar(value="Urgencias")
        for area in ["Urgencias", "Hospitalización", "Unidad de cuidados intensivos"]:
            tk.Radiobutton(area_dinamica, text=area, variable=opcion_elegidaA, value=area).pack()

        resultado = tk.Listbox(area_dinamica, width=60, height=5)
        resultado.pack(pady=5)

        def mostrar_datosA():
            resultado.delete(0, tk.END)
            for i, est in enumerate(Trabajador.values(), start=1):
                if est["areaT"] == opcion_elegidaA.get():
                    texto = f"{i}. Nombre: {est['nombreT']}\nApellido Paterno: {est['apellidoPT']}\nApellido Materno: {est['apellidoMT']}\nIdentificador: {est['identificadorT']}\nRol: {est['rolT']}\nÁrea: {est['areaT']}"
                    resultado.insert(tk.END, texto)

        tk.Button(area_dinamica, text="Mostrar Datos", command=mostrar_datosA).pack(pady=10)

    def mostrar_camas():
        limpiar_area_dinamica()
        tk.Label(area_dinamica, text="Estados de Camas", font=("Arial", 14)).pack(pady=10)

        tk.Label(area_dinamica, text="Número de cama:").pack()
        camaP = tk.Entry(area_dinamica)
        camaP.pack(pady=5)

        resultado = tk.Listbox(area_dinamica, width=60, height=5)
        resultado.pack(pady=5)

        def mostrar_datosC():
            resultado.delete(0, tk.END)
            ocupada = "NO"
            for i, est in enumerate(paciente.values(), start=1):
                if est["cama"] == camaP.get():
                    texto = f"{i}. Nombre: {est['nombre']}\nApellido Paterno: {est['apellidoP']}\nApellido Materno: {est['apellidoM']}\nIdentificador: {est['identificador']}\nCama: {est['cama']}"
                    resultado.insert(tk.END, texto)
                    ocupada = "SI"
            if ocupada == "NO":
                resultado.insert(tk.END, "Cama desocupada")

        tk.Button(area_dinamica, text="Mostrar Datos", command=mostrar_datosC).pack(pady=10)


    tk.Button(menu_lateral, text="Inicio", command=mostrar_mensaje_bienvenida, width=15).pack(pady=10)
    tk.Button(menu_lateral, text="Datos Paciente", command=mostrar_datos_paciente, width=15).pack(pady=10)
    tk.Button(menu_lateral, text="Datos Empleado", command=mostrar_datos_trabajador, width=15).pack(pady=10)
    tk.Button(menu_lateral, text="Áreas", command=mostrar_areas, width=15).pack(pady=10)
    tk.Button(menu_lateral, text="Camas", command=mostrar_camas, width=15).pack(pady=10)
    tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

    mostrar_mensaje_bienvenida()
    ventana_principal.mainloop()


mostrar_ventana_login()
