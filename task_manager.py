def create_task(title, description):
    # Логика создания задачи
    print(f"Создана новая задача: {title}")
    task = Task(title,description)
    task.save()
    print(f"Сохранили задачу: {title}")
