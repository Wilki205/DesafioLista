from tkinter import simpledialog, messagebox

tarefas = []

def listar_tarefas():
    if tarefas:
        msg = "\n".join(f"{i+1}. {tarefa}" for i, tarefa in enumerate(tarefas))
    else:
        msg = "Nenhuma tarefa cadastrada."
    messagebox.showinfo("Lista de Tarefas", msg)

def inserir_tarefa():
    nova = simpledialog.askstring("Inserir Tarefa", "Digite a nova tarefa:")
    if nova:
        tarefas.append(nova)
        messagebox.showinfo("Sucesso", "Tarefa adicionada!")

def deletar_tarefa():
    if not tarefas:
        messagebox.showwarning("Aviso", "Nenhuma tarefa para deletar.")
        return
    indice = simpledialog.askinteger("Deletar Tarefa", "Digite o número da tarefa para deletar:")
    if indice and 1 <= indice <= len(tarefas):
        removida = tarefas.pop(indice - 1)
        messagebox.showinfo("Sucesso", f"Tarefa '{removida}' removida.")
    else:
        messagebox.showerror("Erro", "Índice inválido.")
