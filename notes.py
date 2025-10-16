import json

filename = 'notes.json'


def load_notes():
    """Загружает заметки из файла (если он есть)."""
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_notes(notes):
    """Сохраняет заметки в файл."""
    with open(filename, 'w') as f:
        json.dump(notes, f)


def show_notes(notes):
    """Показывает все заметки."""
    if not notes:
        print("Пока нет заметок.")
    else:
        print("\nТвои заметки:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")


def add_note(notes):
    """Добавляет новую заметку."""
    note = input("Введите текст заметки: ")
    notes.append(note)
    save_notes(notes)
    print("Заметка сохранена!\n")


def main():
    notes = load_notes()
    while True:
        print("\nМеню:")
        print("1. Показать заметки")
        print("2. Добавить заметку")
        print("3. Выйти")

        choice = input("Выберите пункт: ")

        if choice == '1':
            show_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            print("До встречи!")
            break
        else:
            print("Неверный выбор, попробуй ещё раз.")


main()
