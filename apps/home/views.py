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
                "basics": {
                    "url": "#tabs-basics",
                    "name": "Basics",
                },
                "squad": {
                    "url": "#tabs-squad",
                    "name": "Squad",
                },
                "points": {
                    "url": "#tabs-points",
                    "name": "Scoring Points",
                },
                "auction": {
                    "url": "#tabs-auction",
                    "name": "Auction",
                },
                "sealed": {
                    "url": "#tabs-sealed",
                    "name": "Sealed Bids",
                },
                "transfers": {
                    "url": "#tabs-transfers",
                    "name": "Transfers",
                },
                "faq": {
                    "url": "#tabs-faq",
                    "name": "FAQ",
                },
            },
        }
        return render(request, self.template_name, context)
