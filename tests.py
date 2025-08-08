import random
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize('book', ['КПД3', 'Осров сокровищ'])
    def test_add_new_book_positive(self, books_collector, book):
        books_collector.add_new_book(book)
        assert books_collector.books_genre[book] == ''

    def test_set_book_genre_valid_name(self, books_collector):
        books_collector.add_new_book('Комедийная книга')
        books_collector.set_book_genre('Комедийная книга', 'Комедии')
        assert books_collector.books_genre['Комедийная книга'] == 'Комедии'

    def test_get_book_genre_return_valid_name(self, books_collector):
        books_collector.add_new_book('Аватар')
        books_collector.set_book_genre('Аватар', 'Фантастика')
        assert books_collector.get_book_genre('Аватар') == 'Фантастика'

    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):
        books_collector.add_new_book('Головоломка')
        books_collector.set_book_genre('Головоломка', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list

    def test_get_books_genre_filled_dict(self, books_collector):
        books = ['Рататуй', '3 мушкетера', 'Гарри Поттер', 'Эрагон', '3 долматинца']
        for name in books:
            books_collector.add_new_book(name)
        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
            and type(books_collector.get_books_genre()) == dict

    def test_get_books_for_children_correct_genre(self, books_collector):
        books = ['1 правило волшебника', '2 правило волшебника', '3 правило волшебника', '4 правило волшебника', '5 правило волшебника']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1
        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()


    def test_add_book_in_favorites_when_books_in_list(self, books_collector):
        books = ['Рататуй', 'Рататуй2', 'Рататуй3', 'Рататуй4']
        for name in books:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites('Рататуй')
        assert 'Рататуй' in books_collector.favorites

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book('Шерлок Холмс')
        books_collector.add_book_in_favorites('Шерлок Холмс')
        books_collector.delete_book_from_favorites('Шерлок Холмс')
        assert 'Шерлок Холмс' not in books_collector.favorites

    def test_get_list_of_favorites_books_not_empty(self, books_collector):
        books = ['Книга1', 'Книга 2', 'Книга 3']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)
        assert books_collector.get_list_of_favorites_books()
