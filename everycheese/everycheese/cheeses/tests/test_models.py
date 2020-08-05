import pytest

from ..models import Cheese


pytestmark = pytest.mark.django_db


def test__str__():
    cheese = Cheese.objects.create(
        name="Stracchino",
        description="Fromage semi-doux idéal pour les soirées guindées",
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
