tarefas = []

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def inserir_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def deletar_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para deletar: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\nMENU")
        print("1 - Listar Tarefas")
        print("2 - Inserir Tarefa")
        print("3 - Deletar Tarefa")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas()
        elif opcao == "2":
            inserir_tarefa()
        elif opcao == "3":
            deletar_tarefa()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()