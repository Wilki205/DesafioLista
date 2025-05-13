import tkinter as tk
from biblioteca import listar_tarefas, inserir_tarefa, deletar_tarefa

def sair():
    root.destroy()

root = tk.Tk()
root.title("Lista de Tarefas")

tk.Label(root, text="MENU", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Button(root, text="1 - Listar Tarefas", command=listar_tarefas, width=30).pack(pady=5)
tk.Button(root, text="2 - Inserir Tarefa", command=inserir_tarefa, width=30).pack(pady=5)
tk.Button(root, text="3 - Deletar Tarefa", command=deletar_tarefa, width=30).pack(pady=5)
tk.Button(root, text="4 - Sair", command=sair, width=30).pack(pady=5)

root.protocol("WM_DELETE_WINDOW", sair)
root.mainloop()
