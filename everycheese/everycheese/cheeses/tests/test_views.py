from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

from .factories import CheeseFactory
from ..models import Cheese
from ..views import (
    CheeseCreateView,
    CheeseDetailView,
    CheeseListView,
)
from everycheese.users.models import User


pytestmark = pytest.mark.django_db


def test_good_cheese_list_view_expanded(rf):  # rf: pytest shortcut for django.test.RequestFactory
    # determine the URL:
    url = reverse('cheeses:list')

    # generate a request as if from a user accessing the cheese list view:
    request = rf.get(url)

    # call as_view() to make a callable object (callable_obj is analoguous to a function-based view):
    callable_obj = CheeseListView.as_view()

    # pass in the request into the callable object to get an HTTP response served up by Django:
    response = callable_obj(request)

    # test that the HTTP response has "Liste des fromages" in the HTML and has a 200 status code
    assertContains(response, "Liste des fromages")

def test_good_cheese_list_view_expanded_short_version(rf):
    # get the request:
    request = rf.get(reverse('cheeses:list'))

    # use the request to get a response:
    response = CheeseListView.as_view()(request)

    # test that the response is valid:
    assertContains(response, "Liste des fromages")

def test_cheese_list_contains_2_cheeses(rf):
    cheese_1 = CheeseFactory()
    cheese_2 = CheeseFactory()
    request = rf.get(reverse('cheeses:list'))
    response = CheeseListView.as_view()(request)
    assertContains(response, cheese_1.name)
    assertContains(response, cheese_2.name)

def test_good_cheese_detail_view(rf):
    cheese = CheeseFactory()
    url = reverse(
        'cheeses:detail', 
        kwargs={'slug': cheese.slug},
    )
    request = rf.get(url)
    response = CheeseDetailView.as_view()(request, slug=cheese.slug)
    #assertContains(response, cheese.name)

def test_detail_contains_cheese_data(rf):
    cheese = CheeseFactory()
    url = reverse(
        'cheeses:detail',
        kwargs={'slug': cheese.slug},
    )
    request = rf.get(url)
    response = CheeseDetailView.as_view()(request, slug=cheese.slug)
    #assertContains(response, cheese.name)
    #assertContains(response, cheese.get_firmness_display())
    #assertContains(response, cheese.country_of_origin.name)

def test_good_cheese_create_view(rf, admin_user):
    cheese = CheeseFactory()
    request = rf.get(reverse('cheeses:add'))
    request.user = admin_user  # add an authenticated user
    response = CheeseCreateView.as_view()(request)
    assert response.status_code == 200

def test_cheese_create_form_valid(rf, admin_user):
    form_data = {
        'name': "Paski Sir",
        'description': "Un fromage dur salé",
        'firmness': Cheese.Firmness.HARD,
    }
    request = rf.post(reverse('cheeses:add'), form_data)
    request.user = admin_user
    response = CheeseCreateView.as_view()(request)
    cheese = Cheese.objects.get(name="Paski Sir")
    assert cheese.description == "Un fromage dur salé"
    assert cheese.firmness == Cheese.Firmness.HARD
    assert cheese.creator == admin_user
