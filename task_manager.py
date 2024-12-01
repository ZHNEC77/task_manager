from task_manager_class import TaskManager


def main():
    manager = TaskManager('data/tasks.json')

    while True:
        print("\nМеню:")
        print("1. Просмотреть все задачи")
        print("2. Просмотреть задачи по категории")
        print("3. Добавить задачу")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Поиск задач")
        print("7. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':
                tasks = manager.view_tasks()
                for task in tasks:
                    print(task)
            elif choice == '2':
                category = input("Введите категорию: ")
                tasks = manager.view_tasks(category)
                for task in tasks:
                    print(task)
            elif choice == '3':
                title = input("Название: ")
                description = input("Описание: ")
                category = input("Категория: ")
                due_date = input("Срок выполнения (ГГГГ-ММ-ДД): ")
                priority = input("Приоритет (Низкий, Средний, Высокий): ")
                manager.add_task(title, description,
                                 category, due_date, priority)
            elif choice == '4':
                task_id = input("Введите ID задачи: ")
                title = input(
                    "Новое название (оставьте пустым, если не хотите менять): ")
                description = input(
                    "Новое описание (оставьте пустым, если не хотите менять): ")
                category = input(
                    "Новая категория (оставьте пустым, если не хотите менять): ")
                due_date = input(
                    "Новый срок выполнения (оставьте пустым, если не хотите менять): ")
                priority = input(
                    "Новый приоритет (оставьте пустым, если не хотите менять): ")
                status = input(
                    "Статус (Выполнена/Не выполнена) (оставьте пустым, если не хотите менять): ")
                manager.edit_task(task_id, title, description,
                                  category, due_date, priority, status)
            elif choice == '5':
                task_id = input("Введите ID задачи: ")
                manager.delete_task(task_id)
            elif choice == '6':
                keyword = input(
                    "Ключевое слово (оставьте пустым, если не хотите искать): ")
                category = input(
                    "Категория (оставьте пустым, если не хотите искать): ")
                status = input(
                    "Статус (оставьте пустым, если не хотите искать): ")
                tasks = manager.search_tasks(keyword, category, status)
                for task in tasks:
                    print(task)
            elif choice == '7':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    main()
