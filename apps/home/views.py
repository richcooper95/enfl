from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    """Home view."""
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class HallOfFameView(TemplateView):
    """Hall of fame view."""
    template_name = "hall_of_fame.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class PositionsView(TemplateView):
    """Positions view."""
    template_name = "positions.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class RulesView(TemplateView):
    """Rules view."""
    template_name = "rules.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
