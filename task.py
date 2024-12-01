class Task:
    def __init__(self, task_id: str, title: str, description: str, category: str, due_date: str, priority: str, status: str = "Не выполнена"):
        """
        Инициализация объекта Task.

        :param task_id: Уникальный идентификатор задачи (UUID).
        :param title: Название задачи.
        :param description: Описание задачи.
        :param category: Категория задачи.
        :param due_date: Срок выполнения задачи.
        :param priority: Приоритет задачи.
        :param status: Статус задачи (по умолчанию "Не выполнена").
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self) -> dict:
        """
        Преобразует объект Task в словарь.

        :return: Словарь с данными задачи.
        """
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }
