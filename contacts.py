import json
import os


def save_contacts(contacts, filename):
    """Сохраняет контакты в файл JSON с красивым форматированием"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Ошибка при сохранении файла:", e)


filename = 'contacts.json'

# Загружаем контакты, если файл существует
if os.path.exists(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contacts = json.load(f)
    except json.JSONDecodeError:
        print("Файл повреждён, создаётся новый список контактов.")
        contacts = []
    except Exception as e:
        print("Ошибка при открытии файла:", e)
        contacts = []
else:
    contacts = []

while True:
    print("\nМеню:")
    menu = {
        1: 'Показать все контакты',
        2: 'Добавить новый контакт',
        3: 'Удалить контакт',
        4: 'Выйти'
    }
    for key, value in menu.items():
        print(key, value)

    try:
        choice = int(input('Выберите пункт: '))
    except ValueError:
        print("Введи число от 1 до 4.")
        continue

    if choice == 1:
        if not contacts:
            print("Список контактов пуст.")
        else:
            print("\nСписок контактов:")
            for i, c in enumerate(contacts, 1):
                name = c.get('name', '')
                phone = c.get('phone', '')
                email = c.get('email', '')
                print(f"{i}. {name} — {phone}" + (f" — {email}" if email else ""))

    elif choice == 2:
        name = input('Имя: ').strip()
        phone = input('Телефон: ').strip()
        email = input('Email (необязательно): ').strip()

        if not name or not phone:
            print('Имя и телефон обязательны!')
        else:
            contact = {'name': name, 'phone': phone, 'email': email}
            contacts.append(contact)
            save_contacts(contacts, filename)
            print('Контакт успешно добавлен!')

    elif choice == 3:
        if not contacts:
            print("Нечего удалять — список пуст.")
        else:
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c.get('name', '')} — {c.get('phone', '')}")
            try:
                idx = int(input("Введите номер контакта для удаления: "))
                if 1 <= idx <= len(contacts):
                    removed = contacts.pop(idx - 1)
                    save_contacts(contacts, filename)
                    print(f"Контакт {removed.get('name')} удалён.")
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Введи, пожалуйста, число.")

    elif choice == 4:
        print("Выход из программы...")
        break
    else:
        print("Неверный пункт меню, выбери от 1 до 4.")
