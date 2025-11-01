import json


def save_tasks(tasks, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Ошибка при сохранении:", e)


def load_tasks(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nСписок задач:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")


def add_task(tasks):
    name = input("Введите название задачи: ").strip()
    if name:
        tasks.append({"task": name, "done": False})
        print(f'Задача "{name}" добавлена!')
    else:
        print("Название задачи не может быть пустым.")


def complete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Введите номер задачи, которую хотите отметить выполненной: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            print(f'Задача "{tasks[idx - 1]["task"]}" отмечена как выполненная.')
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Введите число.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Введите номер задачи для удаления: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f'Задача "{removed["task"]}" удалена.')
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Введите число.")


filename = "tasks.json"
tasks_list = load_tasks(filename)  # загружаем задачи из файла

while True:
    print("\nМеню:")
    print("1. Показать все задачи")
    print("2. Добавить новую задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Выйти")

    choice = input("Выберите пункт меню (1-5): ")

    if choice == "1":
        show_tasks(tasks_list)
    elif choice == "2":
        add_task(tasks_list)
        save_tasks(tasks_list, filename)
    elif choice == "3":
        complete_task(tasks_list)
        save_tasks(tasks_list, filename)
    elif choice == "4":
        delete_task(tasks_list)
        save_tasks(tasks_list, filename)
    elif choice == "5":
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор! Попробуйте снова.")

