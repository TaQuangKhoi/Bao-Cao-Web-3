from django import forms


class SignInForm(forms.Form):
    template_name = "form_snippet.jinja"
    input_classes = "bg-[#3D3241] text-white/70 outline-none rounded-lg min-w-0 w-full px-4 py-3"

    username = forms.CharField(
        label='Email or username', max_length=100,
        label_suffix="",  # <--- remove semicolon from the end of this line
        widget=forms.TextInput(
            attrs={
                'class': input_classes,
                'placeholder': 'example@email.com'
            }
        )
    )

    password = forms.CharField(
        max_length=32,
        label_suffix="",  # <--- remove semicolon from the end of this line
        widget=forms.PasswordInput(attrs={'class': input_classes})
    )
