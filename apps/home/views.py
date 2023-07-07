from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    """Home view."""

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class HallOfFameView(LoginRequiredMixin, TemplateView):
    """Hall of fame view."""

    template_name = "hall_of_fame.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class PositionsView(LoginRequiredMixin, TemplateView):
    """Positions view."""

    template_name = "positions.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class RulesView(TemplateView):
    """Rules view."""

    template_name = "rules.html"

    def get(self, request, *args, **kwargs):
        context = {
            "tabs": {
                k: {"url": f"#tabs-{k}", "name": v}
                for k, v in [
                    ("basics", "Basics"),
                    ("squad", "Squad"),
                    ("points", "Scoring Points"),
                    ("auction", "Auction"),
                    ("sealed", "Sealed Bids"),
                    ("transfers", "Transfers"),
                    ("faq", "FAQ"),
                ]
            }
        }

        return render(request, self.template_name, context)
