from django.urls import reverse, resolve
import pytest

from everycheese.users.models import User


pytestmark = pytest.mark.django_db


def test_detail(user: User):
    assert (
        reverse("users:detail", kwargs={"username": user.username})
        == f"/utilisateurs/{user.username}/"
    )
    assert (
        resolve(f"/utilisateurs/{user.username}/").view_name
        == "users:detail"
    )


def test_update():
    assert reverse("users:update") == "/utilisateurs/~update/"
    assert resolve("/utilisateurs/~update/").view_name == "users:update"


def test_redirect():
    assert reverse("users:redirect") == "/utilisateurs/~redirect/"
    assert (
        resolve("/utilisateurs/~redirect/").view_name == "users:redirect"
    )
