from datetime import date
from django.db import models


class FantasyFootballSeason(models.Model):
    """Models a football season"""

    year = models.CharField(max_length=4)
    start = models.DateField()
    end = models.DateField()
    enableUpdates = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def current_season():
        """
        Find the current date and work out the appropriate string for the
        current season.
        """
        current_date = date.today()

        # From July onwards use the current year
        if current_date.month >= 7:
            return str(current_date.year)

        # From Jan to June use the previous year
        return str(current_date.year - 1)

    def date_to_week(self, date_to_convert: date):
        """
        Return the week of the season within which the specified date lies.
        The first day of the season is the start of week 1.
        """
        delta = date_to_convert - self.start
        week = delta.days // 7 + 1

        assert 0 < week < 52

        return week

    def total_weeks(self):
        """Return the number of weeks in the season"""
        return self.date_to_week(self.end) + 1

    def current_week(self):
        """Return the week we are currently in"""
        today = date.today()

        if today < self.start:
            return 0

        if today > self.end:
            return self.total_weeks() + 1

        return self.date_to_week(today)


class FantasyFootballPlayerSeason(models.Model):
    """Models a football player over the course of a season"""

    name = models.CharField(max_length=50)
    position = models.CharField(
        choices=[("GK", "GK"), ("FB", "FB"), ("CB", "CB"), ("MF", "MF"), ("ST", "ST")],
        max_length=2)
    club = models.CharField(max_length=3)
    status = models.CharField(
        choices=[
            ("FIT", "Fit"),
            ("INJURED", "Injured"),
            ("SUSPENDED", "Suspended"),
            ("DOUBTFUL", "Doubtful"),
            ("INELIGIBLE", "Ineligible"),
            ("LFT", "Late Fitness Test"),
            ("INTERNATIONAL", "International"),
        ],
        max_length=20,
    )
    reason = models.CharField(max_length=100, blank=True)
    season = models.ForeignKey(FantasyFootballSeason, on_delete=models.CASCADE)
    points_last_season = models.IntegerField(default=0)
    week_scores = models.JSONField(default=list)
    url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
