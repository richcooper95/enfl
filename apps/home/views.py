from typing import Dict, List, Tuple

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


def get_tabs(tabs: List[Tuple[str, str]]) -> Dict[str, Dict[str, str]]:
    return {k: {"url": f"#tabs-{k}", "name": v} for k, v in tabs}


# Create your views here.
class HomeView(TemplateView):
    """Home view."""

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {"tabs": get_tabs([("home", "Home")])}

        return render(request, self.template_name, context)


class HallOfFameView(LoginRequiredMixin, TemplateView):
    """Hall of fame view."""

    template_name = "hall_of_fame.html"

    def get(self, request, *args, **kwargs):
        context = {"tabs": get_tabs([("winners", "Hall of Fame")])}

        return render(request, self.template_name, context)


class PositionsView(LoginRequiredMixin, TemplateView):
    """Positions view."""

    template_name = "positions.html"

    def get(self, request, *args, **kwargs):
        context = {"tabs": get_tabs([("final-positions", "Positions")])}

        return render(request, self.template_name, context)


class RulesView(TemplateView):
    """Rules view."""

    template_name = "rules.html"

    def get(self, request, *args, **kwargs):
        context = {
            "tabs": get_tabs(
                [
                    ("basics", "Basics"),
                    ("squad", "Squad"),
                    ("points", "Scoring Points"),
                    ("auction", "Auction"),
                    ("sealed", "Sealed Bids"),
                    ("transfers", "Transfers"),
                    ("faq", "FAQ"),
                ]
            )
        }

        return render(request, self.template_name, context)
