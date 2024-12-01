import json
import os
import uuid
from task import Task
from typing import List, Optional


class TaskManager:
    def __init__(self, file_path: str):
        """
        Инициализация объекта TaskManager.

        :param file_path: Путь к файлу для хранения задач.
        """
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[dict]:
        """
        Загружает задачи из файла.

        :return: Список задач.
        """
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            return []
        except json.JSONDecodeError:
            print("Ошибка чтения файла. Возможно, файл поврежден.")
            return []

    def save_tasks(self):
        """
        Сохраняет задачи в файл.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError:
            print("Ошибка записи в файл.")

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str):
        """
        Добавляет новую задачу.

        :param title: Название задачи.
        :param description: Описание задачи.
        :param category: Категория задачи.
        :param due_date: Срок выполнения задачи.
        :param priority: Приоритет задачи.
        """
        try:
            if not title or not description or not category or not due_date or not priority:
                raise ValueError("Все поля должны быть заполнены.")
            task_id = str(uuid.uuid4())
            new_task = Task(task_id, title, description,
                            category, due_date, priority).to_dict()
            self.tasks.append(new_task)
            self.save_tasks()
        except ValueError as e:
            print(f"Ошибка добавления задачи: {e}")

    def view_tasks(self, category: Optional[str] = None) -> List[dict]:
        """
        Возвращает список задач.

        :param category: Категория задач для фильтрации (опционально).
        :return: Список задач.
        """
        if category:
            return [task for task in self.tasks if task['category'] == category]
        return self.tasks

    def edit_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None, category: Optional[str] = None, due_date: Optional[str] = None, priority: Optional[str] = None, status: Optional[str] = None) -> bool:
        """
        Редактирует существующую задачу.

        :param task_id: Идентификатор задачи.
        :param title: Новое название задачи (опционально).
        :param description: Новое описание задачи (опционально).
        :param category: Новая категория задачи (опционально).
        :param due_date: Новый срок выполнения задачи (опционально).
        :param priority: Новый приоритет задачи (опционально).
        :param status: Новый статус задачи (опционально).
        :return: True, если задача была отредактирована, иначе False.
        """
        try:
            for task in self.tasks:
                if task['id'] == task_id:
                    if title:
                        task['title'] = title
                    if description:
                        task['description'] = description
                    if category:
                        task['category'] = category
                    if due_date:
                        task['due_date'] = due_date
                    if priority:
                        task['priority'] = priority
                    if status:
                        task['status'] = status
                    self.save_tasks()
                    return True
            raise ValueError("Задача с указанным ID не найдена.")
        except ValueError as e:
            print(f"Ошибка редактирования задачи: {e}")
            return False

    def delete_task(self, task_id: str):
        """
        Удаляет задачу по идентификатору.

        :param task_id: Идентификатор задачи.
        """
        try:
            self.tasks = [task for task in self.tasks if task['id'] != task_id]
            self.save_tasks()
        except ValueError as e:
            print(f"Ошибка удаления задачи: {e}")

    def search_tasks(self, keyword: Optional[str] = None, category: Optional[str] = None, status: Optional[str] = None) -> List[dict]:
        """
        Ищет задачи по ключевым словам, категории или статусу.

        :param keyword: Ключевое слово для поиска (опционально).
        :param category: Категория для поиска (опционально).
        :param status: Статус для поиска (опционально).
        :return: Список найденных задач.
        """
        result = self.tasks
        if keyword:
            result = [task for task in result if keyword.lower() in task['title'].lower(
            ) or keyword.lower() in task['description'].lower()]
        if category:
            result = [task for task in result if task['category'] == category]
        if status:
            result = [task for task in result if task['status'] == status]
        return result
