import sys
from database import save_survey

def ask_question(prompt):
    """Запрашивает у пользователя ввод, возвращает строку."""
    return input(prompt).strip()

def main():
    print("Добро пожаловать в опросный агент!")

    while True:
        print("\n--- Новый опрос ---")
        first_name = ask_question("Введите имя: ")
        last_name = ask_question("Введите фамилию: ")
        position = ask_question("Введите должность: ")
        responsibilities = ask_question("Введите должностные обязанности: ")

        # Сохраняем в БД
        try:
            save_survey(first_name, last_name, position, responsibilities)
            print("Данные успешно сохранены!")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            sys.exit(1)

        # Спросить, продолжить ли
        another = input("Хотите добавить ещё одного сотрудника? (y/n): ").strip().lower()
        if another != 'y':
            print("Работа завершена. До свидания!!!")
            break

if __name__ == "__main__":
    main()