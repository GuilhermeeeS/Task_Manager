from tasks import TaskManager

def show_menu():
    print("\nGerenciador de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas Pendentes")
    print("3. Listar Tarefas Concluídas")
    print("4. Marcar Tarefa como Concluída")
    print("5. Remover Tarefa")
    print("6. Filtrar Tarefas por Prioridade")
    print("0. Sair")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            description = input("Descrição: ")
            deadline = input("Prazo (AAAA-MM-DD): ")
            priority = input("Prioridade (alta, média, baixa): ")
            manager.add_task(description, deadline, priority)
        elif choice == "2":
            print("\nTarefas Pendentes:")
            manager.list_tasks(completed=False)
        elif choice == "3":
            print("\nTarefas Concluídas:")
            manager.list_tasks(completed=True)
        elif choice == "4":
            manager.list_tasks(completed=False)
            task_index = int(input("Número da Tarefa para concluir: ")) - 1
            manager.complete_task(task_index)
        elif choice == "5":
            manager.list_tasks(completed=False)
            task_index = int(input("Número da Tarefa para remover: ")) - 1
            manager.remove_task(task_index)
        elif choice == "6":
            priority = input("Filtrar por prioridade (alta, média, baixa): ")
            manager.filter_tasks_by_priority(priority)
        elif choice == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
