from django.urls import resolve, reverse
import pytest

from .factories import CheeseFactory


pytestmark = pytest.mark.django_db


@pytest.fixture
def cheese():
    return CheeseFactory()

def test_list_reverse():
    assert reverse('cheeses:list') == '/les-fromages/'

def test_list_resolve():
    assert resolve('/les-fromages/').view_name == 'cheeses:list'

def test_add_reverse():
    assert reverse('cheeses:add') == '/les-fromages/creer/'

def test_add_resolve():
    assert resolve('/les-fromages/creer/').view_name == 'cheeses:add'

def test_detail_reverse(cheese):
    url = reverse(
        'cheeses:detail',
        kwargs={'slug': cheese.slug},
    )
    assert url == f'/les-fromages/{cheese.slug}/'

def test_detail_resolve(cheese):
    url = f'/les-fromages/{cheese.slug}/'
    assert resolve(url).view_name == 'cheeses:detail'