from django.views.generic import DetailView, ListView

from .models import Cheese


class CheeseListView(ListView):

    model = Cheese


class CheeseDetailView(DetailView):

    model = Cheese
