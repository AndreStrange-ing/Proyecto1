import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from collections import Counter

# Lista global de encuestas
encuestas = []

# Utilidad para obtener nombres de encuestas
def nombres_encuestas():
    return [e["nombre"] for e in encuestas]

# Crear Encuesta 
def ventana_crear_encuesta(parent):
    win = tk.Toplevel(parent)
    win.title("Crear Encuesta")
    win.geometry("500x400")
    win.configure(bg="black")

    tk.Label(win, text="Nombre de la encuesta:", fg="white", bg="black").pack(padx=10, pady=(10,0), anchor="w")
    entry_nombre = tk.Entry(win, bg="#222222", fg="white", insertbackground="white")
    entry_nombre.pack(fill="x", padx=10, pady=6)

    tk.Label(win, text="Agregar pregunta:", fg="white", bg="black").pack(padx=10, pady=(6,0), anchor="w")
    entry_pregunta = tk.Entry(win, bg="#222222", fg="white", insertbackground="white")
    entry_pregunta.pack(fill="x", padx=10, pady=6)

    listbox = tk.Listbox(win, bg="#222222", fg="white", selectbackground="#555555")
    listbox.pack(fill="both", expand=True, padx=10, pady=6)

    preguntas_temp = []

    def agregar_pregunta():
        texto = entry_pregunta.get().strip()
        if texto == "":
            messagebox.showinfo("Información", "La pregunta está vacía")
            return
        preguntas_temp.append(texto)
        listbox.insert(tk.END, texto)
        entry_pregunta.delete(0, tk.END)

    def eliminar_pregunta():
        sel = listbox.curselection()
        if not sel:
            messagebox.showinfo("Información", "Seleccione una pregunta para eliminar")
            return
        idx = sel[0]
        listbox.delete(idx)
        preguntas_temp.pop(idx)

    def guardar_encuesta():
        nombre = entry_nombre.get().strip()
        if nombre == "":
            messagebox.showinfo("Información", "Ingrese un nombre para la encuesta")
            return
        encuesta = {"nombre": nombre, "preguntas": []}
        for i, p in enumerate(preguntas_temp, start=1):
            encuesta["preguntas"].append({f"pregunta{i}": p, "respuestas": []})
        encuestas.append(encuesta)
        messagebox.showinfo("Listo", f"Encuesta '{nombre}' creada con éxito")
        win.destroy()

    frame_botones = tk.Frame(win, bg="black")
    frame_botones.pack(fill="x", padx=10, pady=6)
    tk.Button(frame_botones, text="Agregar Pregunta", command=agregar_pregunta, bg="#333333", fg="white").pack(side="left", padx=5)
    tk.Button(frame_botones, text="Eliminar Pregunta", command=eliminar_pregunta, bg="#333333", fg="white").pack(side="left", padx=5)
    tk.Button(frame_botones, text="Guardar Encuesta", command=guardar_encuesta, bg="#333333", fg="white").pack(side="right", padx=5)

