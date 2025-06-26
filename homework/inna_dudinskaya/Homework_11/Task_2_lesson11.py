class Book:
    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, ISBN, is_the_book_reserved=False):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.is_the_book_reserved = is_the_book_reserved


class SchoolTextbook(Book):
    def __init__(self, book_title, author, number_of_pages, ISBN, subject, school_class, has_exercises,
                 is_the_book_reserved=False):
        super().__init__(book_title, author, number_of_pages, ISBN, is_the_book_reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises

    def __str__(self):
        base_info = (f"Название: {self.book_title}, Автор: {self.author}, "
                     f"страниц: {self.number_of_pages}, предмет: {self.subject}, "
                     f"класс: {self.school_class}")
        if self.is_the_book_reserved:
            return f"{base_info}, зарезервирована"
        return base_info


textbook1 = SchoolTextbook("Алгебра", "Иванов", 200,
                           "978-5-09-071257-3", "Математика",
                           9, True, True)
textbook2 = SchoolTextbook("История", "Петров", 180,
                           "978-5-09-071258-0", "История", 10, False)
textbook3 = SchoolTextbook("География", "Сидоров", 150,
                           "978-5-09-071259-7", "География", 8, True)
textbook4 = SchoolTextbook("Биология", "Дарвин", 220,
                           "978-5-09-071260-3", "Биология", 7, False)
textbook5 = SchoolTextbook("Физика", "Эйнштейн", 190,
                           "978-5-09-071261-0", "Физика", 11, True)

print(textbook1)
print(textbook2)
print(textbook3)
print(textbook4)
print(textbook5)
