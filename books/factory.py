import datetime

from books.models import Book, Publisher
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDate, FuzzyInteger


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    isbn = FuzzyChoice(("978-4-7981-6364-1", "978-4-7981-6364-2"))
    title = FuzzyChoice(("タイトル1", "タイトル2"))
    price = FuzzyInteger(0, 10000)
    publisher = FuzzyChoice(Publisher)
    published = FuzzyDate(datetime.date(2008, 1, 1))
