CHAT_FILE = "chat.txt"


def initialize_chat_file():
    try:
        with open(CHAT_FILE, "x", encoding="utf-8"):
            pass
    except FileExistsError:
        pass


def get_username():
    while True:
        username = input("Введите ваше имя: ").strip()
        if username:
            return username
        print("Имя не может быть пустым!")


def show_chat():
    try:
        with open(CHAT_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print("\n----- Чат -----")
                print(content)
                print("---------------\n")
            else:
                print("\nЧат пока пуст.\n")
    except FileNotFoundError:
        print("Файл чата не найден.")


def send_message(username):
    message = input("Введите сообщение: ").strip()
    
    if not message:
        print("Сообщение не может быть пустым.")
        return

    with open(CHAT_FILE, "a", encoding="utf-8") as file:
        file.write(f"{username}: {message}\n")

    print("Сообщение отправлено!\n")


def show_menu():
    print("Выберите действие:")
    print("1 — Посмотреть чат")
    print("2 — Отправить сообщение")


def main():
    initialize_chat_file()
    username = get_username()

    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            show_chat()
        elif choice == "2":
            send_message(username)
        else:
            print("Некорректный выбор. Введите 1 или 2.\n")


if __name__ == "__main__":
    main()