# Registrar Respuestas 
def ventana_responder_encuesta(parent):
    if not encuestas:
        messagebox.showinfo("Información", "No hay encuestas disponibles")
        return

    win = tk.Toplevel(parent)
    win.title("Responder Encuesta")
    win.geometry("600x500")
    win.configure(bg="black")

    tk.Label(win, text="Seleccione la encuesta:", fg="white", bg="black").pack(fill="x", padx=10, pady=(10,0))
    cmb_encuestas = ttk.Combobox(win, values=nombres_encuestas(), state="readonly")
    cmb_encuestas.pack(fill="x", padx=10, pady=6)
    cmb_encuestas.current(0)

    tk.Label(win, text="Nombre del usuario:", fg="white", bg="black").pack(fill="x", padx=10, pady=(6,0))
    entry_usuario = tk.Entry(win, bg="#222222", fg="white", insertbackground="white")
    entry_usuario.pack(fill="x", padx=10, pady=6)

    frame_preg = tk.Frame(win, bg="black")
    frame_preg.pack(fill="both", expand=True, padx=10, pady=6)

    canvas = tk.Canvas(frame_preg, bg="black")
    scrollbar = tk.Scrollbar(frame_preg, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas, bg="black")
    canvas.create_window((0,0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    respuestas_entries = []

    def cargar_preguntas(event=None):
        for w in inner.winfo_children():
            w.destroy()
        respuestas_entries.clear()
        idx = cmb_encuestas.current()
        encuesta = encuestas[idx]
        for j, preg in enumerate(encuesta["preguntas"], start=1):
            tk.Label(inner, text=f"{j}. {preg[f'pregunta{j}']}", fg="white", bg="black", anchor="w", wraplength=560).pack(fill="x", pady=(6,0))
            ent = tk.Entry(inner, bg="#222222", fg="white", insertbackground="white")
            ent.pack(fill="x", pady=(2,0))
            respuestas_entries.append(ent)

    cargar_preguntas()
    cmb_encuestas.bind("<<ComboboxSelected>>", cargar_preguntas)

    def guardar_respuestas():
        usuario = entry_usuario.get().strip()
        if usuario == "":
            messagebox.showinfo("Información", "Ingrese su nombre")
            return
        idx = cmb_encuestas.current()
        encuesta = encuestas[idx]
        for k, ent in enumerate(respuestas_entries):
            resp = ent.get().strip()
            encuesta["preguntas"][k]["respuestas"].append({usuario: resp})
        messagebox.showinfo("Listo", "Respuestas registradas correctamente")
        entry_usuario.delete(0, tk.END)
        for ent in respuestas_entries:
            ent.delete(0, tk.END)

    tk.Button(win, text="Guardar Respuestas", bg="#333333", fg="white", command=guardar_respuestas).pack(pady=6)

# Mostrar Resultados 
def ventana_resultados(parent):
    if not encuestas:
        messagebox.showinfo("Información", "No hay encuestas disponibles")
        return

    win = tk.Toplevel(parent)
    win.title("Resultados")
    win.geometry("650x500")
    win.configure(bg="black")

    tk.Label(win, text="Seleccione la encuesta:", fg="white", bg="black").pack(fill="x", padx=10, pady=(10,0))
    cmb = ttk.Combobox(win, values=nombres_encuestas(), state="readonly")
    cmb.pack(fill="x", padx=10, pady=6)
    cmb.current(0)

    txt = tk.Text(win, bg="#222222", fg="white", insertbackground="white")
    txt.pack(fill="both", expand=True, padx=10, pady=6)

    def mostrar():
        txt.delete("1.0", tk.END)
        idx = cmb.current()
        encuesta = encuestas[idx]
        txt.insert(tk.END, f"Encuesta: {encuesta['nombre']}\n\n")
        if not encuesta["preguntas"]:
            txt.insert(tk.END, "No hay preguntas registradas\n")
            return
        for j, preg in enumerate(encuesta["preguntas"], start=1):
            txt.insert(tk.END, f"{j}. {preg[f'pregunta{j}']}\n")
            if preg["respuestas"]:
                for k, r in enumerate(preg["respuestas"], start=1):
                    for usuario, resp in r.items():
                        txt.insert(tk.END, f"   {k}. Usuario: {usuario} - Respuesta: {resp}\n")
            else:
                txt.insert(tk.END, "   Sin respuestas\n")
            txt.insert(tk.END, "-"*30 + "\n")

    mostrar()
    cmb.bind("<<ComboboxSelected>>", lambda e: mostrar())

#  Menu Principal 
def main():
    root = tk.Tk()
    root.title("Sistema de Encuestas Dinámico")
    root.geometry("600x400")
    root.configure(bg="black")

    tk.Label(root, text="Bienvenido al Sistema de Encuestas", fg="white", bg="black", font=("Comic Sans MS", 14)).pack(pady=10)

    tk.Button(root, text="Crear Encuesta", width=25, command=lambda: ventana_crear_encuesta(root), bg="#333333", fg="white").pack(pady=6)
    tk.Button(root, text="Responder Encuesta", width=25, command=lambda: ventana_responder_encuesta(root), bg="#333333", fg="white").pack(pady=6)
    tk.Button(root, text="Mostrar Resultados", width=25, command=lambda: ventana_resultados(root), bg="#333333", fg="white").pack(pady=6)

    tk.Button(root, text="Salir", width=25, command=root.destroy, bg="#333333", fg="white").pack(pady=6)

    root.mainloop()


main()