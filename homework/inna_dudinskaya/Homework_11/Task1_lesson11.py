class Book:
    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, ISBN, is_the_book_reserved=False):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.is_the_book_reserved = is_the_book_reserved

    def __str__(self):
        base_info = (f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_of_pages}, "
                     f"материал: {self.page_material}")
        if self.is_the_book_reserved:
            return f"{base_info}, зарезервирована"
        return base_info


book_1 = Book('Идиот', 'Достоевский', 500, '978-5-1712-3025-8', True)

book_2 = Book('Приключения Чиполлино', 'Джанни Родари', 260, '978-5-699-76231-6')

book_3 = Book('Волшебник Изумрудного города', 'Волков', 190, '978-5-353-07281-2')

book_4 = Book('Пес по имени Мани', 'Бодо Шефер', 190, '978-985-15-5530-3')

book_5 = Book('Сказки', 'Андерсен', 124, '978-5-353-10198-7')

print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)
