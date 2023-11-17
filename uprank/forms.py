from django import forms


class UpRankForm(forms.Form):
    LP_GAIN_CHOICES = [
        "14 LP or less", "15 LP or more", "20 LP or more", "25 LP or more", "34 LP or more"
    ]
    CURRENT_LP_CHOICES = [
        "0-20 LP", "21-40 LP", "41-60 LP", "61-80 LP", "81-99 LP"
    ]

    lp_gain = forms.ChoiceField(
        choices=[(choice, choice) for choice in LP_GAIN_CHOICES],
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
