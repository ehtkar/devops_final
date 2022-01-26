from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
def test_create_book():
    book = Book.objects.create(
        title='Pytest',
        genre='testgenre',
        author='John Smith',
    )
    assert book.title == "Pytest"