import tkinter as tk
from tkinter import messagebox

# Crear ventana principal y configurar el fondo
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")
root.configure(bg="#2E2E2E")  # Fondo gris oscuro para la ventana

# Funciones de la aplicación
def add_task():
    task = task_input.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Escribe una tarea antes de añadir.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def mark_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, f"{task} ✔")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar.")

# Crear widgets con colores personalizados
task_input = tk.Entry(root, width=35, font=('Arial', 12), bg="#444444", fg="#FFFFFF", bd=2, relief="solid")
task_input.pack(pady=(15, 5))

# Configuración de Listbox con fondo oscuro y letras blancas
tasks_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE, bg="#333333", fg="#FFFFFF", 
                           font=('Arial', 10), bd=2, relief="solid", highlightcolor="#666666", 
                           selectbackground="#555555", selectforeground="#FFFFFF")
tasks_listbox.pack(fill=tk.BOTH, expand=True, pady=5, padx=10)

# Configuración de botones con estilo personalizado
add_button = tk.Button(root, text="Añadir tarea", width=20, command=add_task, bg="#5CB85C", fg="#FFFFFF", font=('Arial', 10, 'bold'), bd=0)
delete_button = tk.Button(root, text="Eliminar tarea", width=20, command=delete_task, bg="#D9534F", fg="#FFFFFF", font=('Arial', 10, 'bold'), bd=0)
mark_button = tk.Button(root, text="Marcar como completada", width=20, command=mark_task, bg="#5BC0DE", fg="#FFFFFF", font=('Arial', 10, 'bold'), bd=0)

add_button.pack(pady=5)
delete_button.pack(pady=5)
mark_button.pack(pady=5)

# Iniciar el bucle de la ventana
root.mainloop()
