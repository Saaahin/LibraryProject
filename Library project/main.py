class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def __str__(self):
        return f"Название: {self.title} \n Автор: {self.author} \n Год: {self.year}"


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Книга успешно добавлена!")

    def show_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("\n===== СПИСОК КНИГ =====")
            for book in self.books:
                print(book)

    # Выдать книгу
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "Доступна":
                    book.status = "Выдана"
                    print("Книга успешно выдана!")
                    return True
                else:
                    print("Эта книга уже выдана.")
                    return False

        print("Книга не найдена.")
        return False
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "Выдана":
                    book.status = "Доступна"
                    print("Книга успешно возвращена!")
                    return True
                else:
                    print("Эта книга не была выдана.")
                    return False

        print("Книга не найдена.")
        return False

library = Library()
if __name__ == "__main__":
    while True:
        print("\n===== МОЯ БИБЛИОТЕКА =====")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Взять книгу")
        print("4. Вернуть книгу")
        print("5. Выход")

        choice = input("Выберите действие - ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            year = int(input("Введите год выпуска: "))

            book = Book(title, author, year)
            library.add_book(book)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            title = input("Введите название книги: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("Введите название книги: ")
            library.return_book(title)

        elif choice == "5":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")