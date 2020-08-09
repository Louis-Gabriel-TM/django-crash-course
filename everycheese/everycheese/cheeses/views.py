from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from .models import Cheese


class CheeseListView(ListView):

    model = Cheese


class CheeseDetailView(DetailView):

    model = Cheese


class CheeseCreateView(LoginRequiredMixin, CreateView):

    model = Cheese

    fields = [
        'name',
        'firmness',
        'country_of_origin',
        'description',
    ]
