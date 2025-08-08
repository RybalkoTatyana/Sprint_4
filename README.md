## Описание тестовых функций для класса *BooksCollector*

### Создание объекта вынесено фикстурой в конфтест

1. Тест с параметризацией проверяет добавление новых книг в список 
```
    @pytest.mark.parametrize('book', ['КПД3', 'Осров сокровищ'])
    def test_add_new_book_positive(self, books_collector, book):
        books_collector.add_new_book(book)
        assert books_collector.books_genre[book] == ''
```
---
2. Тест добавляет новую книгу и проверяет её жанр
```
    def test_set_book_genre_valid_name(self, books_collector):
        books_collector.add_new_book('Комедийная книга')
        books_collector.set_book_genre('Комедийная книга', 'Комедии')
        assert books_collector.books_genre['Комедийная книга'] == 'Комедии'
``` 
---
3. Тест проверяет возвращение жанра книги по названию.
Проверяется что по названию возвращается жанр.
```
    def test_get_book_genre_return_valid_name(self, books_collector):
        books_collector.add_new_book('Аватар')
        books_collector.set_book_genre('Аватар', 'Фантастика')
        assert books_collector.get_book_genre('Аватар') == 'Фантастика'
```
---
4. Тест проверяет что выводится список книг по определенным жанрам.
Добавляется книга, задается жанр, проверяется жанр и проверяется что отдается список
```
    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):
        books_collector.add_new_book('Головоломка')
        books_collector.set_book_genre('Головоломка', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list
```
---
5. Тест проверяет что в список добавились все книги и что все они помещаются в словарь.
Циклом добавляем книги, в переменную кладем рандомное название книги и проверяем.
```
    def test_get_books_genre_filled_dict(self, books_collector):
        books = ['Рататуй', '3 мушкетера', 'Гарри Поттер', 'Эрагон', '3 долматинца']
        for name in books:
            books_collector.add_new_book(name)
        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
            and type(books_collector.get_books_genre()) == dict
```
---
6. Тест проверяет что в списке с книгами есть только книги с рейтингом для детей.
Циклом создаем список и добавляем всем книгам разные жанры.
Вторым циклом проверяем есть ли в первом списке жанры 18+
```
    def test_get_books_for_children_correct_genre(self, books_collector):
        books = ['1 правило волшебника', '2 правило волшебника', '3 правило волшебника', '4 правило волшебника', '5 правило волшебника']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1
        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()
```
---
7. Тест проверяет что книга добавленная в избранное есть в избранном 
Циклом добавляем книги в список, затм добавляем одну книгу по названию в избранное ищем нужную книгу
```
    def test_add_book_in_favorites_when_books_in_list(self, books_collector):
        books = ['Рататуй', 'Рататуй2', 'Рататуй3', 'Рататуй4']
        for name in books:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites('Рататуй')
        assert 'Рататуй' in books_collector.favorites
```
---
8. Тест проверяет что книга добавленная в избранное есть в избранном
Добавляем книгу в список, добавляем эту книгу по названию в избранное , удаляем ее оттуда и проверяем список. Книги быть не должно.
```
    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book('Шерлок Холмс')
        books_collector.add_book_in_favorites('Шерлок Холмс')
        books_collector.delete_book_from_favorites('Шерлок Холмс')
        assert 'Шерлок Холмс' not in books_collector.favorites
```
---
9. Тест проверяет метод который возвращает список избранных книг.
Циклом добавляем книги в список, затем добавляем  всех в избранное.
Ассертим получение списка.
```
    def test_get_list_of_favorites_books_not_empty(self, books_collector):
        books = ['Книга1', 'Книга 2', 'Книга 3']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)
        assert books_collector.get_list_of_favorites_books()
```
---