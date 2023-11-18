from django import forms

from library_db.models import Rank, Server
from uprank.choices import *


class UpRankForm(forms.Form):
    CURRENT_LP_CHOICES = [
        "0-20 LP", "21-40 LP", "41-60 LP", "61-80 LP", "81-99 LP"
    ]

    ranks = Rank.objects.values('name').distinct()
    rank_positions = Rank.objects.values('position').distinct()

    RANK_CHOICES = [
        (rank['name'], rank['name']) for rank in ranks
    ]

    RANK_POSITION_CHOICES = [
        (rank['position'], rank['position']) for rank in rank_positions
    ]

    servers = Server.objects.values('name').distinct()
    SERVER_CHOICES = [
        (server['name'], server['name']) for server in servers
    ]

    current_rank = forms.ChoiceField(
        choices=RANK_CHOICES,
        label_suffix="",
        label="",
        widget=forms.Select(
            attrs={
                'class': "select-input",
            }
        ),
    )
    current_rank_position = forms.ChoiceField(
        choices=RANK_POSITION_CHOICES,
        label_suffix="",
        label="",
        widget=forms.Select(
            attrs={
                'class': "select-input",
            }
        ),
    )

    lp_gain = forms.ChoiceField(
        choices=LP_GAIN_CHOICES,
        label_suffix="",
        label="",
        widget=forms.Select(
            attrs={
                'class': "select-input",
            }
        ),
    )
    current_lp = forms.ChoiceField(
        choices=[(choice, choice) for choice in CURRENT_LP_CHOICES],
        label_suffix="",
        label="",
        widget=forms.Select(
            attrs={
                'class': "select-input",
            }
        ),
    )
    desired_rank = forms.ChoiceField(
        choices=RANK_CHOICES,
        label_suffix="",
        label="",
        widget=forms.Select(
            attrs={
                'class': "select-input",
            }
        ),
    )
    desired_rank_position = forms.ChoiceField(
        choices=RANK_POSITION_CHOICES,
        label_suffix="",
        label="",
        widget=forms.Select(
            attrs={
                'class': "select-input",
            }
        ),
    )
    server = forms.ChoiceField(
        choices=SERVER_CHOICES,
        label_suffix="",
        label="",
        widget=forms.Select(
            attrs={
                'class': "select-input",
            }
        ),
    )

    priority_order = forms.BooleanField(
        label="",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': "checkbox-input",
            }
        ),
    )
    stream_games = forms.BooleanField(
        label="",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': "checkbox-input",
            }
        ),
    )
